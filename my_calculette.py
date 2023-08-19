def welcome_message():
	print("Welcome to Alex' Mega calculator")
	print("=== MENU ===")
	print("1- Multiplication")
	print("2- Division")
	print("3- Addition")
	print("4- Soustraction")

def switch(choix):
	input1, input2 = get_user_input()
	match choix:
		case '1':
			multi(input1, input2)
		case '2':
			division(input1, input2)
		case '3':
			addition(input1, input2)
		case '4':
			soustraction(input1, input2)
		case _:
			print("Error")



def get_user_input():
	# Get user inputs from CLI
	input1 = input("Enter your first number: ")
	input2 = input("Enter your second number: ")

	# Convert inputs to integers
	input1 = int(input1)
	input2 = int(input2)
	
	return input1, input2

def soustraction(a,b):
	print("Soustraction de %d et %d egale %d" % (a, b, a-b)) 

def addition(a,b):
	print("Addition de %d et %d egale %d" % (a, b, a+b)) 

def multi(a,b):
	print("Multiplication de %d et %d egale %d" % (a, b, a*b))

def division(a,b):	
	while b==0:
		print("Error, your denominator equals 0")
		b = int(input("Choose an naother denominator :"))
	print("Division de %d et %d egale %d" % (a, b, a/b)) 

def main():
	welcome_message()
	choix = input("Choose your desired operation :")
	switch(choix)
	
	

if __name__ == "__main__":
    main()