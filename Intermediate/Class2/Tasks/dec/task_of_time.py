import datetime
import time


def show_time(func):
    def wrapper():
        current_time = datetime.datetime.now()
        print("Current time: ", current_time)
        return func()

    return wrapper


@show_time
def show_time():
    print()


show_time()


def measure_time(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        execution = (end_time - start_time) * 1000
        print("Execution time: ", execution)
        return result
    return wrapper


@measure_time
def measure_time():
    print()


measure_time()
