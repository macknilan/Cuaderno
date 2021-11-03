# EJEMPLO *args, **kwargs

def my_func(*args, **kwargs):
    print("hello world", args, kwargs)


my_func("abc", 1, "sk", [4, 5, 6], abc=123)

# print ('hello world', ('abc', 1, 'sk', [4, 5, 6]), {'abc': 123})
