def replace_symbol(symbol, position):
    """Replace the symbol based on its position (1-based indexing)."""
    if symbol == '1':
        return '123' if position % 2 != 0 else '321'
    elif symbol == '2':
        return '231' if position % 2 != 0 else '132'
    elif symbol == '3':
        return '312' if position % 2 != 0 else '213'

def square_free(n):
    """Generate the square-free sequence up to the n-th iteration."""
    word = '1'  # Start with a0
    
    # Iteratively construct the sequence up to the n-th iteration
    for _ in range(n):
        new_word = ''
        for index, symbol in enumerate(word):
            # Position in the word is index + 1 (1-based index)
            new_word += replace_symbol(symbol, index + 1)
        word = new_word
    
    return word

def print3Blocks(s):
    """Print the string in blocks of 3 symbols separated by spaces."""
    blocks = [s[i:i+3] for i in range(0, len(s), 3)]
    print(' '.join(blocks))

# Example usage
n = int(input("Enter the number of iterations for square_free: "))
result = square_free(n)
print(f"The square-free word after {n} iterations is: {result}")
print3Blocks(result)
