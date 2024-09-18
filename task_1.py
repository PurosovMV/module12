print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N 
# и выводит сумму всех чисел от 1 до N включительно.
# 
# Пример работы программы:
# Введите число: 5
# 
# Я знаю, что сумма чисел от 1 до 5 равна 15

def summa_n(num):
  total_sum = 0
  for i in range(1,num + 1):
    total_sum += i
  return total_sum

input_num = int(input("Введите число: "))
total_sum = summa_n(input_num)
print(f"Я знаю, что сумма чисел от 1 до {input_num} равна {total_sum}")