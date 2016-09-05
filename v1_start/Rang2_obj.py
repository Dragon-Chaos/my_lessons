class MyObject:
    int_field = 8
    str_field = "A string"

print(MyObject.int_field)
print(MyObject.str_field)
print()

object1 = MyObject()
object2 = MyObject()

print(object1.int_field)
print(object2.str_field)
print()

MyObject.int_field = 10
print(MyObject.int_field)
print(object1.int_field)
print()

object1.str_field = "anoher string"
print("MyObject: ",MyObject.str_field)
print("object1: ", object1.str_field)
print("object2: ", object2.str_field)
print()
