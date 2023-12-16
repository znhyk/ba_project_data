import pandas as pd
from sklearn.model_selection import train_test_split

# CSV 파일 읽기
file_path = 'dagagu_add_district.csv'
df = pd.read_csv(file_path)

# 훈련 데이터셋과 평가 데이터셋으로 나누기
train_df, eval_df = train_test_split(df, test_size=0.3, random_state=42)

# 나눈 데이터셋 저장하기 (예시 파일명)
train_df.to_csv('dagagu_add_district_train.csv', index=False, encoding='utf-8-sig')
eval_df.to_csv('dagagu_add_district_validation.csv', index=False,  encoding='utf-8-sig')