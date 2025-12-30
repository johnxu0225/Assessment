def sort(numbers):
    #Bubble sort implementation
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                #Swap if the element is greater than the next
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def sortAndFindMedian(numbers):
    #Sort the numbers first
    sorted_numbers = sort(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        #Even number of elements: median is the average of the middle two
        mid1 = n//2 - 1
        mid2 = n//2
        return (sorted_numbers[mid1] + sorted_numbers[mid2]) / 2
    else:
        #Odd number of elements: median is the middle element
        mid = n//2
        return sorted_numbers[mid]

def main():
    #User input
    input_str = input("Enter numbers separated by spaces: ")
    numbers = list(map(float, input_str.strip().split()))
    
    median = sortAndFindMedian(numbers)
    print("Median of the numbers is:", median)

if __name__ == "__main__":
    main()
# This program calculates the median of a list of numbers.
# First, it sorts the list using a sorting algorithm (selection sort in this case).
# After sorting, it checks if the list has an even or odd number of elements.
# If even, the median is the average of the two middle numbers.
# If odd, the median is the middle number.
# The program allows the user to input numbers separated by spaces and then outputs the median.