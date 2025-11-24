# leo = {'name': 'Lionel Messi', 'nationality': 'Argentina', 'number': 10}
# cr7 = {'name': 'Cristiano Ronaldo', 'nationality': 'Portugal', 'number': 7}

# zizo = dict(name = 'Zinedine Zidane', nationality = 'France', number = 10)
# pele = dict([('name', 'Edson Arantes Do Nascimento'), ('nationality', 'Brazil'), ('number', 10)])

# print(leo['name'])
# print(cr7['nationality'])

# print(zizo.get('name'))

# person = {'name': 'Lale', 'age': 4}
# person['country'] = 'Iran'

# print(person)
# print(person['country'])

# person = {'name': 'Lale', 'age': 4}
# person['age'] = 5

# print(person)

# person = {'name': 'Lale', 'age': 4, 'country': 'Iran', 'language': 'python'}
# print(person)

# del person['country']
# print(person)

# programming_language = person.pop('language')
# print(person)
# print(programming_language)

# person = {'name': 'Lale', 'age': 4}
# person.clear()
# print(person)

person = {'name': 'Lale', 'age': 4}
person_copy = person.copy()
person_copy['age'] = 5

print(person['age'])