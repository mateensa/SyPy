#Given a string of length one, return an integer representing
# the Unicode code point of the character when the argument is a unicode object,
# or the value of the byte when the argument is an 8-bit string

li = [chr(i) for i in range(ord('a'),ord('z')+1)];
print(li)

print([chr(i) for i in range(ord('0'), ord('9'))])
print([chr(i) for i in range(ord('0'), ord('10'))]) #Throws error since 10 is not string length  of 1

# if token in [chr(range(ord('a'), ord('z')+1))] or [chr(range('0'), range('9'))]: