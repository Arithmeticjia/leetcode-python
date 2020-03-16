import ctypes


def execute_time(func):
    from time import time

    # 定义嵌套函数，用来打印出装饰的函数的执行时间
    def wrapper(*args, **kwargs):
        # 定义开始时间
        start = time()
        # 执行函数
        func_return = func(*args, **kwargs)
        # 定义结束时间
        end = time()
        # 打印方法名称和其执行时间
        print('{}() execute time: {}s'.format(func.__name__, end - start))
        # 返回func的返回值
        return func_return

    # 返回嵌套的函数
    return wrapper


ll = ctypes.cdll.LoadLibrary
# lib = ll("main.so")
lib = ll("fbi.so")


# num1 = ctypes.c_int(1)

@execute_time
def fbi_cpp(n):
    print(lib.fbi(n))
    print(lib.main(n))


@execute_time
def fbi_python_run(n):
    fbi_python(n)


def fbi_python(n):
    if n == 1 or n == 2:
        return 1
    return fbi_python(n - 1) + fbi_python(n - 2)


if __name__ == "__main__":
    fbi_cpp(2)
    # fbi_python_run(40)
