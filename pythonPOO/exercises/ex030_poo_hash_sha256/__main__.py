from pythonPOO.exercises.ex030_poo_hash_sha256.classcredential import Credential

def main():
    c = Credential()
    c.password = str(input('Enter the password: '))
    print(c.password)

    c.validate('Password')
    c.validate('helloworld')

if __name__ == "__main__":
    main()
