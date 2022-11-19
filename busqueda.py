import random
import busqueda_lineal as bl
import busqueda_binaria as bb

if __name__ == '__main__':
    print()
    size_list = int(input('What is the list size? '))
    objective = int(input('What number do you want to find? '))
    print()

    list_random = [random.randint(0,1000) for i in range(size_list)]
    count_b = 0
    find_it, count_b = bb.binary_search(list_random, 0, len(list_random), objective, count_b)

    find_it, count = bl.lineal_search(list_random, objective)
    print()
    print(list_random)
    print(f'\nThe item {objective}{" is" if find_it else " is not"} in the list')
    print(f'\nCount in lineal search = {count}')
    print(f'Count in binary search = {count_b}')