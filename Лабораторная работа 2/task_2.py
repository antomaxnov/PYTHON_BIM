salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
dolg = salary - spend # долг на конец первого месяца
increase_months = range(1, months) # месяцы, в которые цены растут

for num in increase_months:
    dolg += salary - spend * (1 + increase) ** num
dolg = round(dolg, 2) * (-1)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", dolg)
