import pdb


def fn(x):
	if type(x) == str:
		pdb.set_trace()
	print x*5

if __name__ == "__main__":
	fn("2")
