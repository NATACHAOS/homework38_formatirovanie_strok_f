# Соперничество двух команд


# Команда 1 Мастера кода
team1_name = 'Мастер кода'
team1_num = 6

# Команда 2 Волшебники данных
team2_name = 'Волшебники данных'
team2_num = 6

# Решили задач Команда 1 Мастера кода
score1 = 40

# Решили задач Команда 2 Волшебники данных
score2 = 42

# Время
team1_time = 1552.512

# Время
team2_time = 2153.31451

# Всего решено задач
tasks_total = 82

# Среднее время решения задачи
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

# Вывод на консоль с использованием %
print(('В команде %r' %(team1_name) + ' ' + 'участников: %d' %(team1_num - 1)))
print('Итого сегодня в командах участников: %d' %(team1_num) + ' ' + 'и %d' %(team2_num - 1) + '!')
print('\n')

# Вывод на консоль с использованием format()
print("Команда '{}' решила задач: {}".format(team2_name, score2))
print("'{}' решили задачи за {} c.".format(team2_name, team2_time))
print('\n')

# Вывод на консоль с использованием f-строк
print(f'Команды решили {score1} и {score2} задач')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу')