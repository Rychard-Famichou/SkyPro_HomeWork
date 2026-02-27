# 📊 Банковские операции — обработка и маскирование

## 📖 Описание проекта

Проект предназначен для обработки банковских транзакций.

Реализованы функции для:

- фильтрации операций по статусу
- сортировки операций по дате
- фильтрации по валюте
- получения описаний операций
- генерации номеров банковских карт
- маскирования номеров карт и счетов

Проект реализован на Python 3.10+.

---

## 📂 Структура проекта

project/
│
├── src/
│ ├── processing.py
│ ├── masks.py
│ └── generators.py
│
├── tests/
│ └── test_*.py
│
└── README.md

---

## ⚙️ Установка

1. Клонировать репозиторий:

`git clone https://github.com/Rychard-Famichou/SkyPro_HomeWork.git`

2. Установить зависимости:

`poetry install`
`pip install pytest`

3. Запустить тесты:

`pytest`

---

# 🛠 Использование функций

---

## 1️⃣ filter_by_state

Фильтрует транзакции по статусу.

`filter_by_state(data: list, state: str = "EXECUTED") -> list`

**Пример:**
```
from processing import filter_by_state

result = filter_by_state(transactions, "EXECUTED")
print(result)
```

## #️⃣ sort_by_date

Сортирует транзакции по дате.

```
sort_by_date(data: list, reverse: bool = True) -> list

reverse=True — по убыванию

reverse=False — по возрастанию
```

**Пример:**
```
from processing import sort_by_date

sorted_data = sort_by_date(transactions)
print(sorted_data)
```

## 3️⃣ filter_by_currency

Генератор, возвращающий транзакции в указанной валюте.

`filter_by_currency(transactions: list, currency_code: str)`

**Пример:**
```
usd_transactions = filter_by_currency(transactions, "USD")

for transaction in usd_transactions:
    print(transaction)
```
_Если транзакций нет:_

`Транзакции в заданной валюте отсутствуют`

_Если список пустой:_

`Введены не верные данные.`

## 4️⃣ transaction_descriptions

Генератор описаний транзакций.

`transaction_descriptions(transactions: list)`

**Пример:**
```
descriptions = transaction_descriptions(transactions)

for desc in descriptions:
    print(desc)
```

## 5️⃣ card_number_generator

Генератор номеров карт в формате: XXXX XXXX XXXX XXXX

`card_number_generator(start: int, end: int)`

**Пример:**
```
for card in card_number_generator(1, 3):
    print(card)
```
_Результат_:
```
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
```

## 6️⃣ get_mask_card_number

Маскирует номер карты.

`get_mask_card_number(card_number: str) -> str`

**Пример:**

`get_mask_card_number("1596837868705199")`

_Результат_:

`1596 83** **** 5199`

## 7️⃣ get_mask_account

Маскирует номер счета.

`get_mask_account(account_number: str) -> str`

**Пример:**

`get_mask_account("12345678901234567890")`

_Результат:_

`**7890`

### 📝 Декоратор логирования log
## 8️⃣ log

Декоратор для автоматического логирования выполнения функции.

**Позволяет фиксировать:**

- успешное выполнение функции
- возникшие ошибки
- входные параметры при ошибке

**Логи могут выводиться:**

- в консоль (по умолчанию)
- в файл в папке logs/

### 📌 Сигнатура

`log(filename: str | None = None)`

**Параметры:**

- `filename` — имя файла для записи логов
  - если передан → лог записывается в logs/<filename>
  - если не передан → лог выводится в консоль

### ✅ Поведение при успешном выполнении

В лог записывается:

`имя_функции ok`

**Пример:**
```
from decorators import log

@log(filename="mylog.txt")
def add(x, y):
    return x + y

add(2, 3)
```
В файл `logs/mylog.txt` будет записано:

`add ok`

### ❌ Поведение при ошибке

Если функция вызывает исключение, в лог записывается:

`имя_функции error: ТипОшибки. Inputs: (args), {kwargs}`

После логирования ошибка пробрасывается дальше.

**Пример:**
```
@log()
def divide(x, y):
    return x / y

divide(5, 0)
```
Вывод в консоль:

`divide error: ZeroDivisionError. Inputs: (5, 0), {}`

### 📂 Где создаётся файл

Файл логов автоматически создаётся в папке:

`project/logs/`

Путь вычисляется относительно корня проекта, независимо от директории запуска.

Если папки `logs` нет — она создаётся автоматически.

## 🧪 Тестирование

Проект покрыт тестами с использованием pytest.

**Запуск:**

`pytest`

Состояние тестирования от 25.02.2026:
+ покрытие 97%
+ отчёт: htmlcov/index.html
