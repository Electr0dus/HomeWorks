from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        print(f'{self.name}, на нас напали!', flush=True)

    def run(self):
        count_enem = 100
        count_day = 0
        while count_enem != 0:
            count_enem -= self.skill
            count_day += 1
            print(f'{self.name}, сражался {count_day} день(дня)..., осталось {count_enem} воинов.', flush=True)
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {count_day} дней!', flush=True)


knihgt1 = Knight("Sir Lancelot", 10)
knihgt2 = Knight("Sir Galahad", 20)
knihgt1.start()
knihgt2.start()
knihgt1.join()
knihgt2.join()
print('Все битвы закончились!', flush=True)
