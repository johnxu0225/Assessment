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

#Example usage
numbers = [7, 2, 5, 3, 9]
median = sortAndFindMedian(numbers)
print("Sorted numbers:", sort(numbers))
print("Median:", median)
