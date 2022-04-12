
decoder_table = {
         '84': 'A',
        '161': 'A',
        '102': 'B',
        '108': 'B',
         '90': 'C',
        '143': 'C',
         '99': 'D',
        '101': 'D',
        '109': 'E',
        '171': 'E',

        '121': 'F',
        '150': 'F',
         '88': 'G',
        '100': 'G',
         '91': 'H',
        '163': 'H',
        '112': 'I',
        '194': 'I',
         '72': 'J',
         '94': 'J',

         '87': 'K',
        '130': 'K',
        '144': 'L',
        '158': 'L',
        '103': 'M',
        '117': 'M',
         '69': 'N',
         '81': 'N',
         '75': 'O',
        '120': 'O',

         '58': 'P',
        '111': 'P',
        '133': 'Q',
        '180': 'Q',
         '86': 'R',
        '192': 'R',
        '104': 'S',
        '125': 'S',
        '115': 'T',
        '190': 'T',

         '77': 'U',
        '173': 'U',
        '123': 'V',
         '95': 'V',
        '142': 'W',
        '183': 'W',
         '97': 'X',
        '105': 'X',
        '155': 'Y',
        '182': 'Y',

         '73': 'Z',
        '116': 'Z',
         }

msg_to_decode = '14477991041157514269' + \
                '142109101691091049984155' + \
                '1251129712112086115182'

# decode message, brute force

print()
print(f'Decoding message: "{msg_to_decode}"')
print()

msg = ''
index = 0
while index < len(msg_to_decode):
    print('Decoding message fragment:', f'({msg_to_decode[index:index+3]})')
    for key in sorted(decoder_table.keys()):
        length_of_key = len(key)
        msg_fragment = msg_to_decode[index: index + length_of_key]
        #print('Trying key:', key, 'on "' + msg_fragment + '"')
        if key == msg_fragment:
            # found it, break out of loop and try next part of message
            print('FOUND LETTER:', key, decoder_table[key])
            msg += decoder_table[key]
            index += length_of_key
            break
print()
print('Decoded message:', msg)
print()
