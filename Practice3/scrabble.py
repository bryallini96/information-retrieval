import operator

letter_values = dict(a=1, b=3, c=3, ch=5, d=2, e=1, f=4, g=2, h=4, i=1, j=8, k=0, l=1, ll=8, m=3, n=1, ñ=8, o=1, p=3,
                     q=5, r=1, rr=8, s=1, t=1, u=1, v=4, w=0, x=8, y=4, z=10)

inverted_index = dict(a=[], b=[], c=[], d=[], e=[], f=[], g=[], h=[], i=[], j=[], k=[], l=[], m=[], n=[],
                      ñ=[], o=[], p=[],
                      q=[], r=[], s=[], t=[], u=[], v=[], w=[], x=[], y=[], z=[])


def read_file(path):
    file = open(path)
    content = file.read()
    file.close()
    return content


def get_words_of_file(content):
    list_words = content.split('\n')
    i = 0
    for word in list_words:
        letters = get_word_letters(word)
        for id, value in letters.items():
            inverted_index[id].append((i, value))
        i += 1
    return list_words


def word_value(word_list):
    value = 0
    for i in word_list:
        value = value + letter_values.get(i)
    return value


def enter_letters():
    word_list = []
    validation = False
    for i in range(7):
        while not validation:
            print('Ingrese la palabra #', i + 1)
            letter = input()
            validation = validate_enter_letter(letter)
        word_list.append(letter)
        validation = False
    return word_list


def validate_enter_letter(letter):
    valid_letters = dict(a=1, b=1, c=1, d=1, e=1, f=1, g=1, h=1, i=1, j=1, k=1, l=1, m=1, n=1,
                          ñ=1, o=1, p=1,
                          q=1, r=1, s=1, t=1, u=1, v=1, w=1, x=1, y=1, z=1)
    if valid_letters.get(letter):
        return True
    return False


def get_word_letters(word):
    letters = dict()
    for i in range(len(word)):
        cant = letters.get(word[i])
        if cant:
            cant += 1
            letters[word[i]] = cant
        else:
            letters[word[i]] = 1
    return letters


def get_word_lists(lista):
    keys = list(lista.keys())
    j = 0
    dic = dict()
    for i in keys:
        lista = inverted_index.get(i)
        if lista:
            dic[j] = lista
        j += 1
    return dic


def create_set(values):
    s = set()
    for i in values:
        for j in i:
            s.add(j[0])
    return s


def get_list_to_intersect(list):
    list_to_intersect = []
    for k in list:
        list_to_intersect.append(k[0])
    return list_to_intersect


def intersect_words(lists, frecuency):
    s = create_set(lists.values())
    final_list = []
    for i in s:
        word = word_list[i]
        intersect_set = set()
        intersect_set.add(i)
        sum = 0
        for j in lists.values():
            intersect_list = get_list_to_intersect(j)
            list_to_set = set(intersect_list)
            result = list_to_set.intersection(intersect_set)
            if result:
                sum += 1
        #if len(frecuency) == sum:
        if len(word) == sum or sum == len(frecuency):
            final_list.append(word)
    return final_list


def rank_words(word_list):
    rank = dict()
    for i in word_list:
        value = word_value(i)
        rank[i] = value
    rank_sort = sorted(rank.items(), key=operator.itemgetter(1), reverse=True)

    for value, word in rank_sort:
        print(word, 'puntuación -->', value)


#file_content = read_file('dict/diccionario.txt')
file_content = read_file('dict/test.txt')
word_list = get_words_of_file(file_content)
letters = enter_letters()
print('Palabras de archivo',word_list)
print('Letras ingresadas',letters)
frecuency = get_word_letters(letters)
lists = get_word_lists(frecuency)
final_list = intersect_words(lists, frecuency)
print(final_list)
if len(final_list) > 0:
    rank_words(final_list)
else:
    print("No se encontraron palabras")