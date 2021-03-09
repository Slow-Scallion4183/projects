import random
import urllib.request
import string

class password:
	def __init__(self, length, string_method, numbers, special_chars):
		self.length = length
		self.string_method = string_method
		self.numbers = numbers

	# def generate_intricate(self, iterations):
	# 	characters = string.ascii_letters + string.digits + string.punctuation
	# 	for p in range(iterations):
	# 		output_password = ''
	# 		for c in range(self.length):
	# 			output_password += random.choice(characters)
	# 		print(output_password)

	def generate(self, iterations):
		characters = string.ascii_letters + string.digits + string.punctuation
		for p in range(iterations):
			output_password = ''
			for c in range(self.length):
				output_password += random.choice(characters)
			print(output_password)





# Test

password1 = password(20) # password length = 20
password1.generate_memorable(3) # generate a memeorable password (containing words and numbers) 3 times