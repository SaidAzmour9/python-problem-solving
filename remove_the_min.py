def remove_smallest(numbers):

    if len(numbers) < 1:
        return []
    else:
        numbers = numbers.copy()
        numbers.remove(min(numbers))

        return numbers