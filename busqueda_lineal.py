# permite encontrar si un objeto está dentro de una iterable.

def lineal_search(list_random, objective):
    match = False
    count = 0
    for element in list_random: # O(n)
        count += 1
        if element == objective:
            match = True
            break
    
    return match, count
