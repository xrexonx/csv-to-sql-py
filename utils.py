
# Sample usage:
# for_each(lambda val: print(val), ['asdasdasd', 'qweqwewqe'])
def for_each(fn, array):
	[fn(val) for val in array]

# Sample usage:
# for_each_with_index(lambda idx, val: print(idx, val), ['asdasdasd', 'qweqwewqe'])
def for_each_with_index(fn, array):
	[fn(idx, val) for idx, val in enumerate(array)]

remove_char = lambda str, char: str.replace(char, '')
# def remove_char(str, char):
	# return str.replace(char, '')

def parse_csv_null_val(arr_str, sub):
	return list(map(lambda str: sub if str == '' else str, arr_str))