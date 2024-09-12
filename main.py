print("Приветствую на викторине по теме Кухни всего мира")
right = 0

print("Вопрос номер один:Кто придумал эчпочмак? ")
user_answer = input()
if user_answer == "Тюркские племена":
    print("Правильно")
    right = right + 1
else:
    print("Неправильно")

print("Луковый суп — это блюдо какой кухни?")
user_answer = input()
if user_answer == "Французcкой":
    print("Правильно")
    right = right + 1
else:
    print("Неправильно")

print("Где родина начос?")
user_answer = input()
if user_answer == "Мексика":
    print("Правильно")
    right = right + 1
else:
    print("Неправильно")

print("Как называются китайские пельмени?")
user_answer = input()
if user_answer == "Гедза":
    print("Правильно")
    right = right + 1
else:
    print("Неправильно")

print("В национальную кухню какой страны входят драники?")
user_answer = input()
if user_answer == "Белорусскую":
    print("Правильно")
    right += 1
else:
    print("Неправильно")

print("Поздравляю вы прошли викторину! Ваше количество правильных ответов,", right, ",спасибо за игру!")