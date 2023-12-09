# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44  # объем дискеты в Мб
page = 100
line = 50
sym = 25
volume_sym = 4 # байты на один символ

volume *= (1024 ** 2) # объем дискеты в байтах
sym_lot = page * line * sym # символов в книге
volume_book = sym_lot * volume_sym
book_lot = round(volume / volume_book)

print("Количество книг, помещающихся на дискету:", book_lot)
