def game():
    
    progress = True
    word = ['orange']
    lifes = 3


    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speach(list_to_string_convert(template))
    while progress:
        user_guess = user_input()
        template = build_template(template, word_in_play, user_guess)
        guessed = list_to_string_convert(template)
        print_result(guessed)
        progress = check_win(guessed)

        if not check_mistake(word_in_play, user_guess):
            print(f'Осталось {lifes} попытки')
            lifes = check_attempt(lifes)

        if lifes == 0:
            lose_speach()
            break

        if not progress:
            win_speech()

def lose_speech():
    print('вы проиграли!')

def win_speech():
    print('вы выйграли!')

def check_attempt(life):
    """
input: life - int
output: int, life -= 1
"""
    return lifes - 1
    


def check_mistake(w, g):
    """
input: w - word_in_play (string), g - user_input (string)
    output: bool, checks if user guess is wrong
    if no such g in w, return False, else True
    """
    
    flag = False
    for i in w:
        flag = True
    return flag
  

            
            

def check_win(g):
    """
input: g - template (string)
output: bool, if no '_' in g return False, else True
"""
    for l in g:
        if l == '_':
            return True
    return False

def print_result(g):
    """
input: g - template (string)
output: retorn None, used as just built-in function print(g)
"""
    print(f'Результат: {g}')
    

def build_template(t, w, g=''):
    """
input: t - template (list), w - word (string), g - guess (string)
output: t - template (list) with replaced characters in template
if character in word == guess:
'character'
else:
'_'
"""
    for i in range(len(w)):
        if t[i] == '_':
             if w[i] == g:
                 t[i] = w[i]
             else:
                t[i] = '_'
    return t
       

def user_input():
    """
output;
return str, built-in input() function
"""
    return input('Введите букву: ')


def welcome_speach(t):
    """"
input: t - template (string)
output: return None, used as just built-in function print()
"""
    print(f'''
Добро пожаловать в игру - hangman 2000
Ваша задача угадать загаданое слово за несколько попыток,
иначе вас ждет расплата!
Загаданое слово состоит из {len(t)} букв {t}
''')
    

def start_template(w):
    """
input: w - string (word)
output: replace all chars in string '_',
return replaced chars as string with length w == t
"""
    t = []
    for l in w:
        t.append('_')
    return t
        

def list_to_string_convert(t):
    """
input: t - template (list)
output: s - list converted to spring
"""
    s = ''
    return s.join(t)
    
def get_word(w):
    """
input: w - list witch strings (words)
output: for now: first element in list as string
TODO:  random string from list
"""
    return w[0]
game()



