#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''


from numpy import number

def quicksort(numbers_in_a_list):
    if len(numbers_in_a_list) == 1:
        return numbers_in_a_list[0]

def quicksort(a, low, high):
    if low < high:

        pivot = a[high]
        index = low

        for item in range(low, high):
            if a[item] <= pivot:
            
                a[item], a[index] = a[index], a[item]
                index += 1
    
        a[index], a[high] = a[high], a[index]

        quicksort(a, low, index-1)
        quicksort(a,index+1, high)

    return a

#WRITE YOUR CODE HERE FOR THE RECURSIVE SORTING FUNCTION

    return quicksort(numbers_in_a_list[1:]) if numbers_in_a_list[0] < numbers_in_a_list[1] else quicksort(numbers_in_a_list[:1] + numbers_in_a_list[2:])

numlist = '/Users/reno/Documents/Code/InClassAssignment-5/InClassAssignment-5/numbers.txt'

def main():
    sortedlist = []
    quicksort(numlist)
# WRITE YOUR MAIN FUNCTION HERE TO READ IN YOUR numbers.txt FILE, RUN THE LIST THROUGH YOUR SORTING ALGORITHM, 
# AND WRITE OUT YOUR FILE

    return quicksort(numlist)


if __name__ == "__main__":
    main()
