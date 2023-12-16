from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserListView
import cv2
from tensorflow.keras.models import load_model
from kivy.core.text import LabelBase
import tensorflow as tf
from kivy.uix.camera import Camera

# 한글 폰트 등록
LabelBase.register(name='NanumGothic', fn_regular='NanumGothic.ttf')

class FoodRecommendationApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.camera = Camera(resolution=(640, 480), play=True)
        layout.add_widget(self.camera)
        return Builder.load_string()

    def upload_image(self, instance):
        file_chooser = FileChooserListView(path='.', dirselect=True)
        file_chooser.bind(on_submit=self.load_image)
        file_chooser.open()

    def load_image(self, chooser, path, filename):
        image_path = f'{path}/{filename[0]}'
        image = cv2.imread(image_path)  # OpenCV를 사용하여 이미지 로드
        # 이미지를 모델에 전달하여 결과 예측
        # 예측 결과를 self.result_label에 표시

if __name__ == '__main__':
    FoodRecommendationApp().run()
