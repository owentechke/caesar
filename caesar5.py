def decrypt_caesar(string_to_decrypt):
    '''
    Decrypt text that has been encrypted using Caesar's Cipher.
    Function tries different offsets and uses letter frequency to determine which version is most likely to be English
    '''
    string_to_decrypt = string_to_decrypt.lower()
    highest_score = 0
    string_score = 0
    newstring=""
    offset_string = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcde"

    letter_scores = {
      "a": 43.31,"b": 10.56,"c": 23.13,"d": 17.25, "e": 56.88,
      "f": 9.24,"g": 12.59,"h": 15.31,"i": 38.45,"j": 1.00,
      "k": 5.61,"l": 27.98,"m": 15.36, "n": 33.92,"o": 36.51,
      "p": 16.14,"q": 1.00,"r": 38.64,"s": 29.23,"t": 35.43,
      "u": 18.51, "v": 5.13,"w": 6.57,"x": 1.48,"y": 9.06,"z": 1.39 }

    for i in range(26):#Try different offsets
        
        for my_char in string_to_decrypt:           #Offset each character
            if my_char not in offset_string:        #Take non-alphabetic characters as they are
                newstring += my_char
                continue
            
            usual = offset_string.index(my_char)    #Get usual position
            newchar = offset_string[usual+i]        #get new position and therefore new character
            letter_score = letter_scores[newchar]   #Get letter score of the new character 
            string_score += letter_score            #Add to score
            newstring += newchar                    #Add to decrypted string 

        if string_score > highest_score:
            my_answer = newstring
            highest_score = string_score
            offset_used = i

        print(newstring," ",string_score)
        
        #Reset for next iteration
        string_score = 0
        newstring=""

    print("\nAnswer: ", my_answer)
    print("Score: ", highest_score)
    print("Offset: ", offset_used,"\n" )

def decrypt_caesar_w_offset(string_to_decrypt, offset):
    '''
    Decrypt text that has been encrypted using Caesar's Cipher.
    Function uses provided offset
    Offset is expected to be max of 25
    '''
    import string
    string_to_decrypt = string_to_decrypt.lower()
    newstring=""
    offset_string = string.ascii_lowercase[::-1]*2 #create alphabet in reverse x 2
   
    for my_char in string_to_decrypt:           #Offset each character
        if my_char not in offset_string:        #Take non-alphabetic characters as they are
            newstring += my_char
            continue
        
        usual = offset_string.index(my_char)    #Get usual position
        newchar = offset_string[usual+offset]   #get new position and therefore new character
        newstring += newchar                    #Add to decrypted string 

    print("--"*5,"Decrypted with offset\n", newstring,"--"*5,)

def encrypt_caesar(string_to_encrypt, offset):
    '''
    Encrypts text using Caesar's Cipher and provided offset
    Offset is expected to be max of 25
    '''
    string_to_encrypt = string_to_encrypt.lower()
    standard_alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabc"
    encrypted_string = ""
    
    for my_char in string_to_encrypt:
        if my_char not in standard_alphabet:
            encrypted_string += my_char
            continue
        
        usual_pos = standard_alphabet.index(my_char)
        new_char = standard_alphabet[usual_pos + offset]
        encrypted_string += new_char

    return encrypted_string


mystring = '''MHILY LZA ZBHL XBPZXBL MVYABUHL HWWPBZ JSHBKPBZ JHLJBZ KPJABT HYJHUBT LZA ULBAYVU'''
mystring = "cqn jupxarcqv carnb cx orwm cqn arpqc tnh jwm mnlahycb cqn bcarwp kh pdnbbrwp."
mystring = "DWWDFN DW GDZQ"

plain_string = "The Caesar Cipher is a monoalphabetic rotation cipher used by Gaius Julius Caesar."
plain_string = "pda ywaown yeldan eo w ikjkwhldwxapey nkpwpekj yeldan qoaz xu cweqo fqheqo ywaown."
plain_string = '''
The quick brown fox jumped over the lazy dog.
The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.

Exponents, like ² and ¾ are also considered to be numeric values.

"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.

'''

mystring = encrypt_caesar(plain_string, 7)

print(mystring+"\n")

decrypt_caesar(mystring)

decrypt_caesar_w_offset(mystring, 7)
