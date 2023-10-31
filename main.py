# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def encode(en_password):
    new_pass = []
    for ii in range(len(en_password)):
        new_digit = int(en_password(ii)) + 3
        new_pass.append(new_digit)
        return new_pass
def decode(de_password):
    old_pass = []
    for ii in range(len(de_password)):
        old_digit = int(de_password(ii)) - 3
        old_pass = old_pass + old_digit
        return old_pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        print('Please enter an option:', end=' ')
        option = int(input())
        if option == 1:
            print('Please enter your password to encode:', end=' ')
            en_password = input()
            encoded = encode(en_password)
            print('Your password has been encoded and stored!')
        elif option == 2:
            password = decode(encoded)
            input(print(f'The encoded password is ', {encoded}, ', and the original password is ', {password}))
        elif option == 3:
            break


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
