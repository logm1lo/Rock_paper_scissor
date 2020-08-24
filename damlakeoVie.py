from random import randint

print("Nhap Đấm, Lá, Kéo:")
player = input()
computer = randint(0,2)

if computer == 0:
	computer = "Đấm"
if computer == 1:
	computer = "Lá"
if computer == 2:
	computer = "Kéo"

print("---------------------")
print("Bạn chọn:" + player)
print("Máy chọn:" + computer)
print("---------------------")

if player == computer:
	print("Hòa")
else:
	if player == "Đấm":
		if computer == "Lá":
			print("Thua")
		else:
			print ("Thắng")
	
	elif player == "Lá":
		if computer == "Đấm":
			print("Thắng")
		else:
			print ("Thua")
	
	elif player == "Kéo":
		if computer == "Lá":
			print("Thắng")
		else:
			print ("Thua")
	else:
		print("Nhập sai, vui lòng nhập lại")



