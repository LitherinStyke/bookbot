from stats import get_words_from_book

def get_book_text(path_to_file:str):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    print(f'{get_words_from_book(get_book_text('books/frankenstein.txt'))} words found in the document')

main()