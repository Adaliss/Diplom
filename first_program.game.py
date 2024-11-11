import random


def play_game():
    guesses_made = 0
    name = input("Привет! Как тебя зовут?\n")
    number = random.randint(1, 100)
    print("Отлично, {0}, я загадал число между 1 и 100. Сможешь угадать?".format(name))

    while guesses_made < 10:
        guess = int(input("Введи число: "))
        guesses_made += 1

        if guess < number:
            print("Твое число меньше того, что я загадал.")
        elif guess > number:
            print("Твое число больше загаданного мной.")
        else:
            print("Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!".format(name, guesses_made))
            break
    else:
        print("Не угадал. Я загадал число {0}. Не теряй надежды, в следующий раз точно повезёт!".format(number))


def main():
    while True:
        play_game()
        continue_game = input("Хотите сыграть снова? (да/нет): ").strip().lower()
        if continue_game != 'да':
            print("Спасибо за игру!")
            break


if __name__ == "__main__":
    main()
