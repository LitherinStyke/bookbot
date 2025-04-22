import stats

def get_book_text(path_to_file:str):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = get_book_text('books/frankenstein.txt')

    print(f'{stats.get_word_count(book)} words found in the document')
    #print(stats.get_char_count(book))
    stats.organize_characters(stats.get_char_count(book))
    
main()