import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, StringProperty

import main


class CustomWidget(Widget):
    link_address_text_input = StringProperty('')


class MainApp(App):
    def build(self):

        box = BoxLayout(orientation = 'vertical')

        input1 = TextInput(text ="Paste the link.....", multiline = "False")
        button = Button(text ="Download")
        input1.bind(on_text_validate=on_enter)

        box.add_widget(input1, button)

        return box

    def on_enter(instance, value):
        print('User pressed enter in', instance)



if __name__ == "__main__":
    app = MainApp()
    app.run()

