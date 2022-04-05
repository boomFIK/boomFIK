from random import randint

game = Truenum = randint(1,100)
num = randint(1, 100)

print('Попробуй угадай число от 1 до 100')

while game:
    guess = int(input('Вааше предположение: '))

    if guess == num:
        print('Вы угадали верно!')
        game = False
    elif guess < num:
        print(f'Ответ неверный, попробуй число больше чем {guess}')
    elif guess > num:
        print(f'Ответ неверный, попробуй число меньше чем {guess}')

    

