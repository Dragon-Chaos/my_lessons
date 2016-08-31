attemps_left = 3
while attemps_left  >0:
    attemps_left -= 1
    password = input("Enter password "
                     "(you have {} attemps left): ".format(attemps_left + 1))
    if password == "98x":
        print("Access garanted")
        break

else:
    print("Access denied")

print("Welcome!")