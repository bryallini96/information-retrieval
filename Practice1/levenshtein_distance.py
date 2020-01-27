def levenshtein_distance(str1, str2):
    str1_length = len(str1)
    str2_length = len(str2)

    if str1_length == 0 or str2_length == 0:
        return max(str1_length, str2_length)

    str1 = str1.lower()
    str2 = str2.lower()

    matrix = []
    for i in range(str1_length + 1):
        matrix.append([i])

    for i in range(str2_length):
        matrix[0].append(i + 1)

    for i in range(1, str1_length + 1):
        for j in range(1, str2_length + 1):
            matrix[i].append(min(matrix[i][j-1] + 1, matrix[i-1][j] + 1, matrix[i-1][j-1] + (not str1[i-1] == str2[j-1])))
    return matrix[str1_length][str2_length]

print("Ingrese la primera palabra: ")
str1 = input()
print("Ingrese la segunda palabra: ")
str2 = input()
distance = levenshtein_distance(str1, str2)
print("Distancia de Levenshtein entre",str1.lower(),"y",str2.lower(),"es:",distance)