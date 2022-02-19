from datetime import datetime
import turtle
import turtle
# ex.1
'''def decorator(fn):
    def wrapper():
        return repr(fn())
    return wrapper

@decorator
def line(quote='Eeey, Boss!'):
    return quote

print(line())'''

# ex.2
'''def functions(num:int):
    fn = [*range(6)]

    def square(size: int):
        t = turtle.Turtle()
        for _ in range(4):
            t.forward(50)
            t.right(90)

    ff = [print, input, lambda : range(5, 0, -1), lambda x: x*3 if type(x) == str else print('Ahaha'), lambda :datetime.now().strftime("%d/%m/%Y %H:%M:%S"), square]
    return dict(zip(fn, ff))[num]'''

#functions(1)('Hello, world')
#functions(5)(50)

#ex.5
'''def len_word_sorted(text:str) -> str:
    return ' '.join((sorted(text.split(), key=lambda x: len(x))))

t = \'На Хабре множество раз обсуждалась тема декораторов, однако, на мой взгляд, данная статья (выросшая из одного вопроса на stackoverflow) описывает данную тему на\'

print(len_word_sorted(t))'''

#ex.6
'''def len_word_sorted(text:str) -> str:
    return ' '.join((sorted(text.split(), key=lambda x: len(x), reverse=True)))

t = \'На Хабре множество раз обсуждалась тема декораторов, однако, на мой взгляд, данная статья (выросшая из одного вопроса на stackoverflow) описывает данную тему на\'

print(len_word_sorted(t))'''

# advanced_decorator1
'''def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print('Look, what I\'ve got:', arg1, arg2)
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print('My name is ', first_name, last_name)

print_full_name('Gleb', 'Denisov')'''

# advanced_decorator2

'''def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3
        return  method_to_decorate(self, lie)
    return wrapper

class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayyourage(self, lie):
        print('I am %s, what\'ve you thought?' % (self.age + lie))

L = Lucy()
L.sayyourage(-3)'''

# advanced_decorator3
'''def a_decorator_passing(fn):
    def wrapper(*args, **kwargs):
        print('Has anything been passed into me?')
        print(args)
        print(kwargs)
        return fn(*args, **kwargs)
    return wrapper

@a_decorator_passing
def function_with_no_arguments():
    print('Pyton is cool, no argument here')

function_with_no_arguments()

@a_decorator_passing
def function_with_named_arguments(a,b,c, platypus='...sure, why not?'):
    print('Do %s,%s sand %s love platypuses? %s' % (a,b,c, platypus))


function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")

@a_decorator_passing
def funcion_with_arguments(a,b,c):
    print(a, b, c)

funcion_with_arguments(1, 2, 3)

class Mary(object):

    def __init__(self):
        self.age = 31

    @a_decorator_passing
    def sayyourage(self, lie=-3):
        print('I am %s, what\'ve you thought?' % (self.age + lie))

M = Mary()
M.sayyourage()'''
# advanced_decorator3
def decorator_maker():
    print('''Я создаю декораторы! Я буду вызван только раз: когда ты попросишь меня создать тебе декоратор.''')
    def my_decorator(func):
        print('Я - декоратор! Я буду вызван только раз: в момент декорирования функции.')
        def wrapped():
            print('''Я - обёртка вокруг декорируемой функции. 
                      Я буду вызвана каждый раз когда ты вызываешь декорируемую функцию.                          Я возвращаю результат работы декорируемой функции.''')
            return func()
        print('Я возвращаю обёрнутую функцию.')

        return wrapped

    print("Я возвращаю декоратор.")
    return my_decorator

new_decorator = decorator_maker()

@new_decorator
def decorated_function():
    print("Я - декорируемая функция.")

decorated_function()

