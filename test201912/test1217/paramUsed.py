
# def function(arg):
#     print(arg, type(arg))
# function(1)


# def function(*args):
#     print(args, type(args))
# function(1)


# def function(x, y, *args):
#     print(x, y, args, type(args))
# function(1, 2, 3, 4, 5)


# def function(**kwargs):
#     print(kwargs, type(kwargs))
# function(a=2)


#
# def function(**kwargs):
#     print(kwargs, type(kwargs))
# function(a=1, b=2, c=3)


# 注意点：参数arg、*args、**kwargs三个参数的位置必须是一定的。必须是(arg,*args,**kwargs)这个顺序，否则程序会报错。
# arg单个参数；*args将参数打包成tuple；**kwargs将参数打包成dict
def function(arg, *args, **kwargs):
    print(arg, args, kwargs)
function(6,7,8,9,a=1, b=2, c=3)
