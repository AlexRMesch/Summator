from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        main = BoxLayout(orientation="vertical")
        self.n1 = TextInput(multiline=False)
        main.add_widget(self.n1)
        self.n2 = TextInput(multiline=False)
        main.add_widget(self.n2)
        bt = Button(text="сложить")
        bt.bind(on_press=self.sm)
        main.add_widget(bt)
        self.lab = Label()
        main.add_widget(self.lab)
        return main

    def sm(self, a):
        self.lab.text = str(float(self.n1.text) + float(self.n2.text))

app = MainApp()
app.run()