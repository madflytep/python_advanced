import time
from threading import Thread
from multiprocessing import Process
from functools import wraps

# Функция для измерения времени выполнения другой функции
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} выполнена за {end_time - start_time} секунд.")
        return end_time - start_time
    return wrapper

# Функция для вычисления n-го числа Фибоначчи
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@timer
def sync_fibonacci(n):
    for _ in range(10):  # Вызов функции 10 раз
        fibonacci(n)

@timer
def thread_fibonacci(n):
    threads = []
    for _ in range(10):  
        thread = Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:  
        thread.join()

@timer
def process_fibonacci(n):
    processes = []
    for _ in range(10):  
        process = Process(target=fibonacci, args=(n,))
        processes.append(process)
        process.start()
    
    for process in processes: 
        process.join()


n = 35

sync_time = sync_fibonacci(n)
thread_time = thread_fibonacci(n)
process_time = process_fibonacci(n)

results = f"""
Результаты времени выполнения функции вычисления числа Фибоначчи для n=35:

1. Синхронный запуск: {sync_time}.
2. Запуск через потоки (threading): {thread_time}.
3. Запуск через процессы (multiprocessing): {process_time}.

Примечание: Время выполнения для методов с использованием потоков и процессов может значительно отличаться от синхронного запуска из-за накладных расходов на управление потоками/процессами и специфики выполнения Python кода.
"""

file_path = "hw_4/artifacts/4_1.txt"
with open(file_path, "w") as file:
    file.write(results)

file_path
