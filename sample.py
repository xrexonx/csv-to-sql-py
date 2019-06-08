from utils import for_each, for_each_with_index, remove_char

# print("Hello world")
arr = ['asdasdasd', 'qweqwewqe']

for_each(lambda val: print(val), arr)
for_each_with_index(lambda idx, val: print(idx, val), arr)
print(remove_char('xrexonx', 'x'))

if __name__ == '__main__':
	print(__name__)