def main():
    letters_count_dict = {}
    path_to_file = 'books/frankenstein.txt'
    text = read_file(path_to_file).lower()
    num_words = word_count(text)

    for char in text:
        if char.isalpha():
            if char in letters_count_dict:
                letters_count_dict[char] += 1
            else:
                letters_count_dict[char] = 1
    # print(letters_count_dict)

    sorted_list = sort_dict(letters_count_dict)

    print_report(path_to_file, num_words, sorted_list)

    # print(f'--- Begin report of {path_to_file} ---')
    # print(f'{num_words} words in this document')

def read_file(path):
    with open(path) as f:
      return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def sort_count(dict):
    return dict['count']

def sort_dict(letters_count_dict):
    list = [{'letter': k, 'count': v} for k, v in letters_count_dict.items()]
    list.sort(reverse=True, key=sort_count)

    return list

def print_report(path_to_file, num_words, sorted_list):
    print(f'--- Begin report of {path_to_file} ---')
    print(f'{num_words} words found in the document')
    print()
    for item in sorted_list:
        letter = item['letter']
        count = item['count']
        print(f"The '{letter}' character was found {count} times")
    print('--- End report ---')

main()

