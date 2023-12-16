import csv

"""
Call:
lm(formula = guarantee ~ scale + build_age + station_km + univ_km + 
    district, data = dagagu)

Residuals:
     Min       1Q   Median       3Q      Max 
-13487.6  -2506.7     30.5   2568.5  12937.3 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept) 11476.514    191.577  59.905  < 2e-16 ***
scale         134.726      2.483  54.268  < 2e-16 ***
build_age     -88.899      2.762 -32.189  < 2e-16 ***
station_km  -1066.510    111.661  -9.551  < 2e-16 ***
univ_km      -335.004     50.016  -6.698 2.21e-11 ***
districtne  -2138.699    158.235 -13.516  < 2e-16 ***
districtnw  -1712.629    176.652  -9.695  < 2e-16 ***
districtse   -925.629    202.374  -4.574 4.84e-06 ***
districtsw  -1491.633    167.674  -8.896  < 2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 3589 on 11229 degrees of freedom
Multiple R-squared:  0.227,	Adjusted R-squared:  0.2265 
F-statistic: 412.2 on 8 and 11229 DF,  p-value: < 2.2e-16
"""
#다가구, 대학으로부터 3km 이내, 전세만, 전세보증금 2억 이하, 85평방미터 이하.
#계수기술
Intercept = 11476.514
scale = 134.726
build_age = -88.899
station_km = -1066.510
univ_km = -335.004 
district_ne = -2138.699
district_nw = -1712.629
district_se = -925.629
district_sw = -1491.633
csvfile = "./dagagu_add_district_validation.csv"
fr = open(csvfile, 'r', encoding="utf-8-sig")
rdr = csv.reader(fr)
for line in rdr:
    junse = line[15]
    if junse == "junse":#맨첫행 패스
        continue
    elif junse == '0':#전세만
        continue
    else:
        pass
    #전세가 2억 자름
    if int(line[18].replace(',',''))>20000:
        continue
    else:
        pass
    #85제곱미터 자름
    if float(line[14]) > 85:
        continue
    else:
        pass
    scale_input = float(line[14])
    #값없을 때 제외
    if line[20] == "":
        continue
    else:
        pass
    build_age_input = int(line[20].split('.')[0])-2023
    station_km_input = int(line[10])/1000
    #대학 주변 3000미터 자름
    if int(line[12]) > 3000:
        continue
    else:
        pass
    univ_km_input = int(line[12])/1000
    district_input = line[6]
    district_ne_input = 0
    district_nw_input = 0
    district_se_input = 0
    district_sw_input = 0
    if district_input == "cn":
        pass
    elif district_input == "ne":
        district_ne_input = 1
    elif district_input == "nw":
        district_nw_input = 1
    elif district_input == "se":
        district_se_input = 1
    elif district_input == "sw":
        district_sw_input = 1
    
    predicted_y = Intercept 
    predicted_y += scale*scale_input
    predicted_y += build_age*build_age_input 
    predicted_y += station_km*station_km_input
    predicted_y += univ_km*univ_km_input
    predicted_y += district_ne*district_ne_input
    predicted_y += district_nw*district_nw_input
    predicted_y += district_se*district_se_input
    predicted_y += district_sw*district_sw_input
    real_y = int(line[18].replace(',',''))
    print(f"Yhat:{predicted_y}, Y:{real_y}, residual:{real_y-predicted_y}")
