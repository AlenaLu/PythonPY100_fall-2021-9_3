BYTES_ONE_CHAR = 1
# дискета 1.44 МБ
pages = 100  # TODO ввести количество страниц
lines = 50  # TODO ввести количество строк
chars = 25  # TODO ввести количество символов в строке

total_chars = pages * lines * chars  # TODO общее количество символов в книге
total_bytes = BYTES_ONE_CHAR * total_chars  # TODO размер одной книги в байтах

disk_size = 1.44 * 1024 * 1024  # TODO размер дискеты в байтах

print(disk_size // total_bytes)  # TODO найти количество книг, которое поместится на дискете
