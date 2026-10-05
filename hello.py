print("IT Help Desk Assistant")
print("-----------------------")
print("Welcome!")
print()
print("What problem are you having?")
print("1. Internet connection")
print("2. Computer running slowly")
print("3. Printer problem")
print("4. Password problem")

choice = input("Enter the number of your problem: ")

if choice == "1":
	print("Let's troubleshoot your Internet connection.")
	print("1. Check that Wi-Fi is turned on.")
	print("2. Check whether other devices have Internet.")
	print("3. Restart your router.")
	print("4. Try connecting again.")
elif choice == "2":
	print("Let's troubleshoot your slow computer.")
elif choice == "3":
	print("Let's troubleshoot your printer.")
elif choice == "4":
	print("Let's troubleshoot your password problem.")
else:
	print("Please choose a number from 1 to 4.")
