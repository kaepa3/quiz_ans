import math
import itertools
import inspect


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
    return n + 1

def start_chars(base_text):
    indexies = []
    for v in remove_list:
        buf = my_index_multi(base_text, v)
        indexies.extend(buf)
    
    points = map(calc_minus, indexies)
    char_list =[]
    for v in points:
        char_list.append(base_text[v])
    char_list.append(base_text[0])
    return char_list

def char_start_zero(vals, ngs):
    numbers = [ i[1] for i in vals if i[0] in ngs]
    return any([i == 0 for i in numbers]) 

def create_formula(text, combination):
    result_text = text
    for v in combination:
        result_text = result_text.replace(v[0], str(v[1]))    
    result_text =result_text.replace("=", "==")    
    return result_text

def main():
    text_list = create_spell_list(base_text)
    ng_char = start_chars(base_text)
    numbers = [idx for idx in range(10)]
    for v in itertools.permutations(numbers, len(text_list)):
        combination = list(zip(text_list, v))
        if char_start_zero(combination, ng_char):
            continue
        formula_text = create_formula(base_text, combination)
        if eval(formula_text) == True:
            print(formula_text)
            
if __name__ == "__main__":
    main()