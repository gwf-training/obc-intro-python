# https://docs.python.org/3/library/

import time
import _thread



def process(name, wait):
    for _ in range(3):
        time.sleep(wait)
        print(f"{time.ctime(time.time())}: tread: {name}")

def main():
    print("FUNCIONES BUILT-IN")

    _thread.start_new_thread(process, ("h1", 1))
    _thread.start_new_thread(process, ("h2", 3))

    time.sleep(30)
    print("FIN!")

if __name__ == "__main__":
    main()