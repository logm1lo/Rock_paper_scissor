from random import randint

print("Nhap Rock, Paper, Scissor:")
player = input()
computer = randint(0,2)

if computer == 0:
	computer = "Rock"
if computer == 1:
	computer = "Paper"
if computer == 2:
	computer = "Scissor"

print("---------------------")
print("You choose:" + player)
print("Computer chooses:" + computer)
print("---------------------")

if player == computer:
	print("Draw")
else:
	if player == "Rock":
		if computer == "Paper":
			print("Lose")
		else:
			print ("Win")
	
	elif player == "Paper":
		if computer == "Rock":
			print("Win")
		else:
			print ("Lose")
	
	elif player == "Scissor":
		if computer == "Paper":
			print("Win")
		else:
			print ("Lose")
	else:
		print("Wrong answer, please try again")



