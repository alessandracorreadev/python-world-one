from rich import print
from rich.panel import Panel


class Tv:
    volmin = 1
    volmax = 5
    chmin = 1
    chmax = 5

    def __init__(self, vol=2, ch=1):
        self.volnow = vol
        self.chnow = ch
        self.tv_on = False

    def toggle(self):
        self.tv_on = not self.tv_on

    def volume_up(self):
        if self.tv_on:
            if self.volnow < Tv.volmax:
                self.volnow += 1

    def volume_down(self):
        if self.tv_on:
            if self.volnow > Tv.volmin:
                self.volnow -= 1

    def next_channel(self):
        if self.tv_on:
            if self.chnow < Tv.chmax:
                self.chnow += 1
            else:
                self.chnow = Tv.chmin

    def previous_channel(self):
        if self.tv_on:
            if self.chnow > Tv.chmin:
                self.chnow -= 1
            else:
                self.chnow = Tv.chmax

    def display(self):
        if not self.tv_on:
            content = ":prohibited: TV is off\n"
        else:
            content = "CHANEL = "
            for ch in range(Tv.chmin, Tv.chmax+1):
                if ch == self.chnow:
                    content += f"[white on yellow] {ch} [/]"
                else:
                    content += f" {ch} "

            content += "\nVOLUME = "

            for vol in range(Tv.volmin, Tv.volmax+1):
                if vol <= self.volnow:
                    content += f"[white on blue] [/]"
                else:
                    content += f"[white on yellow] [/]"

        print(Panel(f"{content}", title="[ TV ]", width=40))


class Remote:
    def __init__(self, tv: Tv):
        self.tv = tv

    def remote_button(self, button):
        match button:
            case "@":
                self.tv.toggle()
            case ">":
                self.tv.next_channel()
            case "<":
                self.tv.previous_channel()
            case "+":
                self.tv.volume_up()
            case "-":
                self.tv.volume_down()



tv1 = Tv()
remote1 = Remote(tv1)
while True:
    tv1.display()
    btn = input(f"< CH{tv1.chnow} >  - VOL{tv1.volnow} + ")
    remote1.remote_button(btn)
    print("\n"*10)
