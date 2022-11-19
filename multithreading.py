import threading
import time


def worker1(e):
    is_event_triggered = e.wait(3)
    print('worker 1 started')
    time.sleep(5)
    print('worker 1 ended')


def worker2(e):
    print('worker 2 started')
    while not event.is_set():
        is_event_triggered = e.wait(2)
        if is_event_triggered:
            print('doing my work after event is triggered')
        else:
            print('doing something else')
    print('worker 2 ended')


event = threading.Event()

t1 = threading.Thread(name="worker1", target=worker1, args=(event,))
t2 = threading.Thread(name="worker2", target=worker2, args=(event,))

t1.start()
t2.start()

time.sleep(7)

print('firing the event')
event.set()

print('program completed')


