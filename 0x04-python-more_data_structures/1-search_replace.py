#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda l: replace if l == search else l, my_list))
    return (new_list)
