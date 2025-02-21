# using random library to generate random list
import random
# using timeit library for better consistency than built in timer()
import timeit
# using OS library to detect operating system
from os import system, name


# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# to pause program for viewing
def pause():
    try:
        input("Press Enter to continue...")
    except SyntaxError:
        pass


def this_is_a_dashing_line():
    print("\n----------------------------------------------------------\n")


# bubble sort algorithm
def bubbleSort(array, option):
    for passnum in range(len(array)-1, 0, -1):
        if option == 1:
            # ascending order sort
            for i in range(passnum):
                if array[i] > array[i+1]:
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp
        elif option == 2:
            # Descending order sort
            for i in range(passnum):
                if array[i] < array[i+1]:
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp
    return array


# insertion sort algorithm
def insertionSort(array, option):
    for i in range(1, len(array)):
        # element to be compared
        current = array[i]

        # comparing the current element with the sorted portion and swapping
        if option == 1:
            while i > 0 and array[i-1] > current:  # sort ascending
                array[i] = array[i-1]
                i = i-1
                array[i] = current
        elif option == 2:
            while i > 0 and array[i-1] < current:  # sort descending
                array[i] = array[i-1]
                i = i-1
                array[i] = current

    return array


# ascending merge sort algorithm
def mergeSort(L):
    array = []
    if len(L) == 1:
        return L
    mid = len(L) // 2

    sublist1 = mergeSort(L[:mid])

    sublist2 = mergeSort(L[mid:])

    x, y = 0, 0
    while x < len(sublist1) and y < len(sublist2):
        if sublist1[x] > sublist2[y]:  # < for descending
            array.append(sublist2[y])
            y = y + 1

        else:
            array.append(sublist1[x])
            x = x + 1

    array = array + sublist1[x:]

    array = array + sublist2[y:]
    return array


# descending merge sort algorithm
def reverseMergeSort(array):
    newList = []
    if len(array) == 1:
        return array
    mid = len(array) // 2

    sublist1 = reverseMergeSort(array[:mid])

    sublist2 = reverseMergeSort(array[mid:])

    x, y = 0, 0
    while x < len(sublist1) and y < len(sublist2):
        if sublist1[x] < sublist2[y]:  # < for descending
            newList.append(sublist2[y])
            y = y + 1

        else:
            newList.append(sublist1[x])
            x = x + 1

    newList = newList + sublist1[x:]

    newList = newList + sublist2[y:]

    return newList


# generate 1000 element ascending list
def ascendingList():
    counter = 0
    mylist = []
    for i in range(999):
        mylist.append(counter)
        counter += 1
    return mylist


# generate 1000 element descending list
def descendingList():
    counter = 998
    mylist = []
    for i in range(999):
        mylist.append(counter)
        counter -= 1
    return mylist


# generate 1000 element random list
def randomList():
    mylist = []
    random.seed(1)
    for i in range(999):
        mylist.append(random.randint(1, 999))
    return mylist


# main menu
def showMenuOuter():
    print("Please choose a sorting method to perform: ")
    print("1. Insertion Sort")
    print("2. Bubble Sort")
    print("3. Merge Sort")
    print("4. Exit System")


# second layer menu
def showMenuInner():
    print("Please choose a list to perform sorting method: ")
    print("1. Ascending Order List")
    print("2. Descending Order List")
    print("3. Random Order List")
    print("4. Return to main menu")


# third layer menu
def showMenuInnerMost():
    print("Please choose the order to perform sorting method: ")
    print("1. Ascending Order")
    print("2. Descending Order")
    print("3. Return to previous menu")


# algorithm for main menu
def optionOuter():
    while True:
        clear()
        showMenuOuter()
        try:
            choice1 = int(input("Choice: "))
        except ValueError:
            print("Enter number only.\n")
            pause()
            continue

        if choice1 == 1:
            clear()
            optionInner(choice1)

        elif choice1 == 2:
            clear()
            optionInner(choice1)

        elif choice1 == 3:
            clear()
            optionInner(choice1)

        elif choice1 == 4:
            clear()
            print("Thank you for using XYZ sorting system.\n")
            return False
        else:
            print("Choose option 1-4 only.\n")


# algorithm for second layer menu
def optionInner(choice1):
    while True:
        clear()
        showMenuInner()
        try:
            choice2 = int(input("Choice: "))
        except ValueError:
            print("Enter number only.\n")
            pause()
            continue

        if choice2 == 1:
            clear()
            optionInnerMost(choice1, choice2)

        elif choice2 == 2:
            clear()
            optionInnerMost(choice1, choice2)

        elif choice2 == 3:
            clear()
            optionInnerMost(choice1, choice2)

        elif choice2 == 4:
            clear()
            return False
        else:
            print("Choose option 1-4 only.\n")


