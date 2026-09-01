from ex035_classes import *

def main():
    d = Doc("class_summary", 250_000)
    p = Pdf("contract", 1_300_000)
    d.open_file()
    p.open_file()
    print(d.complete_name)


if __name__ == "__main__":
    main()