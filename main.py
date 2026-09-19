def menu(a):
    if a == 1:
        encrypt()

    elif a == 2:
        shift = int(input("Enter the shift value: "))
        text = input("Enter the text to decrypt: ")
        print(decrypt(shift,text))

    elif a==3:
        print(bruteforce())

    else:
        print("unknown")
        
def encrypt():
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    caesar = alpha[(shift ):] + alpha[:(shift)] #alpha[start:stop:step]
   

    def caesar_cipher(text,caesar):
        final = ""
        for i in text:
            for j in alpha:
                if i == j:
                    final += caesar[alpha.index(j)]
                    break
                elif i.isupper() and i.lower() == j:
                    final += caesar[alpha.index(j)].upper()
                    break
                if i not in caesar:
                    final += i
                    break
        return final


    print(caesar_cipher(text, caesar))

def decrypt(shift,text):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    caesar = alpha[(shift ):] + alpha[:(shift)] 
    final=''
    for i in text:
        for j in caesar:
            if i == j:
                final += alpha[caesar.index(j)]
                break
            elif i.isupper() and i.lower() == j:
                final += alpha[caesar.index(j)].upper()
                break
            if i not in alpha:
                final += i
                break
    return final

def bruteforce():
    a = input("enter to decrypt:3")
    for i in range(1,27):
        print(i,decrypt(i,a))

a = input("Enter the choice:")
while True:
    if int(a) == 0:
        break
    menu(int(a))
    a = input("Enter the choice:")
