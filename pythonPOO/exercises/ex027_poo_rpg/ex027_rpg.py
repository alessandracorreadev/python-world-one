from abc import ABC, abstractmethod
from random import choice, randint
from rich import print

class Character(ABC):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.skills = list()
        self.maxhp = self.hp

    def attack(self, target, power=100):
        if self.hp > 0 and target.hp > 0:
            print(f"[green]{self.name}[/] attacked [red]{target.name}[/] with>> "
                  f"skill: [blue]{choice(self.skills)}[/] power: {power}.")
            target.take_damage(target, power)
        else:
            print(f"The attack {self.name} -> {target.name} cannot be performed.")
        print("-" * 70)

    def take_damage(self,name, power_damage):
        damage = randint(50, power_damage)
        self.hp -= damage
        if self.hp <= 0:
            print(f"[green]{name.name}[/] is [red]DEAD.[/]")
            self.hp = 0
        else:
            print(f"[green]{name.name}[/] took [red]{damage} damage.[/]", end=' ')
        print(f"[green]{name.name}[/] HP now: {name.hp}.")

    @abstractmethod
    def heal(self):
        pass

class Warrior(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.skills = ["Power Strike", "Crushing Blow", "Furious Charge"]
        self.maxhp = self.hp

    def heal(self):
        if self.hp != 0:
            heal = randint(50, 100)
            if self.hp < self.maxhp:
                self.hp += heal
                print(f"[blue]{self.name}[/] bandaged the wounds and [green]recovered {heal} health[/] points.")
            else:
                print(f"[blue]{self.name}[/] health points [green]is full.[/]")
                self.hp = self.maxhp
        else:
            print(f"You can't heal {self.name}.The character [red]is DEAD.[/]")



class Wizard(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.skills = ["Magic Missile", "Fireball", "Ice Beam"]
        self.maxhp = self.hp

    def heal(self):
        if self.hp != 0:
            if self.hp < self.maxhp:
                heal = randint(50, 100)
                self.hp += heal
                print(f"[blue]{self.name}[/] cast a healing spell and [green]restored {heal} health[/] points.")
            else:
                self.hp = self.maxhp
                print(f"[blue]{self.name}[/] health points [green]is full.[/]")
        else:
            print(f"You can't heal {self.name}.The character [red]is DEAD.[/]")