print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел
# import math

def nod(int1, int2):
  # Вариант 1
  # return math.gcd(int1, int2)
  
  # Вариант 2
  result_nod = 1
  for i in range(1, max(int1, int2)+1):
   if int1 % i == 0 and int2 % i == 0:
      if i > result_nod:
        result_nod = i
  return result_nod

  


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
result = nod(num1, num2)
print(f"Наибольший общий делитель двух чисел {num1} и {num2} равен {result}")
