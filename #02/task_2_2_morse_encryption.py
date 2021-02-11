import re


'''
    Numbers in the Morse code have the following pattern:

    all digits consist of 5 characters;
    the number of dots at the beginning indicates the numbers from 1 to 5, the remaining characters are dashes;
    starting with the number 6, each dot is replaced by a dash and vise versa.
    Write the function morse_number() for encryption of a number in a three-digit format in Morse code.

'''

        
def  morse_number(var):

    pattern = re.search(r'^([0]|[1-5]|[6-9]{1})-?([0]|[1-5]|[6\
                          -9]{1})-?([0]|[1-5]|[6-9]{1})$', var)

    script = ''

    counter = 1

    while counter <= 3:

        pt = int(pattern.group(counter))

        if pt == 0:
            script = script + abs(pt-5) * '-' + ' '

        elif 0 < pt < 6:
            script = script + pt * '.'
            script = script + (5 - pt) * '-'
            script = script + ' '

        elif 5 < pt < 10:
            script = script + (pt - 5) * '-'
            script = script + abs(pt - 10) * '.'
            script = script + ' '

        else:
            pass

        counter += 1

    return script.strip()


var = '784'
print(morse_number(var))
