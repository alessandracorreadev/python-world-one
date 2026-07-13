from ex027_rpg import *

def main():
    c1 = Warrior("Arthur", 1500)
    c2 = Wizard("Morgana", 1000)
    c3 = Warrior("Lancelot", 1000)

    c1.attack(c2)
    c3.attack(c1)
    c2.attack(c3)
    c2.attack(c1)
    c3.attack(c2)
    c3.attack(c2)
    c3.attack(c2)
    c3.attack(c2)
    c3.attack(c2)
    c3.attack(c2)
    c3.attack(c2)
    c3.attack(c2)
    c3.attack(c2)
    c3.attack(c2)
    c3.attack(c2)
    c3.attack(c2)
    c3.attack(c2)
    c3.attack(c2)

    c1.heal()
    c1.heal()
    c1.heal()
    c2.heal()


if __name__ == "__main__":
    main()

