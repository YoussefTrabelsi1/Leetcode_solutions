def romanToInt(s: str) -> int:
    # Roman numeral symbol-to-value map
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 
        'L': 50, 'C': 100, 
        'D': 500, 'M': 1000
    }
    
    total = 0  # To store the result
    prev_value = 0  # To track the previous Roman numeral value

    # Iterate through the Roman numeral string in reverse order
    for char in reversed(s):
        current_value = roman_map[char]
        
        # If the current value is smaller than the previous, subtract it
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        # Update previous value
        prev_value = current_value

    return total
