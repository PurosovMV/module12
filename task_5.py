print('Задача 5. Текстовый редактор')

# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы 
# и любой цифры в тексте (а не только буквы Ы как раньше).
# 
# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
# 
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
# 
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
# 
# Количество цифр 0: 2
# Количество букв л: 1


def count_letters(input_str):
  search_for_digit = input("Какую цифру ищем? ")
  search_for_letter = input("Какую букву ищем? ")
  cnt_digits = input_str.count(search_for_digit)
  cnt_letters = input_str.count(search_for_letter)
  print(f"Количество цифр {search_for_digit}: {cnt_digits}\nКоличество букв {search_for_letter}: {cnt_letters}")


input_str = input("Введите текст: ")
count_letters(input_str)
  
  