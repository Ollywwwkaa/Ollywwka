import time
class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        execution_time = self.end_time - self.start_time
        print(f"Время выполнения: {execution_time:.2f} сек")
        return False
    import time
with Timer():
    time.sleep(1.5)
    print("Код выполнен успешно")
try:
    with Timer():
        time.sleep(0.5)
        raise ValueError("Что-то пошло не так!")
except ValueError as e:
    print(f"Поймано исключение: {e}")