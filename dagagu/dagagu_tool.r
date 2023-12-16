dagagu <- read.csv("dagagu_last3.csv", header = TRUE,fileEncoding = "cp949")
#2023년1월1일부터 동년 11월30일까지, 서울시내 다가구주택의 확정일자 신고내역
#해당 데이터를 통하여, 예측회귀분석을 진행, 저평가된 지역을 찾는  것이 첫째 목표표
#학세권 분석을 진행하여 학교 주변이 고평가 되어 있는지 확인하는 것이 두번째 목표
#저평가된 지역 중 여러 기준(업무지구와의 거리, 학교와의 거리)를 이용 최적의 입지와 주거형태를 추천하는 것이 세번째 목표


str(dagagu)
plot(x=dagagu$scale, y=dagagu$guarantee, xlab="면적", ylab="가격")
cor(dagagu$scale, dagagu$guarantee)
summary(dagagu$guarantee)


#univ_m이 1000을 초과하는 경우 레코드 제외
dagagu <- dagagu[dagagu$univ_m <= 3000, ]
#junse가 0(월세)인 경우 레코드 제외
dagagu <- dagagu[dagagu$junse != 0, ]
#guarantee 열의 쉼표 있는 숫자를 정수로 변환하여 다시 저장
dagagu$guarantee <- as.integer(gsub(",", "", dagagu$guarantee))
#guarantee가 특정수치가 넘어가는 경우 레코드 제외
dagagu <- dagagu[dagagu$guarantee < 30000, ]
#scale이 특정수치를 넘으면 레코드 제외
dagagu <- dagagu[dagagu$scale <= 85, ]
#건물의 연식으로 변환하여 다시 저장
dagagu$build_age <- 2023 - dagagu$build
#결측치 삭제
dagagu <- dagagu[complete.cases(dagagu$build_age), ]
#반지하여부를 저장
#dagagu$banjiha <- ifelse(dagagu$floor <= -1, 1, 0)
#역과의 거리를 km로 변환
dagagu$station_km <-  dagagu$station_m/1000
#대학과의 거리를 km로 변환
dagagu$univ_km <-  dagagu$univ_m/1000
#각 업무중심과의 거리를 km로 변환
dagagu$cbd_km <- dagagu$cbd_m/1000
dagagu$gbd_km <- dagagu$gbd_m/1000
dagagu$ybd_km <- dagagu$ybd_m/1000
#제곱미터당 가격 칼럼 생성
dagagu$scaled_guarantee <- dagagu$guarantee/dagagu$scale
#term을 정수형으로 바꿔줌
dagagu$term <- as.integer(dagagu$term)
#rent_month를 정수형으로 바꿔줌
dagagu$rent_month <- as.integer(dagagu$rent_month)
#월세총비용(보증금+월세*계약월)을 구함
dagagu$wolse_cost <- dagagu$guarantee + dagagu$term*dagagu$rent_month
#동대문구만 데이터 빼기
dagagu <- dagagu[grepl("동대문구", dagagu$address), ]

#데이터 나누기
set.seed(123)
num_rows <- round(nrow(dagagu)*0.7)
#0.7을 곱해서 70% 짜르고, 소수점 되면 안되니까 round로 함.
#그러면 정수로 자를 행번호가 나옴
train_index <- sample(1:nrow(dagagu), num_rows)
#sample 명령옳 random sampling해줌.
train_df <- dagagu[train_index,]
validation_df <- dagagu[-train_index,]

#모델1
model <- lm(guarantee~scale+build_age+floor+banjiha+station_km+univ_km+gbd_km, train_df)
#모델2
model <- lm(guarantee~scale+build_age+banjiha+station_km+univ_km+gbd_km+goo, train_df)
#모델3
model <- lm(guarantee~district+scale+build_age+banjiha+station_km+univ_km+gbd_km+total_time_gbd_h, train_df)
#모델4
model <- lm(guarantee~scale+build_age+station_km+univ_km+district, train_df)
summary(model)#잘 안나와도 예측모델이므로 RMSE만 잘 나오면 문제없음
#table(is.na(dagagu$build_age))
#dagagu <- dagagu[complete.cases(dagagu$build_age), ]
#validation_df <- validation_df[complete.cases(dagagu$build_age), ]
validation_df$predicted <- predict(model, validation_df)
validation_df$residuals <- validation_df$guarantee - validation_df$predicted
#View(validation_df[,c("Id","Price","predicted", "residuals")])
#NA제거거
validation_df <- validation_df[complete.cases(validation_df$residuals), ]
# 제거 후 summary 출력
summary(validation_df$residuals)
#한줄에 실제,예측,상관,잔차 다 볼 수 있음
#MSE
mse <- mean((validation_df$guarantee - validation_df$predicted)^2)
#RMSE
rmse <- sqrt(mse)
rmse
#잔차값을 1,0으로 변환하여 저장(under_rated, 1일때 rh평가됨)
validation_df$under_rated <- ifelse(validation_df$residuals < 0, 1, 0)
#엑셀로 저장
install.packages("writexl")
# 패키지 불러오기
library(writexl)
write_xlsx(validation_df, path = "dagagu_predicted_residual.xlsx")