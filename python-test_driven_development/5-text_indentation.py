#!/usr/bin/python3
# 5-text_indentation.py
""" function that prints a text with 2 new lines
after each of these characters: ., ? and : """


def text_indentation(text):
    char = {'.', '?', ':'}
    if type(text) is not str:
        raise TypeError('text must be a string')
    text_form = text.strip()
    for i, x in enumerate(text_form):
        if x in char:
            print(f'{x}\n')
        else:
            if text_form[i - 1] in char:
                continue
            if text_form[i] == ' ' and text_form[i - 1] == ' ':
                continue
            print(f'{x}', end='')
