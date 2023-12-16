import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pathlib

# 데이터 경로 설정
data_dir = pathlib.Path("C:/Users/koung/kicpython/hansik/kfood_new/data/learning_rgb1/image/")

# 이미지 크기 및 배치 크기 설정
img_height = 100
img_width = 100
batch_size = 32

# 데이터셋 생성을 위한 ImageDataGenerator 설정
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

# 데이터 불러오기
train_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=True)

# 모델 생성(더 깊은 신경망 아키텍처 사용)
model = keras.Sequential([
    keras.layers.Conv2D(32, 3, padding='same', activation='relu', input_shape=(img_height, img_width, 3)),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(128, 3, padding='same', activation='relu'),  # 추가 합성곱 층
    keras.layers.MaxPooling2D(),
    keras.layers.Dropout(0.3),  # 드롭아웃을 더 많이 사용
    keras.layers.Flatten(),
    keras.layers.Dense(256, activation='relu'),  # 더 많은 뉴런
    keras.layers.Dense(len(train_generator.class_indices), activation='softmax')
])

# 정규화 기법 및 다른 최적화 알고리즘 사용
model.compile(optimizer='adam',
              loss='categorical_crossentropy',  # 다중 클래스 분류 문제의 손실 함수
              metrics=['accuracy'])

epochs = 30
history = model.fit(train_generator, epochs=epochs)

# 앙상블 학습 (여러 다른 모델을 조합)
# 같은 모델을 여러 번 학습하여 간단한 앙상블 시도
num_ensemble_models = 5
ensemble_models = []

for _ in range(num_ensemble_models):
    model = keras.Sequential([
        # 모델 아키텍처는 동일하게 사용
        keras.layers.Conv2D(32, 3, padding='same', activation='relu', input_shape=(img_height, img_width, 3)),
        keras.layers.MaxPooling2D(),
        keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
        keras.layers.MaxPooling2D(),
        keras.layers.Conv2D(128, 3, padding='same', activation='relu'),
        keras.layers.MaxPooling2D(),
        keras.layers.Dropout(0.3),
        keras.layers.Flatten(),
        keras.layers.Dense(256, activation='relu'),
        keras.layers.Dense(len(train_generator.class_indices), activation='softmax')
    ])
    
    model.compile(optimizer='adam',
              loss='categorical_crossentropy',  # 다중 클래스 분류 문제의 손실 함수
              metrics=['accuracy'])
    
    model.fit(train_generator, epochs=epochs)
    ensemble_models.append(model)

# 각 모델의 예측을 평균내어 앙상블 결과 생성
ensemble_predictions = []

for model in ensemble_models:
    predictions = model.predict(train_generator)
    ensemble_predictions.append(predictions)

ensemble_predictions = tf.stack(ensemble_predictions)  # 예측을 스택으로 변환
ensemble_predictions = tf.reduce_mean(ensemble_predictions, axis=0)  # 예측 평균

# 모델 저장 (앙상블 모델을 저장하려면 적절한 방식으로 저장)
model.save("C:/Users/koung/kicpython/hansik/kfood_new/models/model.h5")