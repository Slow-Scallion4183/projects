import random
import string

class password:
	def __init__(self, length, string_method, numbers=True, special_chars=False):
		self.length = length
		self.string_method = string_method
		self.numbers = numbers
		self.special_chars = special_chars

	def generate_intricate(self, iterations):
		if self.string_method == 'upper':
			stringMethod = string.ascii_uppercase
		elif self.string_method == 'lower':
			stringMethod = string.ascii_lowercase
		elif self.string_method == 'both':
			stringMethod = string.ascii_letters

		if self.numbers:
			stringNumbers = string.digits
		elif self.numbers:
			stringNumbers = ''

		if self.special_chars == True:
			stringSpecial = string.punctuation
		elif self.special_chars == False:
			stringSpecial = ''

		characters = stringMethod + stringNumbers + stringSpecial
		for p in range(iterations):
			output_password = ''
			for c in range(self.length):
				output_password += random.choice(characters)
			print(output_password)

# Test

password1 = password(20, 'both', True, True) # password length = 20
password1.generate_intricate(3) # generate a memeorable password (containing words and numbers) 3 times
