"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(0,len(items)):
        if frequencies.get(str(items[i])) :
            frequencies.update({str(items[i]):frequencies.get(str(items[i]))+1})
        else:
            frequencies[str(items[i])] = 1
    return frequencies
