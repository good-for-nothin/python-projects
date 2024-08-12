def thue_morse(n):
    """Generate the Thue-Morse sequence up to the n-th iteration."""
    sequence = '0'  # Start with t0

    # Iteratively construct the sequence
    for _ in range(n):
        inverse = ''.join('1' if ch == '0' else '0' for ch in sequence)
        sequence += inverse  # Append the inverse to the current sequence
    
    return sequence
