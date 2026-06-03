from rich import print
from time import sleep


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        self.counter = 1
        print((f"[blue]You have just opened the book [red]'{self.title}'[/], which "
                f"has [green]{self.pages} pages[/] in total. You are now on [yellow]page {self.counter}[/][/]."))
        sleep(1.5)

    def skip_pages(self, value):
        count_pages = 0
        for number in range(0, value):
            if not self.end_book():
                count_pages += 1
                self.counter += 1
                print(f"Page {self.counter} :arrow_forward: ", end='')
                sleep(1)

        print(f"[blue]You skip {count_pages} pages and now you are on [yellow]page {self.counter}[/][/].")

        if self.end_book():
            print(f"[red]You have reached the end of the book {self.title}.[/]")

    def end_book(self) -> bool:
        return True if self.counter == self.pages else False


book1 = Book("10 Things I Learned in Python", 20)

book1.skip_pages(5)
book1.skip_pages(10)
book1.skip_pages(100)
book1.skip_pages(5)

# book2 = Book("It Ends With Us", 366)