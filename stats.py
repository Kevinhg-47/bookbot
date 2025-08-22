import sys

def get_num_words(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    num_words = len(file_contents.split())
    return num_words
    
def count_characters(book_path):
    char_count = {}

    with open(book_path) as f:
        file_contents = f.read()
    characters = [c.lower() for palabra in file_contents for c in palabra]
    for char in characters:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(char_count_dict):
    sorted_list = [{"char": char, "num": count} for char, count in char_count_dict.items()]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list