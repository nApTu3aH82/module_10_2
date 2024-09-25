# -*- coding: utf-8 -*-
import threading
from time import sleep
from threading import Thread


class Knight(Thread):
    res = []

    def __init__(self, names, power):
        self.names = names
        self.power = power
        Knight.res.append([names, power])
        super().__init__()

    def run(self):
        print(f'{self.names}, на нас напали!')
        count_warriors = 100
        count_day = 0
        while count_warriors != 0:
            count_day += 1
            count_warriors -= self.power
            print(f'{self.names} сражается {count_day} день (дня)..., осталось {count_warriors} воинов')
            sleep(1)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
threads = []
for count in range(2):
    thread = Knight(Knight.res[count][0], Knight.res[count][1])
    thread.start()
    threads.append(thread)
#
for thread in threads:
    thread.join()

print('Все битвы закончились')
