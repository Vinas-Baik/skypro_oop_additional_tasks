"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
from time import perf_counter, sleep


class Timer:

    def __init__(self):
        self.elapsed_time = perf_counter()
        print(f'Init - {self.elapsed_time}')

    def __enter__(self):
        self.elapsed_time = perf_counter()
        print(f'Enter - {self.elapsed_time}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = perf_counter() - self.elapsed_time
        print(f'Exit - {self.elapsed_time}')

timer = Timer()
with timer:
    sleep(3)

print(f"Execution time: {timer.elapsed_time}")
