import time
from threading import Thread


def countdown(n: int) -> None:
    '''countdown'''
    for i in range(n):
        print(n - i - 1, 'left')
        time.sleep(1)


# создание потока для вызова функции с аргументами
t1 = Thread(target=countdown, name='CountdownThread', args=(3,))
t1.start()
print(t1.ident, t1.name)
# t1.join()  # Wait until the thread terminates
# t1.is_alive()  # Return whether the thread is alive

############################################################

import time
from threading import Thread


# наследуемся от класса Thread
class CountdownThread(Thread):
    '''CountdownThread'''
    def __init__(self, n: int):
        super().__init__(name='CountdownThread')
        self.n = n

    # автоматически вызывается методом start
    def run(self) -> None:
        '''run'''
        for i in range(self.n):
            print(self.n - i - 1, 'left')
            time.sleep(1)


t2 = CountdownThread(3)
t2.start()
print(t2.ident, t2.name)

############################################################

# блокировки

import time
from threading import Lock

l = Lock()
l.acquire()
# do some with locked resource
l.release()

############################################################

# отправка сигналов между потоками

# метод wait блокирует вызывающий поток,
# пока другой не вызовет метод notify

# поток может разблокироваться без notify - spurious wakeup

from collections import deque
from threading import Condition

q = deque()
c = Condition()


def producer() -> None:
    '''producer'''
    while True:
        # залочиваем ресурс
        c.acquire()
        # делаем что-то с залоченным ресурсом
        q.append('next task')
        # сообщаем, что блокировку можно снять
        c.notify()
        # разлочиваем ресурс
        c.release()


def consumer() -> None:
    '''consumer'''
    while True:
        c.acquire()

        while not q:
            c.wait()

        data = q.popleft()
        c.release()
        # обрабатываем данные из FIFO очереди
        print(data)


############################################################


# читаем сообщения из соединения и кладем их на обработку
def readAndPut(connection, lock, queue):
    '''readAndPut'''
    try:
        while True:
            lock.acquire()
            msg = connection.readMsg()
            lock.release()
            queue.put(msg)
    except Exception:
        lock.release()
        readAndPut(connection, lock, queue)


# чтоб не заморачиваться в lock, используем "менеждер контекста"
# он лочит и освобождает ресурсы за нас
def readAndPutCtx(connection, lock, queue):
    '''readAndPut'''
    try:
        while True:
            with lock:
                msg = connection.readMsg()

            queue.put(msg)
    except IOError:
        readAndPutCtx(connection, lock, queue)


readAndPutThread = Thread(target=readAndPutCtx, args=())
readAndPutThread.start()

############################################################

# используйте модуль queue только в многопоточном режиме
from queue import Queue, LifoQueue, PriorityQueue

# в однопоточном режиме deque достаточно
# т.к. нет лишних вызовов acquire/release
from collections import deque

# пример работы с FIFO очередью из модуля queue


def worker(q):
    '''worker'''
    # блокировка, ожидает следующий элемент из очереди
    data = q.get()
    # обрадотка данных из очереди
    print(data)
    # нотифает о выполнении обработки
    q.task_done()


def master(q):
    '''master'''
    for item in ['task1', 'task2']:  # source()
        q.put(item)

    # блокировка, ожидет пока вся очередь не будет обработана
    q.join()


############################################################

# futures - Promises in Python

from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=4)
# запуск одиночного future
executor.submit(print, 'hello')
# запуск массива futures
list(executor.map(print, ['hello', 'world']))
# остановка future
executor.shutdown()

# поддерживает "менеждер контекста"
with ThreadPoolExecutor(max_workers=4) as executor:
    future = executor.submit(sorted, [30, 10, 50, 20, 40])

# методы доступа к состоянию
future.running()
future.done()
future.cancelled()
# методы доступа к результату
future.result()
future.exception()
# зарегистрировать колбек после выполения
future.add_done_callback(print)

############################################################

# пример неблокирующей работы с вводом/выводом
# менеждер контекста + файловая система + сетевые запросы

from urllib.request import urlretrieve
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    with open('./urls.txt', 'w') as urls:
        for url in urls:
            executor.submit(urlretrieve, url)

############################################################

# async/await in Python + async for, async with ...

import asyncio


async def echo(source, target) -> None:
    '''echo'''
    while True:
        line = await source.readline()

        if not line:
            break

        target.write(line)


loop = asyncio.get_event_loop()
server = asyncio.start_server(echo, port=3000)
loop.create_task(server)

try:
    loop.run_forever()
finally:
    server.close()
    loop.close()

############################################################

# мультипроцессинг - порождаем много "питонов" :),
# чтобы обойти проблему GIL

import time
from multiprocessing import Process, Pipe


def countdown2(n: int) -> None:
    '''countdown2'''
    for i in range(n):
        print(n - i - 1, 'left')
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=countdown2, args=(5,))
    p.start()
    print(p.name, p.pid, p.daemon)
    p.join()
    print(p.exitcode)


# общение между процессами через Pipe
# альтернатива - через Queue или JoinableQueue из модуля queue
def sendMsg(receiver, message: str) -> None:
    '''sendMsg'''
    receiver.send(message)


parent, child = Pipe()
p = Process(target=sendMsg, args=(child, 'ping'))

p.start()
parent.recv()
p.join()

############################################################

# для параллельного запуска разных job
# можно использовать также пакет joblib,
# который работает как мультипоточном, так и в мультипроцессорном режиме
# (backend='threading') or (backend='multiprocessing')

# pip install joblib
from joblib import Parallel, delayed
