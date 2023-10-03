#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) is not 'e':
        print("abcdefghijklmnopqrstuvwxyz"[::-1].replace('q', '').replace('e', ''))
