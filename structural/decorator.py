from functools import wraps


def make_blink(function):
	"""decorator function"""
	@wraps(function)
	def decorator(*args, **kwargs):
		ret = function(*args, **kwargs)
		return '<blink>' + ret + '</blink>'

	return decorator


@make_blink
def hello_world(name):
	"""Original function"""
	return 'Hello '+ name

print(hello_world('vysakh'))	