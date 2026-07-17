"""
超卖/卖票
"""
import threading
import time


def sale_ticket():
    global ticket_num

    # while ticket_num > 0:
    #     lock.acquire()
    while True:
        with lock:
            if ticket_num <= 0:
                lock.release()
                break
            time.sleep(0.01)
            ticket_num -= 1
            print(f"{threading.current_thread().name}卖了一张票，还剩余{ticket_num}张票")

if __name__ == '__main__':
    ticket_num = 100

    lock = threading.Lock()

    threads = [threading.Thread(target=sale_ticket, name="窗口" + str(i)) for i in range(1, 4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

