def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# Test case
input_sequence = [23, 35, 2, 4, 5, 35, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  
