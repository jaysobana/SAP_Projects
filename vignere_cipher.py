def calculate_shifts(letters):
    for j in range(97, 123):
        if chr(j) == letters:
           return j % 97

def encrypt_letter(letter,key):
    if not letter.isalpha():
        return letter
    for j in range(0, 25):
        if chr(j+97) == letter:
            var = ((j+key) % 26)
            ##print(letter,j,key,chr(var+97))
            return(chr(var+97))
    
def encrypt_text(var_letter,var_keyword):
    
    list_letter = []
    for i in range(0, len(var_letter)):
        ##if var_letter[i].isalpha():
        list_letter.append(encrypt_letter(var_letter[i].lower(),calculate_shifts(var_keyword[i%len(var_keyword)].lower())))
        ##else:
            ##list_letter.append(var_letter[i])
                
    return(''.join(list_letter))


var_letter = input("Which text should be encrypted:")
var_keyword = input("Which keyword should be used?")

print(encrypt_text(var_letter.lower(),var_keyword.lower()))
