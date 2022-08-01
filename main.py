import kivy
kivy.require('2.1.0') 

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.scatter import Scatter
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock

class Cat:
    def __init__(self, frame, x=0):
        self.max = 5
        self.frame = frame
        self.image = Image(source=f'cat_walking/frame_{self.frame}_delay-0.1s.png')
        self.speed = 30
        self.leave = False
        self.image.pos[0] = x
        

        self.bounary = Window.size[0]/2

    def change_speed(self, val):

        if self.speed == 0 and val < 0:
            return

        if self.speed > 0:
            self.speed = abs(self.speed) + val
        else:
            self.speed = -(abs(self.speed) + val)


    def __add__(self, x):
        self.frame += x
        if self.frame > self.max:
            self.frame = self.frame % self.max

        if not self.leave:
            if abs(self.image.pos[0]) > self.bounary:
                if self.image.pos[0] > 0:
                    self.speed = abs(self.speed)
                else:
                    self.speed = -abs(self.speed)


        if self.speed < 0:
            self.image.source = f'cat_walking/frame_{self.frame}_delay-0.1s_f.png'
        else:
            self.image.source = f'cat_walking/frame_{self.frame}_delay-0.1s.png'

        self.image.pos[0] -= self.speed


class MyApp(App):

    def build(self):

        self.cato = Cat(0)
        self.cato2 = Cat(0, 100)
        
        self.label = Label(text='Hello world ')
        self.input = TextInput(font_size = 50, size_hint_y = None, height = 100)
        self.input.bind(text=self.on_text)

        self.box = BoxLayout(orientation ='vertical')
        self.box.add_widget(self.label)
        self.box.add_widget(self.input)
        # textinput.bind(text=on_text)
        
        self.box.add_widget(self.cato.image)
        self.box.add_widget(self.cato2.image)
        Clock.schedule_interval(self.walk, .1)
        return self.box

    def on_text(self, _, val):
        if val == "bye":
            self.cato.leave = True
        elif val == "get back":
            self.cato.leave = False 

        elif val == "fast":
            self.cato.change_speed(10)
        elif val == "slow":
            self.cato.change_speed(-10)



    def walk(self, _):
        self.cato + 1
        self.cato2 + 1
        self.label.text = str(self.cato2.image.pos)
        
    
if __name__ == '__main__':
    MyApp().run()

