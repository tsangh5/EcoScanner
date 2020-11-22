from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '800')
import cv2
import os
from pyzbar.pyzbar import decode

class CamApp(App):

    def build(self):
        self.img1=Image(size_hint=(1, 1))
        self.btn = Button(background_normal='pic3.png', background_down='pic3.png', on_release=self.take, size_hint=(.4, .2), pos_hint={'x': 0.35, 'y': 0})
        layout = FloatLayout(size=(800, 450), pos_hint= {'center_y': 0.5, 'center_x': 0.5})
        layout.add_widget(self.img1)
        layout.add_widget(self.btn)
        os.chdir('./images')
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout
    def take(self, frame):
        num = len([name for name in os.listdir('.') if os.path.isfile(name)])
        ret, frame = self.capture.read()
        cv2.imwrite(f'{num}.png', frame)
    def update(self, dt):
        ret, frame = self.capture.read()
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img1.texture = texture1
        for img in os.listdir('.'):
            if os.path.isfile(img):
                self.analyse(img)
    def analyse(self, img):
        photo = cv2.imread(img)
        result = decode(photo)
        print(result)

if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()
