from db_schema import schema_fields

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

def get_data_type(fields, idx):
	return list(fields[idx].values())[1]

def set_default_value(fields, idx):
	data_type = get_data_type(fields, idx)
	default_val = '""'
	if data_type == 'date':
		default_val = '"2012-06-28 22:10:19.170000"'
	elif data_type == 'int':
		default_val = '0'

	return default_val


def parse_null_val(arr_str, table_name):
	schema_fields_types = schema_fields()
	foodict = {k: v for k, v in schema_fields_types.items() if k.startswith(table_name)}
	new_val = []
	fields = list(foodict.values())[0]['fields']
	for idx, val in enumerate(arr_str):
		if val == '""':
			new_val.append(set_default_value(fields, idx))
		else:
			new_val.append(val)

	# print(new_val)
	return new_val
	# return list(map(lambda str: sub if str.strip() == '""' else str, arr_str))

# Build fields for query
def build_fields(values):
	for fields in values:
		arr_fields = [list(field.values())[0] for field in fields]
		return ', '.join(arr_fields)