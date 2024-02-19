def normalize_by_index(list_of_lists):
    # Find the maximum value for each index across all sublists
    max_values = [max(sublist[i] for sublist in list_of_lists) for i in range(len(list_of_lists[0]))]
    
    # Normalize elements in each sublist
    normalized_lists = [[element / max_values[i] for i, element in enumerate(sublist)] for sublist in list_of_lists]
    
    return normalized_lists

# Example usage
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
normalized_lists = normalize_by_index(list_of_lists)
print(normalized_lists)