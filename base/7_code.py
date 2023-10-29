"""
Соблюдение общих норм для написания красивого кода, который легко читать и поддерживать.
"""

# 1) Соблюдение PEP8.
# 2) Длина строки — 119 символов.
# 3) Импорты отсортированы правильно, неиспользуемых импортов нет.
# 4) Отступы — 4 пробела.
# 5) Одинаковые кавычки, одинаковые методы решения одинаковых проблем.
# 6) Отсутствие закомментированного кода и стандартных комментариев.
# 7) Комментарии к функциям оформлены в виде Docstrings.
# 8) Длинные куски кода логически разделены пустыми строками, как абзацы в тексте.
# 9) Исполняемый код в .py-файлах закрыт конструкцией if __name__ == ‘__main__’
# 10) В f-строках применяется только подстановка переменных. Не применяются логические или арифметические операции.
# 11) Переменные названы в соответствии с их смыслом, по-английски, нет однобуквенных названий и транслита.


# Проектирование
# YAGNI You Aren’t Gonna Need It / Вам это не понадобится
# Неиспользуемый код удаляется, а не комментируется или висит мёртвым грузом

# DRY Don’t Repeat / Не повторяйтесь
# Не должно быть одинаковых классов / функций / больших кусков кода, делающих одно и то же

# KISS Keep It Simple, Stupid / Будь проще
# Нужно стремиться писать максимально простой и понятный код.
# Каждая функция и класс ориентированы на выполнение одной конкретной задачи

# Есть еще SOLID и DI
# но это необязательно для нашего уровня (уровень поиска первой работы)
