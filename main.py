def encrypt():
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    caesar = alpha[(shift ):] + alpha[:(shift)]
   

    def caesar_cipher(text,caesar):
        final = ""
        for i in text:
            for j in alpha:
                if i.lower() == j:
                    final += caesar[alpha.index(j)]
                    break
        return final


    print(caesar_cipher(text, caesar))

encrypt()
