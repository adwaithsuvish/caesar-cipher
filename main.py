ceasar = 'efghijklmnopqrstuvwxyzabcd'
alpha = 'abcdefghijklmnopqrstuvwxyz'
text = input("Enter the text to encrypt: ")
final = ""
for i in text:
    for j in alpha:
        if i.lower() == j:
            final += ceasar[alpha.index(j)]
            break
print(final)