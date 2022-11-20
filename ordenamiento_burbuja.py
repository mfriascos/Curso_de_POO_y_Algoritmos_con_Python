import random

def bubble_sort(list):
    n = len(list)

    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1],list[j]
    return list

if __name__ == '__main__':
    
    size_list = int(input('Type the size list -> '))

    list = [random.randint(0,100) for i in range(size_list)]
    print(f'\n{list}')

    sorted_list = bubble_sort(list)
    print(sorted_list)