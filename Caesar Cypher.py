def caesar_encrypt(realText, step):
        result = ""
        for i in range(len(realText)):
                char = realText[i]
                if (char.isupper()):
#65 and 97 are the number of characters of lower and upper case letters in ascii#
                        result += chr((ord(char) + step - 65) % 26 + 65)
      
                else: result += chr((ord(char) + step - 97) % 26 + 97)
        return result


    
