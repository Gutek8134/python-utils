def binsort(array: list, *elements: any):
    for element in elements:
        startIndex, stopIndex = 0, len(array)
        index = 0
        while stopIndex - startIndex > 1:
            index = (startIndex+stopIndex)//2
            if element == array[index]:
                break
            elif element > array[index]:
                startIndex = index
            elif element < array[index]:
                stopIndex = index
        array.insert(index, element)
    return array


def tests():
    a = [1, 2, 3, 7, 11, 16, 26]
    print(binsort(a, 3, 9, 8, 5, 20, 7))


if __name__ == "__main__":
    tests()
