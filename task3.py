# -Задайте список из вещественных чисел. Напишите программу, которая найдёт
#  разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114

def difference_max_min(list):
   new_list = [round(i%1,2) for i in list if i%1 != 0]
   rezult = max(new_list) - min(new_list)
   print('%.4f' % rezult)
   return rezult
list = [1.1, 1.2, 3.1, 5.17, 10.02]
difference_max_min(list)