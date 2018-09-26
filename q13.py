import math
import itertools

remove_list = ["+", "="]
base_text = "read+write+talk=skill"

def my_index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]

def create_spell_list(base_text):
    text_list = list(set(list(base_text)))
    for v in remove_list:
        while v in text_list:
            text_list.remove(v)
    return text_list

def calc_minus(n):
    return n - 1

def char_start_index(base_text):
    indexies = []
    for v in remove_list:
        buf = my_index_multi(base_text, v)
        indexies.extend(buf)
    return map(calc_minus, indexies)

def main():
    text_list = create_spell_list(base_text)
    char_indeies = char_start_index(base_text)
    numbers = [idx for idx in range(10)]
    for v in itertools.permutations(numbers, len(text_list)):
        combination = zip(text_list, v)
        print(combination[0])
        break
    
    
        

if __name__ == "__main__":
    main()