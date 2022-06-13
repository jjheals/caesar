import string 

alphabet = string.printable

# ---------- INTERACTIVE ---------- #

method = input('\nDo you want to "decode" or "encode" text?: ')
method.lower()

# Check that method is either 'decode or 'encode'
while ((method != 'decode') and (method != 'encode')):
    method = input('\nPlease type "decode" or "encode": ')
    method.lower()

shift = int(input(f'\nWhat is the shift?: '))

# Check that shift is an integer and 1 <= integer <= 26
while ((not isinstance(shift, int)) or (not shift <= 26) or (not shift >=1)):
    shift = int(input('\nPlease enter an integer greater than 0 and less than 26: '))

origString = input(f'\nEnter the text you want to {method} with an shift of {shift}: ')


# ---------- FUNCTIONS ---------- #

# Shift the alphabet by the given shift factor
def shiftAlph(alph):
    global shift
    global alphabet 
    global method

    if method == 'decode':
        shift = shift*-1

    return alph[shift:] + alph[:shift]

# Create the new string 
def transpose():
    global origString
    global alphabet

    newString = ''
    shiftedAlph = shiftAlph(alphabet)

    for char in origString:
        newString += shiftedAlph[alphabet.index(char)]

    print(f'\nTransposed text: {newString}')
    return 

transpose()

