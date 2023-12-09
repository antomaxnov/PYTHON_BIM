numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

skip = 4
lot = len(numbers)
left_total = sum(numbers[:skip])
right_total = sum(numbers[skip + 1:])

average = (left_total + right_total) / lot

numbers[skip] = average
print("Измененный список:", numbers)
