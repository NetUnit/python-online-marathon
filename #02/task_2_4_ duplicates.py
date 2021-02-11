import re


'''
    As input data, you have a string that consists of words that have duplicated characters at the end of it.

    All duplications may be in the next format:

    wordxxxx
    wordxyxyxy
    wordxyzxyzxyz
    , where x, xy or xyz repeated ending of the word

Using re module write function pretty_message() that remove all duplications

'''


def pretty_message(data):
    
    # single item
    data = re.sub(r'([a-z])\1+', r'\1', data)

    # 2 doubles
    data = re.sub(r'([a-z])(.*)\2+', r'\1\2', data)

    # the rest
    data = re.sub(r'(..*)\1+', r'\1', data)

    return data


data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceaceaceace repeatedededed groupssss of symbolssss"
#ata = "Another input data string"
print(pretty_message(data))