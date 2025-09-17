li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turns = 0

def board(li):
    print(f' {"-" * 12}')
    for i in range(9):
        print(f'| {li[i]}', end = ' ')
        if (i + 1) % 3 == 0:
            print('|', '\n', '-' * 12)

def get_valid_input():
    while True:
        num_str = input("Enter a number from 1 to 9: ")
        if not num_str.isdigit():
            print('⚠️  Invalid input, please enter a number ⚠️')
            continue
        num = int(num_str)
        if num not in range(1, 10):
            print('⚠️  Invalid input, please enter a number between 1 and 9 ⚠️')
            continue
        if li[num - 1] in ['X', 'O']:
            print('⚠️  This number is already taken, choose another one ⚠️')
            continue
        return num

def play(li, num):
    global turns
    if turns % 2 == 0:
        li[num - 1] = 'X'
    else:
        li[num - 1] = 'O'
    turns += 1

board(li)
for i in range(9):
    num = get_valid_input()
    play(li, num)
    board(li)
    if turns >= 5:
        if (li[0] == li[1] == li[2]) or (li[3] == li[4] == li[5]) or (li[6] == li[7] == li[8]) or \
           (li[0] == li[3] == li[6]) or (li[1] == li[4] == li[7]) or (li[2] == li[5] == li[8]) or \
           (li[0] == li[4] == li[8]) or (li[2] == li[4] == li[6]):
            if turns % 2 == 1:
                print('🎉 (X) WINS!🎉')
            elif turns % 2 == 0:
                print('🎉 (O) WINS!🎉')
            break
    if turns == 9:
          print('🤝 DRAW!🤝')
          break