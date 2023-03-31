from datetime import date
today_date = date.today()

with open('list.json') as file:
    task = file.read()

print('здравствуйте, что пожелаете:')
print('вывести все задачи')
print('вывести все задачи на сегодня')
print('внести новую задачу')
print('удалить задачу')

command = input()

if command == ('вывести все задачи'):
    print(task)
elif command == ('вывести все задачи на сегодня'):
    print(task)