
people = [
	{"name":"Harry", "house":"Gryffindor"},
	{"name":"Cho", "house":"Ravenclaw"},
	{"name":"Draco", "house":"Stytherin"}
]

people.sort(key=lambda person: person["name"])

print(people)
