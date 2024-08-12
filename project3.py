def count_squares(s):
    """Count the number of squares (two consecutive identical sub-words) in the string s."""
    count = 0
    length = len(s)
    
    # Iterate over possible starting points for squares
    for i in range(length):
        for j in range(1, (length - i) // 2 + 1):
            # Compare the subword starting at i with the next one of the same length
            if s[i:i+j] == s[i+j:i+2*j]:
                count += 1
    
    return count

# Example usage
example_string = '1231233'
result = count_squares(example_string)
print(f"The number of squares in the string '{example_string}' is: {result}")
