#Tarea 2 - Arreglo de sufijos: Recuperación de información
#Elaborado por: Bryan Rodrigo Quiroz Palominos

import operator
import re


def read_file(path):
    file = open(path)
    content = file.read()
    file.close()
    return content


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


def clean_string(str_to_clean):
    str_with_only_alphanumeric =  re.compile(r'\W+', re.UNICODE).split(str_to_clean)
    str_clean = " ".join(str_with_only_alphanumeric).replace("_", "").strip().lower()
    str_clean = " ".join(str_clean.split())
    return str_clean


file_content = read_file('test.txt')
print('Contenido del archivo:', file_content)
str_clean = clean_string(file_content)
print("Ingrese palabra a buscar: ")
str_find = input()
print('Contenido normalizado:', str_clean)
suffix, suffix_array = suffix_array(str_clean)
inf, sup = search(str_find[0], suffix, suffix_array)
ocurrences = occurrences(inf, sup, str_find, suffix, suffix_array)
print(ocurrences,"ocurrencias de:",str_find,"en",str_clean)