import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
        elif isinstance(other, str):
            return self.nickname == other


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname in self.users and user.password == hash(password):
                self.current_user = user
            return user

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(user)
            self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        search_list = []
        for video in self.videos:
            if search_word.lower() in str(video).lower():
                search_list.append(video)
        return search_list

    def watch_video(self, search_name):
        if self.current_user != None:
            for video in self.videos:
                if search_name == video.title:
                    if video.adult_mode == True and self.current_user.age >= 18:
                        while video.time_now < video.duration:
                            video.time_now += 1
                            print(video.time_now, end=' ')
                            time.sleep(1)
                        video.time_now = 0
                        print('Конец видео')
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
