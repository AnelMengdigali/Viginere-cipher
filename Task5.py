
#Task5: Vigenere cipher
def menu5():

	print("         Welcome to the Vigenere cipher         ")    
	key = input("Choose the encryption key (indicate string): ")
	phrase = input("Please enter your phrase: ")
    
	return key, phrase

def vigenereCipher(key, text):

	vcipher = ''
	count = 0 

	#doing a change of position for each letter using key:
	for letter in text:

		if(count >= len(key)):
			count = 0

		pos = ord(letter.lower()) + (ord(key[count].lower()) - 97)

		if(pos > 122):
			pos -= 26

		vcipher += chr(pos)
		count += 1

	return vcipher

key, content = menu5()
print("The encrypted text: ", vigenereCipher(key, content))