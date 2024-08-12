def replace_symbol(symbol, position):
    """Replace the symbol based on its position (1-based indexing)."""
    if symbol == '1':
        return '123' if position % 2 != 0 else '321'
    elif symbol == '2':
        return '231' if position % 2 != 0 else '132'
    elif symbol == '3':
        return '312' if position % 2 != 0 else '213'

def construct_square_free_word(n):
    """Construct a square-free word up to the nth iteration."""
    word = '1'  # Start with a0
    
    # Iteratively construct the word up to the nth iteration
    for _ in range(n):
        new_word = ''
        for index, symbol in enumerate(word):
            # Position in the word is index + 1 (1-based index)
            new_word += replace_symbol(symbol, index + 1)
        word = new_word
    
    return word

# Example usage: Generate the sequence for n iterations
n = int(input("Enter the number of iterations: "))
result = construct_square_free_word(n)
print(f"The square-free word after {n} iterations is: {result}")
