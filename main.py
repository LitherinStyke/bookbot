import stats

def get_book_text(path_to_file:str):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_path = 'books/frankenstein.txt'
    book = get_book_text(book_path)
    char_list = stats.organize_characters(stats.get_char_count(book))

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {stats.get_word_count(book)} total words')
    print('--------- Character Count -------')
    for char_dict in char_list:
        print(f'{char_dict['char']}: {char_dict['count']}')
    print('============= END ===============')

main()