import day10

def day14_1(input):
    used = 0
    for n in range(128):
        to_hash = '{}-{}'.format(input, n)
        hex = day10.day10_2(256, to_hash)
        #bin = ''
        for char in hex:
            for char in hex_to_bin(char):
                if char == '1':
                    used += 1
    return used

def hex_to_bin(char):
    dict = {
        'f': '1111',
        'e': '1110',
        'd': '1101',
        'c': '1100',
        'b': '1011',
        'a': '1010',
        '9': '1001',
        '8': '1000',
        '7': '0111',
        '6': '0110',
        '5': '0101',
        '4': '0100',
        '3': '0011',
        '2': '0010',
        '1': '0001',
        '0': '0000',
    }
    return dict[char]
