"""1. Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка."""

out_f = open("out_file.txt", "w")
line=input("Введите текст  \n")
while line:
    out_f.writelines(line)
    line = input("Введите текст  \n")
    if not line:
        break
out_f.close()

"""2. Создать текстовый файл (не программно),
 сохранить в нём несколько строк, 
 выполнить подсчёт строк и слов в каждой строке."""

my_file = open("out_file.txt", "r", encoding="utf-8")
content=my_file.read()
print ("Содержание файла \n", content)

content1=my_file.readlines()
print(f'Количество строк в файле - {len(content1)}')

with open('out_file.txt', 'r', encoding="utf-8") as file:
    my_list = file.readlines()
    for i in range(len(my_list)):
        new_l = my_list[i].split()
        print(f'Количество строк в файле {len(my_list)}. В {i + 1}-ой строке {len(new_l)} слов(а)')

""" 3. Создать текстовый файл (не программно). 
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
Определить, кто из сотрудников имеет оклад менее 20 тысяч, 
вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников."""

with open('salary.txt', 'r', encoding="utf-8") as file:
    my_list = file.read().split("\n")
    sal=[]
    sum=0
    for i in range(len(my_list)):
        salary = int((my_list[i].split())[1])
        if salary<20000:
            sal.append((my_list[i].split())[0])
        sum+=salary
medium=sum/len(my_list)/12
print ("Оклад меньше 20 000 у сотрудников: ", sal)
print ("Средняя зарплата ", medium)

"""5. Создать (программно) текстовый файл, 
записать в него программно набор чисел, разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить её на экран. """

with open('filsse.txt', 'w+') as file:
    file.write(input('Введите числа через пробел: '))
    l = map(int, file.read().split())
print(sum(l))

