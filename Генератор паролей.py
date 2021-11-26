from random import *

igits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous_characters = 'il1Lo0O'
chars = ''

number_of_passwords = int(input('Сколько паролей необходимо сгенерировать? '))
length_of_passwords = int(input('Введите длинну пароля: '))
digit_in_password = input('Включать ли цифры в пароль? (д = да, н = нет) ')
uppercase_password = input('Включать ли прописные буквы? (д = да, н = нет) ')
lowercase_letters_password = input('Включать ли строчные буквы? (д = да, н = нет) ')
password_symbols = input('Включать ли символы? (д = да, н = нет) ')
ambiguous_characters_password = input('Исключать ли неоднозначные символы? (д = да, н = нет) ')

if digit_in_password.lower() == 'д':
    chars += igits
if uppercase_password.lower() == 'д':
    chars += uppercase_letters
if lowercase_letters_password.lower() == 'д':
    chars += lowercase_letters
if password_symbols.lower() == 'д':
    chars += punctuation
if ambiguous_characters_password.lower() == 'н':
    chars += ambiguous_characters


def generate_password(symbols, length):
    password = sample(symbols, length)
    return password
for i in range(number_of_passwords):
    print(''.join(generate_password(chars, length_of_passwords)))