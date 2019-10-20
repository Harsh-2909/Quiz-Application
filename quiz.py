import json
import random
import getpass

def play():
	score = 0
	with open("assets/questions.json", 'r+') as f:
		j = json.load(f)
		no_of_questions = len(j['questions'])
		for i in range(10):
			ch = random.randint(0, no_of_questions-1)
			print(f'Q{i+1} {j["questions"][ch]["question"]}')
			for option in j["questions"][ch]["options"]:
				print(option)
			answer = input("Enter your answer: ")
			if j["questions"][ch]["answer"][0] == answer[0].upper():
				print("You are correct")
				score+=1
			else:
				print("You are incorrect")
		print(f'FINAL SCORE: {score}')

def createAccount():
	username = input("Enter your USERNAME: ")
	password = getpass.getpass(prompt= 'Enter your PASSWORD: ')
	with open('assets/user_accounts.json', 'r+') as user_accounts:
		users = json.load(user_accounts)
		if username in users.keys():
			print("An account of this Username already exists.\nPlease enter the login panel.")
		else:
			users[username] = [password, 0]
			user_accounts.seek(0)
			json.dump(users, user_accounts)
			user_accounts.truncate()
			print("Account created successfully!")

def loginAccount():
	print('==========LOGIN PANEL==========')
	username = input("USERNAME: ")
	password = getpass.getpass(prompt= 'PASSWORD: ')
	with open('assets/user_accounts.json', 'r') as user_accounts:
		users = json.load(user_accounts)
	if username not in users.keys():
		print("An account of that name doesn't exist.\nPlease create an account first.")
	elif username in users.keys():
		if users[username][0] != password:
			print("Your password is incorrect.\nPlease enter the correct password and try again.")
		elif users[username][0] == password:
			print("You have successfully logged in.\n")


if __name__ == "__main__":
	choice = 1
	while choice != 6:
		print('=========WELCOME TO QUIZ MASTER==========')
		print('-----------------------------------------')
		print('1. PLAY QUIZ')
		print('2. ADD QUIZ QUESTIONS')
		print('3. CREATE AN ACCOUNT')
		print('4. LOGIN PANEL')
		print('5. SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
		print('6. EXIT')
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			play()
		elif choice == 2:
			pass
		elif choice == 3:
			createAccount()
		elif choice == 4:
			loginAccount()
		elif choice == 5:
			pass
		elif choice == 6:
			break
		else:
			print('WRONG INPUT. ENTER THE CHOICE AGAIN')
