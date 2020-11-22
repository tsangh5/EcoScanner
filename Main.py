from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
import random
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.button import Button
from kivy.config import Config
from pyzbar.pyzbar import decode
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty
Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '780')
import cv2
import os
from kivy.core.window import Window
from kivy.core.text import LabelBase
Window.clearcolor = (1, 1, 1, 1)

LabelBase.register(name='Aller',
fn_regular='Aller_Rg.ttf')

class WindowManager(ScreenManager):
    pass


class CameraWindow(Screen):
    def __init__(self, **kwargs):
        super(CameraWindow, self).__init__(**kwargs)
        self.name = 'Camera'
        self.capture = cv2.VideoCapture(0)
        self.img1=Image(size_hint=(1, 1))
        self.btn = Button(background_normal='pic1.png', background_down='pic1.png', on_release=self.take, size_hint=(.3, .2), pos_hint={'x': 0.3, 'y': 0})
        Clock.schedule_interval(self.update, 1.0/33.0)
        layout = FloatLayout(size=(800, 450), pos_hint= {'center_y': 0.5, 'center_x': 0.5})
        layout.add_widget(self.img1)
        layout.add_widget(self.btn)
        self.add_widget(layout)
    def take(self, frame):
        os.chdir('C:/Users/tsangh5/Hackathon/images')
        num = len([name for name in os.listdir('.') if os.path.isfile(name)])
        ret, frame = self.capture.read()
        cv2.imwrite(f'{num}.png', frame)
    def update(self, dt):
        os.chdir('C:/Users/tsangh5/Hackathon/images')
        ret, frame = self.capture.read()
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img1.texture = texture1
        for img in os.listdir('C:/Users/tsangh5/Hackathon/images'):
            if os.path.isfile(img):
                self.analyse(img)
    def analyse(self, img):
        photo = cv2.imread(img)
        yow= decode(photo)
        if yow != []:
            os.chdir('C:/Users/tsangh5/Hackathon')
            f = open('point.txt')
            content = f.readlines()[0]
            result = str(10 + int(content))
            f = open('point.txt', 'r+')
            f.truncate(0)
            new = open('point.txt', 'w')
            new.write(result)
        print(yow)


class MainWindow(Screen):
     def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)  
        self.name = 'main'



class CouponWindow(Screen):
    f = open('coupons.txt', 'r')
    content = f.read()
    text_variable_2 = StringProperty(content)
    def __init__(self, **kwargs):
        super(CouponWindow, self).__init__(**kwargs)



class GameWindow(Screen):
    pass

class StoreWindow(Screen):
    f = open('point.txt', 'r')
    content = f.read()
    text_variable_1 = StringProperty(content)
    hundred = StringProperty('100')
    twohundred = StringProperty('200')
    fivehundred =StringProperty('500')
    thousand = StringProperty('100')
    number = StringProperty(None)
    def __init__(self, **kwargs):
        super(StoreWindow, self).__init__(**kwargs)
        # self.number = int(number)
        # self.coupon = 0
        def transaction(self):
            pass
        #     if int(text_variable_1) < self.number:
        #         pass
        #     else:
        #         f = open('point.txt')
        #         content = f.readlines()
        #         result = str(int(content)- self.number)
        #         f = open('point.txt', 'r+')
        #         f.tuncate(0)
        #         new = open('point.txt', 'w')
        #         new.write(result)
        #         self.coupon = int(self.coupon)
        #         f = open('couponss.txt')
        #         content = f.readlines()
        #         result = str(int(content)+ self.coupons)
        #         f = open('point.txt', 'r+')
        #         f.tuncate(0)
        #         new = open('point.txt', 'w')
        #         new.write(result)
                
                
        


kv = Builder.load_file("My.kv")
red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]


class MainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MainApp().run()
