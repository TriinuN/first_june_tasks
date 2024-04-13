from time import sleep
import threading


def thread_function():
    print("Start")
    sleep(2)
    print("End")


if __name__ == "__main__":
    print("Main_loop: START ")
    thread = threading.Thread(target=thread_function)
    print("Main_loop: Before Running")
    thread.start()      # Start an async task that is not part of main loop
    print("Main_loop: Program is running")
    thread.join()       # Join the async task back to main loop
    print("Main_loop: Complete")
