def get_num_words(string):
    words = string.split()
    return len(words)

def get_num_characters(string):
    lowercase_string = string.lower()

    characters = {}
    for char in lowercase_string:
        if characters.get(char):
            characters[char] += 1
        else:
            characters[char] = 1
    
    return characters

def get_sorted_list(dictionary):
    unsorted_list = []

    for key in dictionary.keys():
        unsorted_list.append({ "char": key, "num": dictionary.get(key) })

    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list

def sort_on(items):
    return items["num"]