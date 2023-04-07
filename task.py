import os
clear = lambda: os.system('cls')
clear()

from datetime import date
import json
today_date = date.today().strftime('%d-%m-%Y')

# print (today_date)   #❗

with open('list.json', encoding='utf-8') as file:
    tasks = json.load(file)

from datetime import date
today_date = date.today()

print('здравствуйте, что пожелаете:')
print('1. вывести все задачи')
print('2. вывести все задачи на сегодня')
print('3. внести новую задачу')
print('4. удалить задачу')
print('5. закончить')

command = ('1')
while command != ('закончить') and command != ('5'):

    command = input()

    if command == ('вывести все задачи') or command == ('1'):
        for task in tasks:
            print(task['task'])

    elif command == ('вывести все задачи на сегодня') or command == ('2'):
        for task in tasks:
            if task['date'] == today_date:
                print(task['task'])

    elif command == ('внести новую задачу') or command == ('3'):
        task = input('Bведите задачу: ')
        date =input('Bведите (не обязательно) на какое число (год полностью)(числа через тире): ')
        task_and_date = {'task': task, 'date': date }
        tasks.append(task_and_date)
        with open('list.json', 'w') as f:
            json.dump(tasks, f)

    elif command == ('удалить задачу') or command == ('4'):
        print('задачи:')
        for task in tasks:
            print(task['task'])
            print(task['date'])
        delete_task = input('Bведите задачу: ')
        delete_date = input('Bведите (если есть) на какое число: ')
        delete = {'task': delete_task, 'date': delete_date}
        try:
            tasks.remove(delete)
        except ValueError:
            print('неверные данные')
        with open('list.json', 'w') as f:
            json.dump(tasks, f)
    
    elif command != ('закончить') and command != ('5'):
        print('неверные данные')

    print(' ')

print('до свидание')