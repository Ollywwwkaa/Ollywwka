import time
def tim(fun):
    def wrapper():
        start = time. time()
        res = fun()
        end = time.time()
        time1 = end - start
        print (f"Время выполнения {fun} : {time1: 4f} секунд")
        return res 
    return wrapper
@tim
def slow():
    for i in range(100000) :
        pass
slow()