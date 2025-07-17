def get_num_words(file_name):
    with open(file_name) as f:
        text = f.read()
        word_list = text.split()
        return len(word_list)

def get_letter_counts(file_name):
    with open(file_name) as f:
        text = f.read()
        letter_counts = {}
        for char in text:
            if char.isalpha():
                char = char.lower()
                if char in letter_counts:
                    letter_counts[char] += 1
                else:
                    letter_counts[char] = 1
        return letter_counts


def convert_dict(input_dict):
    # Convert to list of {"char": a, "num": b} dicts, sorted by "num" descending
    items = [{"char": k, "num": v} for k, v in input_dict.items()]
    sorted_items = sorted(items, key=lambda x: x["num"], reverse=True)
    return sorted_items
