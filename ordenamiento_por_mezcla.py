import random

def merge_sort(list):
    if len(list) > 1:
        half = len(list)//2
        left = list[:half]
        rigth = list[half:]

        print(f'\n{left}')
        print(f'\n{rigth}')


        #Llamada recursiva en cada mitad
        merge_sort(left)
        merge_sort(rigth)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0

        #iterador para la lista principal 
        k = 0

        while i < len(left) and j < len(rigth):
            if left[i] < rigth[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = rigth[j]
                j += 1

            k += 1
        
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(rigth):
            list[k] = rigth[j]
            j += 1
            k += 1
        
    return list

if __name__ == '__main__':
    
    size_list = int(input('\nType the size list -> '))

    list = [random.randint(0,100) for i in range(size_list)]
    print(f'\n{list}')
    print('-'*20)

    sorted_list = merge_sort(list)
    print(sorted_list)