from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, name, nick):
        self.name = name
        self.nick = nick
        self.fav_games = list()

    def add_favorite(self, game):
        self.fav_games.append(game)
        self.fav_games = sorted(self.fav_games, key=str.lower)

    def all_favorites(self):
        content = f"Name: {self.name}"
        content += "\nFavorite games:"
        if len(self.fav_games) > 0:
            for game in self.fav_games:
                content += f"\n:video_game: {game}"
        return content

    def card(self):
        print(Panel(f"{self.all_favorites()}", title=f"Player: <{self.nick}>"))


gamer1 = Gamer("Sheldon Cooper", "Sheldor")
gamer1.add_favorite("Halo 3")
gamer1.add_favorite("Donkey Kong")
gamer1.add_favorite("Age of Conan")
gamer1.add_favorite("Super Mario 64")

gamer1.card()

gamer2 = Gamer("Howard Wolowitz", "Wolowizard ")
gamer2.add_favorite("World of WarCraft")
gamer2.add_favorite("Dance Dance Revolution")
gamer2.add_favorite("Red Dead Redemption")

gamer2.card()