from caesar import caesar_cipher

n = 3
text = input("Input Plain Text : ")
print("Shift Pattern : " + str(n))
print("Cipher : " + caesar_cipher(text, n))