from random_word_gen_by_len import random_word_gen_by_len

def len_and_level():
    lev = int(input("please choose a game level between 1-3 where 1 is easy and 3 is hard:"))
    global game_word_len

    if lev == 1:
        game_word_len = 3
    elif lev == 2:
        game_word_len = 5
    else:
        game_word_len = 7

    print("game word len is: ", game_word_len)
    return game_word_len


def cows(guess, base, len):
    bools = 0
    hits = 0
    size = len
    guess_list = list(guess)
    base_list = list(base)

    if guess == base:
        print("Good job! you win!")
    else:
        for i in range(0, size):
            if guess_list[i] == base_list[i]:
                hits += 1
            else:
                if guess_list[i] in base_list and guess.count(guess_list[i]) == 1:
                    bools += 1
        print("Bools: ", bools)
        print("Hits: ", hits)
        play()

def play():
    user_guess = input("please type a guess: ")
    cows(user_guess, base_word, game_word_len)


len_and_level()
base_word = random_word_gen_by_len(game_word_len)
# print(base_word)
play()

input("press any key to exit")