def readint(arg):
    while True:
        num = str(input(arg))
        try:
            num = int(num);
            return num
        except ValueError:
            if num == '':
                print("\033[1;31mTHE USER DIDN'T WANT TO TYPE A NUMBER\033[m")
                return 0
            print('\033[1;31mERROR, TYPE A VALID NUMBER!\033[m')


def readfloat(arg):
    while True:
        num = str(input(arg))
        try:
            num = float(num);
            return num
        except ValueError:
            if num == '':
                print("\033[1;31mTHE USER DIDN'T WANT TO TYPE A NUMBER\033[m")
                return 0
            print('\033[1;31mERROR, TYPE A VALID NUMBER!\033[m')


n = readint('Type a Integer Number: ')
m = readfloat('Type a Real Number: ')
print(f'You typed the integer number {n} and the real number {m}.')
