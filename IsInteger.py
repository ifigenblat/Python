def check_non_integers(*args):
    non_integers = [arg for arg in args if not isinstance(arg, int)]
    
    if non_integers:
        print(f"These arguments are not integers: {non_integers}")
    else:
        print("All arguments are integers.")

# Example usage:
check_non_integers(1, 2, 'a', 4.5, [6])  # Output: These arguments are not integers: ['a', 4.5, [6]]
check_non_integers(3, 5, 7)             # Output: All arguments are integers.