
def binary_search(list_random, start, end, objective, count_b):
    list_random = sorted(list_random)
    count_b += 1
    print(f'Buscando {objective} entre {list_random[start]} y {list_random[end - 1]}')
    if start > end:
        return False, count_b

    half = (start + end)//2

    if list_random[half] == objective:
        return True, count_b 
    elif list_random[half] < objective:
        return binary_search(list_random, half + 1, end, objective, count_b)
    else:
        return binary_search(list_random, start, half - 1, objective, count_b)
    