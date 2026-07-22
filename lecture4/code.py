input_string = input('Enter a string :')
modiffied_string = ""
vowels = "aeiouAEIOU"
for char in input_string :
    upper_char = char.upper()
    if upper_char in vowels :
        modiffied_string += "*"
    else:
        modiffied_string += upper_char
print("Modified string :", modiffied_string)