def get_num_words(text):
    words = text.split()
    return len(words)


def char_count(text):
    dict = {}
    for char in text:
        if char.lower() in dict:
            dict[char.lower()] += 1
        else:
            dict[char.lower()] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    dict_list = []

    for key in dict:
        if not key.isalpha():
            continue
        dict_list.append({"char":key, "num":dict[key]})

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list