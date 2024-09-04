max_char = input ("Enter two space-separated characters:")
char1, char2 = max_char.split()
maximum_char =  max (char1, char2)
asciiVal_1 = ord(char1)
asciiVal_2 = ord(char2)
print ("------------------------------")
print ("The character with the greater value is: ", maximum_char)
print ("------------------------------")

print ("This part is optional to include.")
print("Showing ASCII values")

print (f"1 :  {asciiVal_1}")
print (f"a :  {asciiVal_2}")
