from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
import random
# vijedga   = text button kiradi


class WidgetsActionExample(GridLayout):
    counter_enable = BooleanProperty(False)
    text = StringProperty("A")
    toggle_text = StringProperty("Off")
  
    random_text = StringProperty("")
    # raqam = "A"

    # def button_click_counter(self):
    # if self.counter_enable:
    raqam = ['v', 'k', 'n']
    # self.raqam = "B"
    # self.text=str(self.raqam)


     

    def func(self):   
        if self.counter_enable:
            randoms = random.choice(self.raqam)
            if randoms == "n":
                self.random_text = "n"
                self.text = randoms
            else:
                self.text = randoms
            # self.text = randoms

    def button_toggle_counter(self, holat):
        if holat.state == "down":
            self.toggle_text = "On"
            self.counter_enable = True
        else:
            self.toggle_text = "Off"
            self.counter_enable = False


class BoxlayoutTurlari(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = 'lr-bt'


class StackLayoutturlari(StackLayout):
    pass
    # def __init__(self,**kwargs):
    #     super().__init__(**kwargs)
    #     for i in range(0,300):
    #         button1 =Button(text=str(i+1),size_hint=(None,None),size=('40dp','40dp'))
    #         self.add_widget(button1)


class AnchorLayoutturlari(AnchorLayout):
    pass


class Gridlayoutturlari(GridLayout):
    pass


class Widjetturlari(Widget):
    pass


class FirstApp(App):
    pass


FirstApp().run()
