import time


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and user.password == password:
                self.current_user = user
                print('Пользователь существует')

    def register(self, nickname, password, age):
        for us in self.users:
            if us.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                break
        else:
            self.users.append(User(nickname, password, age))

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in list(args):
            for v in self.videos:
                if video == v:
                    break
            else:
                self.videos.append(video)

    def get_videos(self, world):
        list_video_world = []
        for i in self.videos:
            if world in i:
                list_video_world.append(i)
        return list_video_world

    def watch_video(self, name_films):
        if self.current_user != None:
            #Найти видео по запросу
            for video in self.videos:
                if name_films in video:
                #Проверка на 18+
                    if video.adult_mode == True:
                        if self.current_user.age >= 18:
                            #Показать Видео
                            count_movies = 1
                            while count_movies <= video.duration:
                                #Остановить видео на данной секунде на 1 сек
                                if video.time_now == count_movies:
                                    print(f'Остановка видео на {count_movies} сек')
                                    time.sleep(1)
                                print(count_movies, end=' ')
                                count_movies +=1
                            print('Конец видео')
                        else:
                            print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        # Показать видео не 18+
                        count_movies = 1
                        while count_movies <= video.duration:
                            if video.time_now == count_movies:
                                print(f'Остановка видео на {count_movies} сек')
                                time.sleep(1)
                            print(count_movies, end=' ')
                            count_movies += 1
                        print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f'{self.title}'

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item.lower() in self.title.lower()


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)

    def __repr__(self):
        return f'{self.nickname}'
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')