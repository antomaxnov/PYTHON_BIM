list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

lot = len(list_players)
mid_right_list = lot // 2 # номер первого игрока второй команды

team_1 = list_players[:mid_right_list]
team_2 = list_players[mid_right_list:]

print(team_1)
print(team_2)

# TODO Разделите участников на две команды