# algorithm for third layer menu
def optionInnerMost(choice1, choice2):
    while True:
        clear()
        showMenuInnerMost()
        try:
            choice3 = int(input("Choice: "))
        except ValueError:
            print("Enter number only.\n")
            pause()
            continue

        if choice3 == 1:
            if choice1 == 1 and choice2 == 1:
                clear()
                print("Original List = {}" .format(ascendingList()))
                this_is_a_dashing_line()
                ascending = ascendingList()
                starttime = timeit.default_timer()
                sortedList = insertionSort(ascending, choice3)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Insertion Sort")
                print("Sort Ascending list in Ascending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 1 and choice2 == 2:
                clear()
                print("Original List = {}" .format(descendingList()))
                this_is_a_dashing_line()
                descending = descendingList()
                starttime = timeit.default_timer()
                sortedList = insertionSort(descending, choice3)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}".format(sortedList))
                this_is_a_dashing_line()
                print("Insertion Sort")
                print("Sort Descending list in Ascending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 1 and choice2 == 3:
                clear()
                print("Original List = {}" .format(randomList()))
                this_is_a_dashing_line()
                random = randomList()
                starttime = timeit.default_timer()
                sortedList = insertionSort(random, choice3)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Insertion Sort")
                print("Sort Random list in Ascending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 2 and choice2 == 1:
                clear()
                print("Original List = {}" .format(ascendingList()))
                this_is_a_dashing_line()
                ascending = ascendingList()
                starttime = timeit.default_timer()
                sortedList = bubbleSort(ascending, choice3)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Bubble Sort")
                print("Sort Ascending list in Ascending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 2 and choice2 == 2:
                clear()
                print("Original List = {}" .format(descendingList()))
                this_is_a_dashing_line()
                descending = descendingList()
                starttime = timeit.default_timer()
                sortedList = bubbleSort(descending, choice3)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Bubble Sort")
                print("Sort Descending list in Ascending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 2 and choice2 == 3:
                clear()
                print("Original List = {}" .format(randomList()))
                this_is_a_dashing_line()
                random = randomList()
                starttime = timeit.default_timer()
                sortedList = bubbleSort(random, choice3)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Bubble Sort")
                print("Sort Random list in Ascending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 3 and choice2 == 1:
                clear()
                print("Original List = {}" .format(ascendingList()))
                this_is_a_dashing_line()
                ascending = ascendingList()
                starttime = timeit.default_timer()
                sortedList = mergeSort(ascending)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Merge Sort")
                print("Sort Ascending list in Ascending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 3 and choice2 == 2:
                clear()
                print("Original List = {}" .format(descendingList()))
                this_is_a_dashing_line()
                descending = descendingList()
                starttime = timeit.default_timer()
                sortedList = mergeSort(descending)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Merge Sort")
                print("Sort Descending list in Ascending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 3 and choice2 == 3:
                clear()
                print("Original List = {}" .format(randomList()))
                this_is_a_dashing_line()
                random = randomList()
                starttime = timeit.default_timer()
                sortedList = mergeSort(random)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Merge Sort")
                print("Sort Random list in Ascending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

        elif choice3 == 2:
            if choice1 == 1 and choice2 == 1:
                clear()
                print("Original List = {}" .format(ascendingList()))
                this_is_a_dashing_line()
                ascending = ascendingList()
                starttime = timeit.default_timer()
                sortedList = insertionSort(ascending, choice3)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Insertion Sort")
                print("Sort Ascending list in descending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 1 and choice2 == 2:
                clear()
                print("Original List = {}" .format(descendingList()))
                this_is_a_dashing_line()
                descending = descendingList()
                starttime = timeit.default_timer()
                sortedList = insertionSort(descending, choice3)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Insertion Sort")
                print("Sort Descending list in descending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 1 and choice2 == 3:
                clear()
                print("Original List = {}" .format(randomList()))
                this_is_a_dashing_line()
                random = randomList()
                starttime = timeit.default_timer()
                sortedList = insertionSort(random, choice3)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Insertion Sort")
                print("Sort Random list in descending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 2 and choice2 == 1:
                clear()
                print("Original List = {}" .format(ascendingList()))
                this_is_a_dashing_line()
                ascending = ascendingList()
                starttime = timeit.default_timer()
                sortedList = bubbleSort(ascending, choice3)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Bubble Sort")
                print("Sort Ascending list in descending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 2 and choice2 == 2:
                clear()
                print("Original List = {}" .format(descendingList()))
                this_is_a_dashing_line()
                descending = descendingList()
                starttime = timeit.default_timer()
                sortedList = bubbleSort(descending, choice3)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Bubble Sort")
                print("Sort Descending list in descending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 2 and choice2 == 3:
                clear()
                print("Original List = {}" .format(randomList()))
                this_is_a_dashing_line()
                random = randomList()
                starttime = timeit.default_timer()
                sortedList = bubbleSort(random, choice3)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Bubble Sort")
                print("Sort Random list in descending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 3 and choice2 == 1:
                clear()
                print("Original List = {}" .format(ascendingList()))
                this_is_a_dashing_line()
                ascending = ascendingList()
                starttime = timeit.default_timer()
                sortedList = reverseMergeSort(ascending)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Merge Sort")
                print("Sort Ascending list in descending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 3 and choice2 == 2:
                clear()
                print("Original List = {}" .format(descendingList()))
                this_is_a_dashing_line()
                descending = descendingList()
                starttime = timeit.default_timer()
                sortedList = reverseMergeSort(descending)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Merge Sort")
                print("Sort Descending list in descending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

            elif choice1 == 3 and choice2 == 3:
                clear()
                print("Original List = {}" .format(randomList()))
                this_is_a_dashing_line()
                random = randomList()
                starttime = timeit.default_timer()
                sortedList = reverseMergeSort(random)
                timeDiff = timeit.default_timer() - starttime
                print("Sorted List = {}" .format(sortedList))
                this_is_a_dashing_line()
                print("Merge Sort")
                print("Sort Random list in descending order")
                print("Result: {} second."
                      .format(timeDiff))
                pause()

        elif choice3 == 3:
            clear()
            return False
        else:
            print("Choose option 1-3 only.\n")


if __name__ == "__main__":
    optionOuter()
