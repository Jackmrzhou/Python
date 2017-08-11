from bs4 import BeautifulSoup
import requests

tieba_url = 'http://' + input('Please input url:\n')
print('\n')

def get_html(tieba_url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}
	html = requests.get(tieba_url, headers = headers).content
	return html

def parse_html(html):
	soup = BeautifulSoup(html, 'html.parser')
	pic_url_list = []
	inner = soup.find_all('cc')
	for pic in inner:
		pic_detail = pic.find_all('img')
		for pic_url in pic_detail:
			pic_url_list.append(pic_url.get('src'))
	#喵的我实现的太不优雅了！
	return pic_url_list

def page(html):
	soup = BeautifulSoup(html, 'html.parser')
	pages = soup.find('li', attrs={'class': 'l_pager pager_theme_5 pb_list_pager'}).find_all('a')
	page_list = []
	for page in pages:
		page_list.append(page.get('href'))
	return page_list

def main():
	count = 1
	html = get_html(tieba_url)
	page_list = page(html)
	page_count = len(page_list)
	
	list_urls = parse_html(html)
	for i in range(0, page_count - 2):
		the_html = get_html('http://tieba.baidu.com' + page_list[i])
		list_urls += parse_html(the_html)
	
	for pic_urls in list_urls:
		file = 'pic//' + str(count) + '.jpg'
		count += 1
		picture = requests.get(pic_urls).content
		with open(file, 'wb') as fp:
			fp.write(picture)
		
	print('Totally download %s pictures' %count)

if __name__ == '__main__':
	main()
	print('Succeed!')
