# import math
# x = input()
# def isinteger(x):
#  return isinstance(x, int)
# print(isinstance(x, int))
# if isinteger(x) == True:
#   print( math.factorial(x))
# else:
#   print('Error')
import math
def calculate_factorial(n):
    return math.factorial(n)
def main():
    while True:
        user_input = input("Введите положительное целое число: ")
        try:
            number = int(user_input)
            if number < 0:
                print("Ошибка: Введите положительное целое число.")
                continue
            factorial_result = calculate_factorial(number)
            print(f"Факториал числа {number} равен {factorial_result}.")
            break
        except ValueError:
            print(
                "Ошибка: Ввод должен быть целым числом. Пожалуйста, попробуйте снова."
            )
if __name__ == "__main__":
    main()
