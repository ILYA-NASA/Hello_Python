# 3: Создайте модуль main.py.
# Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1),
# так и отдельные функции из модуля.

from example1 import create_dir, delete_dir
from example2 import rand_element


create_dir()
delete_dir()
print(rand_element([1, 2, 3, 4, 5]))