file_name = 'byron.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    file_read = file.read()
    print(file_read)
