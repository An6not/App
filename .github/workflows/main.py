from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from datetime import datetime

class Desktop(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Фон рабочего стола
        with self.canvas.before:
            Color(0.1, 0.1, 0.2, 1) # Темно-синий
            self.rect = Rectangle(size=(2000, 2000), pos=(0,0))

        # Виджет часов
        self.time_label = Label(
            text=datetime.now().strftime("%H:%M:%S"),
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'top': 0.95, 'right': 0.95},
            font_size='20sp'
        )
        self.add_widget(self.time_label)

        # Иконка "Терминал"
        self.term_btn = Button(
            text="Terminal",
            size_hint=(None, None),
            size=(100, 100),
            pos=(50, 500),
            background_color=(0, 0.7, 0, 1)
        )
        self.term_btn.bind(on_release=self.open_terminal)
        self.add_widget(self.term_btn)

        # Окно терминала (скрыто по умолчанию)
        self.terminal_window = BoxLayout(
            orientation='vertical',
            size_hint=(0.8, 0.5),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            opacity=0
        )
        
        self.term_input = TextInput(
            multiline=False, 
            background_color=(0,0,0,1), 
            foreground_color=(0,1,0,1),
            font_name='Roboto' # В реальном APK можно добавить моноширинный шрифт
        )
        self.term_input.bind(on_text_validate=self.run_command)
        
        self.term_output = Label(text="Welcome to AI_OS v1.0\nType 'help' for commands", color=(0,1,0,1))
        
        self.terminal_window.add_widget(self.term_output)
        self.terminal_window.add_widget(self.term_input)
        self.add_widget(self.terminal_window)

    def open_terminal(self, instance):
        self.terminal_window.opacity = 1 if self.terminal_window.opacity == 0 else 0

    def run_command(self, instance):
        cmd = instance.text.lower()
        if cmd == "help":
            res = "Commands: help, time, clear, exit, whoami"
        elif cmd == "time":
            res = f"Current time: {datetime.now().strftime('%H:%M:%S')}"
        elif cmd == "whoami":
            res = "User: Admin (Termux Developer)"
        elif cmd == "exit":
            self.terminal_window.opacity = 0
            res = ""
        elif cmd == "clear":
            res = ""
        else:
            res = f"Error: Command '{cmd}' not found"
        
        self.term_output.text = res
        instance.text = ""

class MobileOSApp(App):
    def build(self):
        return Desktop()

if __name__ == "__main__":
    MobileOSApp().run()
