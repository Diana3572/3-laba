
#3.1
n = int(input("Введите количество слов: "))

result = ""

for i in range(n):
    a = input("Введите слово: ")
    result += a + " "

print("Результат:", result.strip())


#3.2
result = ""

a = input("Введите слово: ")
while a != "stop":
    result += a + " "
    a = input("Введите слово: ")

print("Результат:", result.strip())


#3.3
a = "ф"  # Определяем редкую букву

while True:
    word = input("Введите слово: ")  # Пользователь вводит слово

    if a in word:  # Проверяем, содержит ли слово редкую букву
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

# 3.4
import random

correct_answers = 0
wrong_answers = 0

while wrong_answers < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    answer = input(f"{num1} + {num2} = ")

    if int(answer) == num1 + num2:
        print("Правильно!")
        correct_answers += 1
    else:
        print("Ответ неверный")
        wrong_answers += 1

print(f"Игра кончена. Правильных ответов: {correct_answers}")