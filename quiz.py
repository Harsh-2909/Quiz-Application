import json
import random

with open("assets/questions.json", 'r') as f:
	j = json.load(f)
	no_of_questions = len(j['questions'])
	ch = random.randint(0, no_of_questions-1)
	print(j["questions"][ch]["question"])
	for option in j["questions"][ch]["options"]:
		print(option)
	answer = input("Enter your answer: ")
	if j["questions"][ch]["answer"][0] == answer[0].upper():
		print("You are correct")
	else:
		print("You are incorrect")

# if "__name__" == "__main__":
# 	choice = 1
# 	while choice != 4:
# 		print('=========WELCOME TO QUIZ MASTER==========')
# 		print('-----------------------------------------')
# 		print('1. PLAY QUIZ')
# 		print('2. ADD QUIZ QUESTIONS')
# 		print('3. CREATE AN ACCOUNT')
# 		print('4. EXIT')
# 		choice = input('ENTER YOUR CHOICE: ')
# 		if choice == 1:
# 			pass
# 		elif choice == 2:
# 			pass
# 		elif choice == 3:
# 			pass
# 		elif choice == 4:
# 			pass
# 		else:
# 			print('WRONG INPUT. ENTER THE CHOICE AGAIN')
