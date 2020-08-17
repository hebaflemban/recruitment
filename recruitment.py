def main():

	print("Welcome to the special recruitment program,\n please answer the following questions:")
	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	cv ={}

	cv['name'] = input("What's your name? ")
	cv['age'] = input("How old are you? ")
	cv['experience'] = input("How many years of experience do you have? ")
	cv['skills'] = []

	x=1
	for i in skills:
		print ("%d.%s" %(x, i))
		x=x+1

	index1 = input("Choose a skill from above by entering its number: ")
	index2 = input("Choose another skill from above by entering its number: ")

	if (int(index1) > len(skills) )or (int(index2) > len(skills)):
		print("Sorry %s, you got rejected, number entered is not valid" %(cv['name']))
	else:
		pass

	cv['skills'].append( skills[int(index1)-1] )
	cv['skills'].append( skills[int(index2)-1] )

	if int(cv['age'])>24 and int(cv['age'])<41 and int(cv['experience'])>5:
		if "Python" in cv['skills']:
			print ("Congratulations %s, you got accepted!" %(cv['name']))
		else:
			print("Sorry %s, you got rejected" %(cv['name']))
	else:
		print("Sorry %s, you got rejected" %(cv['name']))

	print(cv)
if __name__ == '__main__':
	main()
