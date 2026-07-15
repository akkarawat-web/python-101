inchar = input ("Input one charecter:")
if inchar >='A' and inchar <= 'Z':
    print("You in put Upper Case letter" , inchar)
elif inchar >= 'a' and inchar <= 'z':
    print(" You in put lower case leetter" , inchar)
elif inchar >= '0' and inchar <= '9':
    print("You in put Number" , inchar)
else :
    print("It's not a leeter or number." , inchar)