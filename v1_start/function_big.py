# -*- coding: utf-8 -*-
#?????? ???????? ??????? ????????

def print_info(object_name='unknown object', color='unknown colors', price=0):
    
    print("Print_info...")
    print()
    print("Object:", object_name, sep = '\t')
    print("Color:", color, sep = '\t')
    print("Price:", price, sep = '\t')
    print()
    print()

print_info('Cup', 'blue', 40)

print_info(object_name='pen',
           color='red',
           price=10)

print_info(price=5, object_name='cubok', color='orange')

print_info('coffe', price=10, color='black')

print_info(color='neon')

