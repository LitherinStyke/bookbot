def get_word_count(book_contents:str):
    words = book_contents.split()
    return len(words)

def get_char_count(book_contents:str):
    words = book_contents.split()
    char_counts = {}

    for word in words:
        for chars in word:
            char = chars.lower()
            if char not in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] += 1

    return char_counts

def organize_characters(chars:dict):
    dictionary_list = []
    for char in chars:
        new_dict = {
            "char": char,
            "count": chars[char]
            }
        
        dictionary_list.append(new_dict)

    return dictionary_list
        