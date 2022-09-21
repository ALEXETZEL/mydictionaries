person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

print(person['children'][1])

print(person["pets"]["cat"])


for x in person['children']:
    print(x)

for y in person['pets']:
    print(person['pets'][y])

