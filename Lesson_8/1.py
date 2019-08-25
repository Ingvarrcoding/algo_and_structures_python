"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter

s = 'battle for glory'

def huffman_tree(s):
    freq = Counter(s)
    tree = freq.most_common()
    while len(tree) > 1:
        lt, lw = tree.pop()
        rt, rw = tree.pop()
        new_lt = [lt, rt]
        new_w = lw + rw
        index = next((i for i, tree in enumerate(tree) if tree[1] < new_w), len(tree))
        tree.insert(index, (new_lt, new_w))
    huffman_tree = tree[0][0]
    return huffman_tree

def huffman_code(tree, prefix=''):
    code_table = []
    lt, rt = tree
    if type(lt) is list:
        code_table += huffman_code(lt, f'{prefix}0')
    else:
        code_table.append((lt, f'{prefix}0'))
    if type(rt) is list:
        code_table += huffman_code(rt, f'{prefix}1')
    else:
        code_table.append((rt, f'{prefix}1'))
    return code_table

def huffman_encode(code_table, s):
    encoded_text = ''
    up_dict = dict(code_table)
    for char in s:
        encoded_text += up_dict[char]
    return encoded_text

def main():
    tree = huffman_tree(s)
    code_table = huffman_code(tree)
    encoded_text = huffman_encode(code_table, s)

    print(f'Исходный текст: {s}')
    print(f'Кодированный текст: {encoded_text}')

main()

'''
Исходный текст: battle for glory
Кодированный текст: 010101001011011000111111011011000111100011001100010000
'''