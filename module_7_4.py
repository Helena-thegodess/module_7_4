# Использование %
print("В команде %(team1)s участников: %(team1_num)s!" % {"team1": "Мастера кода", "team1_num": 5})
print("В команде %(team2)s участников: %(team2_num)s!" % {"team2": "Волшебники данных", "team2_num": 6})
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!" % {"team1_num": 5, "team2_num": 6})
#Использование format()
print("Команда {0} решила задач: {1} !".format("Мастера кода", 40))
print("Команда {team2} решила задач: {score_2} !".format(team2="Волшебники данных", score_2=42))
print("{team1} решили задачи за {team1_time} с !".format(team1="Мастера кода", team1_time=10717.6))
print("{team2} решили задачи за {team2_time} с !".format(team2="Волшебники данных", team2_time=18015.2))
# Использование f-строк:
team1 = "Мастера кода"
team2 = "Волшебники данных"
team1_time = 10717.6
team2_time = 18015.2
score_1 = 40
score_2 = 42
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / tasks_total, 1)
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = "Победа команды Волшебники Данных"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = "Победа команды Мастера кода"
else:
    challenge_result = "Ничья!"
print(f"Результат битвы: {challenge_result}!")