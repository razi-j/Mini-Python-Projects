from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):
        self.key = None
        self.pw_File = None
        self.pw_Dict = {}

    def build_key(self, path): #generates the key that fernet will use for encryption and decryption
        self.key = Fernet.generate_key()
        with open(path, 'wb') as keyfile:
            keyfile.write(self.key)

    def load_key(self, path): #loads a preexisting key file
        with open(path, 'rb') as keyfile:
            self.key = keyfile.read()

    def create_password_file(self, path): #creates and sets a new password file for the password dictionary
        self.pw_File = path

    def load_password_file(self, path): #loads a preexisting password file's dictionary and reads it.
        self.pw_File = path
        with open(path, 'r') as pw_file:
            for line in pw_file:
                site, encryptedPass = line.split('|')
                self.pw_Dict[site] = Fernet(self.key).decrypt(encryptedPass.encode()).decode()

    def add_password(self, site, password):
        self.pw_Dict[site] = password

        if self.pw_File is not None:
            with open(self.pw_File, 'a+') as pw_file:
                encrypted = Fernet(self.key).encrypt(password.encode())
                pw_file.write(site + '|'+ encrypted.decode() +"\n")

    def get_pass(self, site):
        return self.pw_Dict[site]