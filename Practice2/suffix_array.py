import operator


def suffix_array(str):
    str = str + '$'
    str = str.lower()
    str_length = len(str)
    suffix = []
    i = str_length
    while i > 0:
        i -= 1
        suffix.append(str[i:str_length])
    dictionary = dict()
    suffix_copy = suffix.copy()
    for i in range(0, str_length):
        dictionary[i] = suffix_copy.pop()
    sort = dict(sorted(dictionary.items(), key=operator.itemgetter(1)))
    suffix_sorted = list(sort.values())
    suffix_array = list(sort.keys())
    return suffix, suffix_sorted, suffix_array

print("Ingrese una palabra: ")
str = input()
suffix, suffix_sorted, suffix_array = suffix_array(str)
print("Sufijos: ", suffix)
print("Sufijos por orden lexicográfico: ", suffix_sorted)
print("Arreglo de sufijos: ", suffix_array)