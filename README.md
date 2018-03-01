# Решатель квадратных уравнений

Скрипт позволяет найти корни квадратного уравнения прям вот так "Вжууух"
И вуаля.

# Как использовать

Функция get_roots принимает три параметра типа int или float. 
Возвращает кортеж с корнями квадратного уравнения при заданных параметрах.

Пример использования:
```python
from quadratic_equation import get_roots
print(get_roots(1,2,-3))
```
Output:
```bash
(-3.0, 1.0)
```

# Как запустить тесты

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
