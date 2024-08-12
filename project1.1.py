def thue_morse_sequence(n):
    """Generate the Thue-Morse sequence up to the n-th term."""
    # Start with t0
    sequence = '0'
    
    # Generate the sequence iteratively
    for _ in range(n):
        # Create the inverse of the current sequence
        inverse = ''.join('1' if ch == '0' else '0' for ch in sequence)
        # Append the inverse to the current sequence
        sequence += inverse
    
    return sequence

# Example usage: generate the first 10 terms of the Thue-Morse sequence
n = 10
sequence = thue_morse_sequence(n)
print(sequence)
