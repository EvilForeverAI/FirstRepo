# длинна списка len()
my_list = [10, 20, 30, 40, "Номер заказа", "Дата отгрузки"]
my_list1 = ["Номер заказа", "Дата отгрузки"]
print(len(my_list))
print(len([]))  # Выведет 0
print(len([1, 2, 3]))  # Выведет 3
print(len([[1, 2, 3]]))  # Выведет 1, двумерный массив
print()
print(my_list[0+1])

#print(my_list.index(15))  # распечатает индекс числа 20, если он есть в списке my_list
#print(my_list1.index('Номер заказа'))  # распечатает индекс числа 20, если он есть в списке my_list

indices = [my_list.index(col) for col in my_list1]
print(indices)