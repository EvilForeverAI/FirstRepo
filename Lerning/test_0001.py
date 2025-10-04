list = []
while True:
    input_word = input("Введите элемента для добавления в список: ")
    list.append(input_word)
    if input_word == "Стоп":
        break
print(list)