from pythonPOO.exercises.ex037_poo_messagesystem.ex037_classes import *

# :warning: yeallow
# :prohibited: red

def main():
    l = [25, 45, "hello"]
    Message().show(l)
    show_message(Message(), "This is only a MESSAGE test.")
    show_message(Warning(), "This is a WARNING message test.")
    show_message(Error(), "This is a ERROR message test.")


if __name__ == "__main__":
    main()