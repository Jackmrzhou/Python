import requests
from bs4 import BeautifulSoup
import re
import time
import increase
#嗯这个写的太繁琐。
#我已经明白减少引入increase的方法
#但是我不打算改了（还不如重写一个）
print('Input url!')
wx_url = judge_url(input())
latter_dict = {}

def judge_url(wx_url):
	if 'http://' not in wx_url:
		return 'http://' + wx_url
	return wx_url 

def download_code(url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}
	data = requests.get(url, headers = headers).content
	return data

def prase_html(html):

	soup = BeautifulSoup(html, "html.parser")	
	vote_example = re.compile("voteInfo\=\{[\S ]*\}")
	instance = re.compile("\{\"name\"\:\"\S*\"cnt\"\:[0-9]*\S*\}")
	#分析源码来写出正则来抓取数据
	vote_ = soup.getText()
	vote = re.findall(vote_example, vote_)
	getvote = re.findall(instance, str(vote))
	return getvote

def creat():
	global latter_dict
#想了很久，想不出除了用全局别的方法了。。
#喵的全局变量真的是下下策=。=
	html = download_code(wx_url)
	r = prase_html(html)
	now_dict = increase.creat_dict(r)
	change = {}
	if latter_dict:
		change = increase.difference(latter_dict, now_dict)
	latter_dict = now_dict
	return change

def main():
	change = creat()
	with open('getvote.txt','a') as fp:
		fp.write('下面表示每隔30秒的是增加的票数')
		fp.write('\n')
		fp.write(str(change))
		fp.write('\n')
		fp.write('CollectTime:' + time.strftime("%H:%M:%S"))
		fp.write('\n')
	print('Write Succeeded!')

if __name__ == '__main__':
	while True:
		time.sleep(30)
		try:
			main()
		except Exception as e:
			print('Write Failed!')