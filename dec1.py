def my_syper_decorator(func):
    def wrapper():
        print('начинаем работу по декорированию!')
        print('пока все идет хорошо')
        func()
        print('Заканчиваем дерорирование')
        print('Всем спасибо!')
    return wrapper
@my_syper_decorator
def privet_mir():
    print("Привет мир!")
@my_syper_decorator
def hello_world():
    print("Hello world!")

if __name__ == '__main__':
    privet_mir()
    print("-------------------------------------------")
    hello_world()

