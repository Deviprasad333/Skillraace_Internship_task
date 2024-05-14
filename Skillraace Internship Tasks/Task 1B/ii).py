def calculate_flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    combined_characters = list(name1 + name2)

    char_count = {}
    for char in combined_characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    common_chars_count = sum(min(char_count.get(char, 0), 2) for char in set(combined_characters))

    total_chars = len(name1) + len(name2)
    remaining_chars = total_chars - common_chars_count

    relationships = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']

    while len(relationships) > 1:
        idx = (remaining_chars % len(relationships)) - 1

        if idx >= 0:
            relationships = relationships[idx + 1:] + relationships[:idx]
        else:
            relationships = relationships[:len(relationships) - 1]

    return relationships[0]

# Example usage:
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

relationship = calculate_flames(name1, name2)
print(f"The relationship between {name1} and {name2} is: {relationship}")
