#Tarea 2 - Arreglo de sufijos: Recuperación de información
#Elaborado por: Bryan Rodrigo Quiroz Palominos

import operator


def suffix_array(str):
    str = str + '$'
    str = str.lower()
    str_length = len(str)
    suffix = []
    i = 0
    while i < str_length:
        suffix.append(str[i:str_length])
        i += 1
    dictionary = dict()
    for i in range(0, str_length):
        value = suffix[i]
        if value[0] != " " and value[0] != "." and value[0] != ",":
            dictionary[i] = value
    sort = dict(sorted(dictionary.items(), key=operator.itemgetter(1)))
    suffix_sorted = list(sort.values())
    suffix_array = list(sort.keys())
    print("Sufijos: ", list(dictionary.values()))
    print("Sufijos por orden lexicográfico: ", suffix_sorted)
    print("Arreglo de sufijos: ", suffix_array)
    return suffix, suffix_array


def search(sub_str, suffix, suffix_array):
    l = 1
    r = len(suffix_array)
    while l < r:
        mid = (l + r) // 2
        if sub_str > suffix[suffix_array[mid]][0]:
            l = mid + 1
        else:
            r = mid
    s = l
    r = len(suffix_array)
    while l < r:
        mid = ((l + r) // 2)
        if sub_str == suffix[suffix_array[mid]][0]:
            l = mid + 1
        else:
            r = mid - 1
    return s, r


def occurrences(inf, sup, str, suffix, suffix_array):
    suffix_array_copy = suffix_array[inf:sup+1]
    ocurrence = 0
    for i in suffix_array_copy:
        if suffix[i].startswith(str):
            ocurrence +=1
    return ocurrence


print("Ingrese una palabra o texto: ")
str = input()
print("Ingrese palabra a buscar: ")
str_find = input()
suffix, suffix_array = suffix_array(str)
inf, sup = search(str_find[0], suffix, suffix_array)
ocurrences = occurrences(inf, sup, str_find, suffix, suffix_array)
print(ocurrences,"ocurrencias de:",str_find,"en",str)