from ex036_payment import *

def main():
    try:
        complete_purchase(Pix(), 8500)
        complete_purchase(BankSlip(), 8500)
        complete_purchase(CreditCard(), 0)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()

