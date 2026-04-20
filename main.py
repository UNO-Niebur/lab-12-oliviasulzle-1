# SearchSortLab.py
# Name: Olivia Sulzle
# Date: 4/19/26
# Assignment: Lab 13 – Searching and Sorting


def linearSearch(data, target):
    """Return the index of target if found, otherwise return -1."""
    
    # TODO: implement linear search
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def bubbleSort(data):
    """Sort the list using bubble sort and return the sorted list."""
    
    # TODO: implement bubble sort
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def main():
    # Test lists
    sortedList = [1, 2, 3, 4, 5]
    reversedList = [5, 4, 3, 2, 1]
    randomList = [3, 1, 4, 2, 5]

    # Test linear search
    print("Search for 4 in randomList:", linearSearch(randomList, 4))
    print("Search for 10 in randomList:", linearSearch(randomList, 10))

    # Test sorting
    print("Sorted list:", bubbleSort(sortedList.copy()))
    print("Reversed list sorted:", bubbleSort(reversedList.copy()))
    print("Random list sorted:", bubbleSort(randomList.copy()))


if __name__ == "__main__":
    main()

# Reflection Questions:
# 1. Which list was easiest to sort? Why?
#    The sorted list ([1, 2, 3, 4, 5]) was easiest to sort because it was already in ascending order,
#    so bubble sort didn't have many steps.

# 2. Which list required the most work?
#    The reversed list ([5, 4, 3, 2, 1]) required the most work because bubble sort had to swap elements
#    multiple times to move the largest elements to the end each time.

# 3. Why is sorting useful before searching?
#    Sorting allows for more efficient search algorithms like binary search, which can find elements
#    in O(log n) time compared to linear search's O(n) time. This is especially important for large datasets.

# 4. When might linear search still be useful?
#    Linear search is still useful for small lists where the overhead of sorting isn't worthwhile,
#    for unsorted data that doesn't need to be searched repeatedly, or when searching for multiple
#    occurrences of an element.
