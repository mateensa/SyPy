# Dictionary is collection of key value pairs of items like Hashmap and hashtable in java likewise
# Keys cannot be duplicated, if duplcated then it will refer latest added entry

di = dict({1:"one", 2:"two", 3:"three",4:"four"});
print(di);

#Another way of delcaring dictionary
d = {1:"one", 2:"two", 3:"three",4:"four"}
print(d)

capitals = {"Karnataka":"Bangalore","Telengana":"Hyderabad"}
print(capitals)
capitals["Maharastra"] = "Mumbai";
print(capitals)
capitals["NewDehli"] = "Dehli"
capitals["TamilNadu"] = "Chennai"
capitals["TamilNadu"] = "Chennai2"
capitals["TamilNadu2"] = "Chennai"
for item in capitals:
    print(item, " is state and capital is ", capitals[item])

print(capitals.keys())
print(capitals.values())
print(list(capitals.keys()))
print(list(capitals.values()))
print(list(capitals))
print(capitals.get("Karnataka"))
print(capitals.get("Kerala", "Capital not defined"))

# Dictionary Comprehension
d = {j:None for j in range(10)}
print(d)