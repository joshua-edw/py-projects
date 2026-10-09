from json.tool import main

# insertion sort: shifts larger numbers to the right and inserts the current number in the correct position
def insertion_sort(numbers):
    result = numbers.copy()
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result

# counting_sort: counts the occurrences of each number and reconstructs the sorted list based on those counts
def counting_sort(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    value_range = largest - smallest + 1
    count = [0] * value_range
    for number in numbers:
        index = number - smallest
        count[index] += 1
    result = []
    for index in range(len(count)):
        value = index + smallest
        for occurence in range(count[index]):
            result.append(value)
    return result

# merge_sort: recursively divides the list into halves, sorts each half, and merges them back together
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers.copy()
    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# choose sort: checks if the list is already sorted and returns a message if it is, otherwise uses the most efficient sort for the list size
def choose_sort(numbers):
    if not numbers:
        return [], "No sorting needed.", "The list is empty."

    size = len(numbers)
    already_sorted = all(numbers[i] <= numbers[i + 1] for i in range(size - 1))
    if already_sorted:
        return numbers.copy(), "No sorting needed.", "It's already sorted!"

    if size <= 32:
        return (
            insertion_sort(numbers),
            "Insertion sort",
            "This list is small, so insertion sort is efficient."
        )
    elif size <= 1000:
        return (
            counting_sort(numbers),
            "Counting sort",
            "This list is medium-sized, so counting sort is efficient."
        )
    else:
        return (
            merge_sort(numbers),
            "Merge sort",
            "This list is large, so merge sort is efficient."
        )


def main():
    print("This is a sorting algorithm program. Please enter a list of whole numbers separated by spaces, ")
    print("and the program will sort them for you using the most efficient sorting algorithm based on the size of the list.")
    user = input("Enter your list of whole numbers: ")
    pieces = user.split()
    numbers = []
    try:
        for piece in pieces:
            number = int(piece)
            numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter only whole numbers separated by spaces.")
        return
    if len(numbers) == 0:
        print("You did not enter any numbers. Please try again.")
        return

    sorted_numbers, method, reason = choose_sort(numbers)

    print(f"Sorted numbers: {sorted_numbers}")
    print(f"Method used: {method}")
    print(f"Reason: {reason}")
    print("Thank you.")

if __name__ == "__main__":
    main()  