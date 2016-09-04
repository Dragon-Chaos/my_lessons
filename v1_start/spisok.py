int_list = [1, 10, 3, 5, 7, 12 ]
char_list = ['a', 'b', 'c', 'z', 'x']
empty_list = []

print("Numers: ", int_list)
print("String: ", char_list)
print("Empty: ", empty_list)

list_from_range = list(range(5))
print("List_from_rangr: ", list_from_range)

list_from_string = list('Visual S')
print("List_from_string: ", list_from_string)


print(list_from_string[0])
print(list_from_string[1])
print(list_from_string[-1])
print()

index = int(input("Enter index: "))
element = list_from_string[index]
print("  ", element)


list_s = int_list [:]
print("Copy list: ", list_s)
sub = list_s[0:3]
sub1 = list_s[:3]
sub2 = list_s[0:-1:2]
print(sub)
print(sub1)
print(sub2)