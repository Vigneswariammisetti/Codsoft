import random
import string
def generate_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters)for _ in range (length))
    return password
def main():
    print("WELCOME TO PASSWORD GENERATOR")
    try:
        length=int(input("enter the desired length of password:"))
        if length<=0:
            print("length should be positive integer.")
            return
        password=generate_password(length)
        print("generated password:",password)
    except ValueError:
        print("INVALID Please Enter a valid Password.")
if __name__=="__main__":
    main()
        
    