name = "Mateen";
age = 30;

print("myname is %s and age is %d"  %(name, age));
formatted = 'myname is {} age is {}'.format(name, age);
print(formatted);


#Formatting ascii chars like ä

name= "Mäteen"
print(name)
print("name is %s"  %(name));

class Data:
    def strin(self):
        return "str";
    def strin(self):
        return "ästr";

print('%s %r' % (Data(), Data()))

print('{0!s} {0!r}'.format(Data()))

wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
    letterlist.append(":---->")
print(letterlist)
