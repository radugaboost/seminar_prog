import time

def worktime(f1, f2):
    def f(string):
        initial_time = time.time()
        f1(string)
        first = time.time() - initial_time
        initial_time = time.time()
        f2(string)
        second = time.time() - initial_time
        print(f1.__name__ if first < second else f2.__name__)
    return f



def double_letter(string):
    s = set()
    for i in string:
        if string.lower().count(i) > 1 and i != ' ':
            s.add(i)
    return len(s)      

def count_duplicates(string):
    return len([ch for ch in (set(string.lower())) if string.lower().count(ch)>1])


funcion = worktime(count_duplicates, double_letter)
funcion('aaaBBnn')