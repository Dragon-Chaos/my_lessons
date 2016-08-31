#example 1
for a in range(10):
    print ("A = ", a)

print ("A = ", a + 1)
#example 2
for b in range(10, 20):
    print ("b = ", b)
#example 3
for c in range(0, 100, 10):
    print ("c = ", c)
#example 4
for d in range(10, 0, -1):
    print ("d = ", d)
#example 5

for attemps_left in range(3, 0, -1):
    password = input("Enter password "
                     "(you have {} attemps left): ".format(attemps_left))
    if password == "98x":
        print("Access garanted")
        print("Welcome!")
        break

else:
    print("Access denied")

