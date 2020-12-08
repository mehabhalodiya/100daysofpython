def cipher():
    ans_start = input("Do you want to start? (YES/NO): ")
    ans_start = ans_start.upper()
    while(ans_start in 'YES'):
        print("What do you prefer to do?")
        ans =  input("Press E to Encrypt and D to Decrypt: ")
        ans = ans.upper()

        if(ans=='E'):
            user_input = input("Enter the text you want to Encrypt: ")
            inlet = 'abcdefghijklmnopqrstuvwxyz1234567890'
            outlet ='4567890abcdefghijklmnopqrstuvwxyz123'
            encryption = ''
            encryption = encryption.maketrans(inlet,outlet)
            print("Decrypted code is:")
            print(user_input.translate(encryption))


        elif(ans=='D'):
            user_input = input("Enter the text you want to Decrypt: ")
            inlet ='4567890abcdefghijklmnopqrstuvwxyz123'
            outlet = 'abcdefghijklmnopqrstuvwxyz1234567890'
            decryption = ''
            decryption = decryption.maketrans(inlet,outlet)
            print("Encrypted code is:")
            print(user_input.translate(decryption))

        else:
            print("Please enter 'E' to Encrypt or 'D' to Decrypt.")
        ans_start = input("Do you want to do it again? ")
        ans_start = ans_start.upper()

    while (ans_start in 'NO'):
        print("Thank You!")
        break

def main():
    cipher()

if __name__ == '__main__':
    main()
