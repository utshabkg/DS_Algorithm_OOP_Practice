# What *args allows you to do is take in more arguments than the number of formal arguments that you previously
# defined. With *args, any number of extra arguments can be tacked on to your current formal parameters (including
# zero extra arguments).
def arg_func(*args):
	for arg in args:
		print(arg)


arg_func('Hello', 'Welcome', 'Geeks')


def kwarg_func(**kwargs):
	for key, value in kwargs.items():
		print("%s = %s" % (key, value))


# Driver code
kwarg_func(first='Hello', mid='Welcome', last='Geeks')
