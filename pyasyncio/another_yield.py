import time


def func1():
    for i in range(11):
        # 这里暂停
        yield
        print('这是我第%s次打印啦' % i)
        time.sleep(1)


def func2():
    # 这里拿到生成器对象
    g = func1()
    # 触发g
    next(g)
    for k in range(10):
        print('哈哈，我第%s次打印了' % k)
        time.sleep(1)
        next(g)


# 不写yield，下面两个任务是执行完func1里面所有的程序才会执行func2里面的程序，有了yield，我们实现了两个任务的切换+保存状态
# 这里执不执行func1()都无所谓，因为执行完就挂那儿了，真正调用的func1()的是func2()
# func1()
func2()
