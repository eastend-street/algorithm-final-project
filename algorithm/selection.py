def selection_sort(array):
    n = len(array)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if array[min] > array[j]:
                min = j
        tmp = array[min]
        array[min] = array[i]
        array[i] = tmp

if __name__ == "__main__":
    array = [1,2,3,4,5,3,2,1,4,3,4,5,0]
    print("before", array)
    selection_sort(array)
    print("after ", array)