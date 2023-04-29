#!/usr/bin/python3
""" Defines a function that finds the peak of an unsorted array of numbers"""


def find_peak(list_of_integers):
    """"Sorts an array and returns the peak"""

    if len(list_of_integers) == 0:
        return None

    array = list_of_integers

    array.sort(reverse=True)

    return array[0]
