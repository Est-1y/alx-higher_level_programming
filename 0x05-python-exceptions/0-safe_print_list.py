#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for index in range(x):
            if index < len(my_list):
                print(my_list[index], end=" ")
                printed += 1
            else:
                break
        print()
    except Exception as e:
        print(f"Error: {e}")
    return printed
