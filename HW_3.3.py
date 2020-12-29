def my_func(a, b, c):
    global number_list, max_number, max_summ
    number_list = list((a, b, c)) #переводим три введенных числа в список
    max_number = max(number_list) #находим максимальное число
    number_list.remove(max_number) #удаляем максимальное число, в списке остается два числа
    max_summ = max_number + (max(number_list)) # определяем максимальное число из оставшихся двух и складываем
    return max_summ

first_number = int(input("1 число:  "))
second_number = int(input("2 число:  "))
third_number = int(input("3 число:  "))
print("Сумма = ", my_func(first_number, second_number,third_number))
