users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

log_session = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}

lot = len(users)
users_set = set(users)
unique = len(users_set)

log_session["Общее количество"] = lot
log_session["Уникальные посещения"] = unique

print(log_session)