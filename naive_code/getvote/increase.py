#import re
#example = re.compile("\{\"name\"\:\"\S*\"cnt\"\:[0-9]*\S*\}")
#不知用正则怎么写=。=

def creat_dict(data):
	for result in data:
		result = result.split(',')
	for i in range(0, len(result)):
		result[i] = result[i].strip('{}')
	result_list = []
	for thing in result:
		result_list += thing.split(':')
#将数据分散

	result_dict = {}
	lenth_result_list = len(result_list) 
	for i in range(0, lenth_result_list):
		if result_list[i] == '"name"':
			result_dict[result_list[i + 1]] = int(result_list[i + 3])
#创建名字和票数对应的字典。
	print(result_dict)
	return result_dict

def difference(latter_dict, now_dict):
	change = {}
	for thing in now_dict:
		change[thing] = now_dict[thing] - latter_dict[thing]
	return change
#作差后返回一个新字典
		