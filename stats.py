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
        if not char.isalpha(): continue
        
        new_dict = {
            "char": char,
            "count": chars[char]
            }
        
        dictionary_list.append(new_dict)

    def sort_on(dict):
        return dict['count']
    
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list
        