from functions import PasswordManager
import getpass
import time

def main():
    pm = PasswordManager()

    print("""Ja's Password Manager!
    1) Create New Key
    2) Load Key
    3) Create New Password File
    4) Load Password File
    5) Add Password
    6) Get Password
    7) View All Passwords
    q) Quit
    """)

    done = False
    while not done:
        choice = input("Enter Choice: ")
        if choice == "1":
            path = input("Enter Path (ex. key.key): ")
            pm.build_key(path)
            print("{} now has an active key!")

        elif choice == "2":
            path = input("Enter Path (ex. key.key): ")
            pm.load_key(path)
            print('{} has been loaded as key')
            
        elif choice == "3":
            path = input("Enter Path (ex. pass.pass): ")
            pm.create_password_file(path)
            print("{} has been created as password file")

        elif choice == "4":
            path = input("Enter Path (ex. pass.pass): ")
            pm.load_password_file(path)
            print("{} has been loaded as password file".format(path))

        elif choice == "5":
            site = input("Enter Site: ")
            password = getpass.getpass("Enter Password: ")
            pm.add_password(site, password)

        elif choice == "6":
            site = input("Enter Site: ")
            print("Your Password for {} is: {}".format(site, pm.get_pass(site)))

        elif choice == "q":
            print("Goodbye!\nProgram will shut down in")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            quit()

        else: print("Invalid Input")

if __name__=="__main__":
    main()        