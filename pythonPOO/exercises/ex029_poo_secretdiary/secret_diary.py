# Diary class that allows a user to write and save messages,
# but only allows reading the stored messages with the correct password.
from rich import print

class Diary:
    def __init__(self, password : str ="P@55w0rd"):
        self.__secrets = list()
        self.__password = password

    def write(self, message : str):
        fmessage = message.strip()
        if type(fmessage) == str and len(fmessage) > 0:
            self.__secrets.append(message)

    def read(self, password = None):
        if password == self.__password:
            for secret in self.__secrets:
                print(f"- {secret}")
        else:
           raise PermissionError("Wrong password!")

    @property
    def password(self):
        print("[red]You can't see the password.[/]")



# message = "text"
# if type(message) == str:
#    print(message)