def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letter_count = {}
    for char in text:
        char = char.lower()
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count

def sort_dict(d):
    sorted_list = []
    for key in d:
        if key.isalpha():
            sorted_list.append(({"char" : key, "num": d[key]}))
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list