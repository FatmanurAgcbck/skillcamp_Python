
""" 1- Write a function that flattens a list. Its elements can consist of multi-layered lists (such as [[3],2]) or non-scalar data. For example:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]"""

sampleList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten_list(sampleList):
    flatten = []
    for item in sampleList:
        if isinstance(item, list):
            flatten.extend(flatten_list(item))
        else:
            flatten.append(item)
    return flatten

op = flatten_list(sampleList)
print(op)





"""
2- Write a function that reverses the elements in the given list. If the elements inside the list also contain the list, reverse their elements as well. For example:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]"""

sample_list = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(sample_list):
    reverse = []
    for item in sample_list[::-1]:
        if isinstance(item, list):
            reverse.append(reverse_list(item))
        else:
            reverse.append(item)
    return reverse

op2 = reverse_list(sample_list)
print(op2)