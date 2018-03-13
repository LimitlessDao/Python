animals = ['rabbits', 'dogs', 'cats']
print(animals)

#Add to the end
animals.append('pelicano')
print(animals)
#add to the start
animal.insert('lion')

#To add a element on a certain position
animals.insert(0, 'dragon')
print(animals)
 
#Remove element from the array
del animals[0]
print(animals)

#Pop an element
popped_animals=animals.pop()
print(animals)
print(popped_animals)

#Pop specific element
print("\n")
print(animals)
animals.remove('dogs')
print("\n")
print(animals)
