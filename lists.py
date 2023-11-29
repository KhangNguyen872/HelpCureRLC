people = ['Mario', 'Luigi']
print(people)

people.append('Bowser')
print(people)

copy_of_people = people.copy()
print(copy_of_people)
copy_of_people.remove('Mario')
print(copy_of_people)

countries = ['India','China','USA','Slovakia']
more_countries = ['Serbia','Myanmar','South Africa','Zambia']
print(countries)

countries.extend(more_countries)

print(countries)

countries.remove('Serbia')
countries.remove('Myanmar')
countries.remove('South Africa')
countries.remove('Zambia')
print(countries)

some_more_countries = ['Japan','Australia']

countries.extend(some_more_countries)
print(countries)

print(countries.index('Slovakia'))

print(countries)

countries.insert(2, 'Tanzania')
print(countries)

countries.remove('Japan')
countries.remove('Australia')
print(countries)

countries.extend(people)
print(countries)

countries.pop(1)
countries.pop(5)
print(countries)