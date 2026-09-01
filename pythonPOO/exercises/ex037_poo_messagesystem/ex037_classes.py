from abc import ABC

from pygments import style
from rich import print, panel
from rich.panel import Panel
import emoji
# :warning: yeallow
# :prohibited: red

class Message:
    style = "white on black"
    title = f":cloud: Notice :cloud:"

    def show(self, user_input):
        print(Panel(f"{user_input}", title=self.title, style=self.style))

class Warning:
    style = "black on yellow"
    title = f":warning: Warning :warning:"

    def show(self, user_input):
        print(Panel(f"{user_input}", title=self.title, style=self.style))

class Error:
    style = "black on red"
    title = f":prohibited: Error prohibited:"

    def show(self, user_input):
        print(Panel(f"{user_input}", title=self.title, style=self.style))

def show_message(type, message):
    type.show(message)




