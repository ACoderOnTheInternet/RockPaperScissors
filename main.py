import random
import time

print("v 1.0.0")
print("welcome to rock paper scissors!")
time.sleep(1.5)
print("--developed by Samurai Doggo Games--")
time.sleep(1.5)
print("please pick your item! (lowercase pls)")
time.sleep(1.5)
print("rock")
time.sleep(0.5)
print("paper...")
time.sleep(0.5)
print("...or scissors!")
time.sleep(0.5)
choice = input()
ai = random.randint(1,3)
if ai == 1:
	aii = "rock"
if ai == 2:
	aii = "paper"
if ai == 3:
	aii = "scissors"
if choice == "rock":
	print("AI chooses, " + aii + "!")
	if aii == "scissors":
		print("you won! hit run or ctrl+enter to restart!")
	if aii == "paper":
		print("you lost! hit run or ctrl+enter to restart!")
	if aii == "rock":
		print("draw! hit run or ctrl+enter to restart!")

if choice == "scissors":
	print("AI chooses, " + aii + "!")
	if aii == "scissors":
		print("draw! hit run or ctrl+enter to restart!")
	if aii == "paper":
		print("you won! hit run or ctrl+enter to restart!")
	if aii == "rock":
		print("you lost! hit run or ctrl+enter to restart!")

if choice == "paper":
	print("AI chooses, " + aii + "!")
	if aii == "scissors":
		print("you lost! hit run or ctrl+enter to restart!")
	if aii == "paper":
		print("draw! hit run or ctrl+enter to restart!")
	if aii == "rock":
		print("you won! hit run or enter to restart!")
