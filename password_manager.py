from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''
        
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

password = input("Enter the master password: ") 
key = load_key() + password.encode()
fer = Fernet(key)
      

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = (line.rstrip())            
            page, user, passw = data.split("|")
            print("Site:", page, "Username:", user, "Password:", fer.decrypt(passw.encode()).decode())
            

def add():
    site = input("Enter the Webpage: ")
    name = input("Enter the username: ")
    pwd = input("Enter the password: ")
    
    with open('password.txt', 'a') as f:
        f.write(site + "|" + name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Do you want to add a password or view them?(add/view) and q to quit: ").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        quit()    
    else:
        print("Invalid mode.")
        continue

