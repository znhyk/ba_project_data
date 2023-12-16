dasedae <- read.csv("dasedae_2.csv", header = TRUE)
# 예제 데이터프레임 생성
#df <- data.frame(기간 = c('202201~202203', '202204~202304', '202207~202209'))
str(dasedae)
plot(x=dasedae$scale, y=dasedae$guarantee, xlab="면적", ylab="가격")
cor(dasedae$scale, dasedae$guarantee)
summary(dasedae$guarantee)


#무작위적으로 섞여있으니 순서대로 하지말고, 주석을 잘 보고 취사선택.

#univ_m이 1000을 초과하는 경우 레코드 제외
dasedae <- dasedae[dasedae$univ_m <= 1000, ]
#term이 '-'인 경우 레코드 제외
dasedae <- dasedae[dasedae$term != '-', ]
#junse가 0(월세)인 경우 레코드 제외
dasedae <- dasedae[dasedae$junse != 0, ]
#junse가 1(전세)인 경우 레코드 제외
dasedae <- dasedae[dasedae$junse != 1, ]
#guarantee 열의 쉼표 있는 숫자를 정수로 변환하여 다시 저장
dasedae$guarantee <- as.integer(gsub(",", "", dasedae$guarantee))
#guarantee가 2000이 넘어가는 경우 레코드 제외
dasedae <- dasedae[dasedae$guarantee < 2000, ]
#건물의 연식으로 변환하여 다시 저장
dasedae$build_age <- 2023 - dasedae$build
#반지하여부를 저장
dasedae$banjiha <- ifelse(dasedae$floor <= -1, 1, 0)
#역과의 거리를 km로 변환
dasedae$station_km <-  dasedae$station_m/1000
#대학과의 거리를 km로 변환
dasedae$univ_km <-  dasedae$univ_m/1000
#term을 정수형으로 바꿔줌
dasedae$term <- as.integer(dasedae$term)
#rent_month를 정수형으로 바꿔줌
dasedae$rent_month <- as.integer(dasedae$rent_month)
#월세총비용(보증금+월세*계약월)을 구함
dasedae$wolse_cost <- dasedae$guarantee + dasedae$term*dasedae$rent_month
#학교 반경 500m를 넘는 레코드 제외
dasedae <- dasedae[dasedae$univ_m <= 500, ]


#다중회귀 돌리기(전세)
result<-lm(
  guarantee~station_km+univ_km+scale+floor+banjiha+build_age,
  data=dasedae)
summary(result)

#우리집: 25제곱미터,14년됨,2층,반지하아님,역으로부터0.348km떨어짐.
14179 - 581 + 9800 + 120 -7462

#다중회귀 돌리기(월세)
result<-lm(
  wolse_cost~station_km+univ_km+scale+floor+banjiha+build_age,
  data=dasedae)
summary(result)

#다중회귀(평당,지하철제거거)(월세) 
result<-lm(
  wolse_cost/scale~univ_m+floor+banjiha+build_age,
  data=dasedae)
summary(result)

#(월세 분석하려면)개월 수 변환!!
library(dplyr)
library(lubridate)

convert_to_months <- function(period) {
  if (grepl("~", period, fixed = TRUE)) {
    periods <- strsplit(period, "~", fixed = TRUE)[[1]]
    start_date <- ymd(paste0(periods[1], "01"))
    end_date <- ymd(paste0(periods[2], "01"))
    months <- interval(start_date, end_date) %/% months(1)
    return(as.numeric(months))
  } else {
    return(as.numeric(period))
  }
}

for (i in seq_along(dasedae$term)) {
  print(paste("Processing row:", i))
  dasedae$term[i] <- convert_to_months(dasedae$term[i])
}

head(dasedae)