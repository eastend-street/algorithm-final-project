def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        # i means position of array
        tmp = array[i]
        if tmp < array[i-1]:
            j = i
            print(j)
            while True:
                array[j] = array[j-1]
                j -= 1
                if j == 0 or tmp >= array[j-1]:
                    break
            array[j] = tmp


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 3, 2, 1, 4, 3, 4, 5, 0]
    print("before", array)
    insertion_sort(array)
    print("after ", array)
