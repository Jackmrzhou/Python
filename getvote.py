import requests
from bs4 import BeautifulSoup
import re
import time

print('Input url!')
wx_url = input()

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

def main():
	html = download_code(wx_url)
	r = prase_html(html)
	with open('getvote.txt','a') as fp:
		fp.write(str(r))
		fp.write('\n')
		fp.write('CollectTime:' + time.strftime("%H:%M:%S"))
		fp.write('\n')
	print('Write Succeeded!')

if __name__ == '__main__':
	while True:
		time.sleep(30)
		main()