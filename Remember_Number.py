import json

#Load the username, if it has been stored previously.
# Otherwise, promt for the username and store it.

def get_stored_Fav_Number():
 	"""Get stored Favorite Number if available."""
 	filename = 'Fav_Number.json'
 	try:
 		with open(filename) as f_obj:
 			Fav_Number = json.load(f_obj)
 	except FileNotFoundError:
 		return None
 	else:
 		return Fav_Number

def get_new_Fav_Number():
	"""Promt for a new username"""
	Fav_Number = input("What is your favorite number? ")
	filename = 'Fav_Number.json'
	with open(filename,'w') as f_obj:
		json.dump(Fav_Number,f_obj)
	return Fav_Number

def greet_user():
	"""Get the fav number"""
	Fav_Number = get_stored_Fav_Number()
	if Fav_Number:
		print("I know what your favorite number is! It's " + Fav_Number + "!")
	else:
		Fav_Number = get_new_Fav_Number()
		print("I'll remember what your favorite number next time you come back!")

greet_user()	
