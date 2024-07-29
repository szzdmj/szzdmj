
import urllib3
from lxml import etree
import html
import re
from bs4 import BeautifulSoup
import requests


# blogUrl = 'szmj0.github.io'
blogUrl = 'www.shenzhouzhengdao.org'

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'} 

def addIntro(f):
	txt = '''  
![N|Solid](https://github.com/szmj0/update/blob/main/extras/Icon-256.jpg)
# 神州明见畅游真相精简阅读版 	
---
简介文字
![N|Solid](https://github.com/szmj0/update/blob/main/extras/sjmj-fg.jpg)

''' 
	f.write(txt)

def addProjectInfo(f):
	txt ='''
# 开源项目  
- [app](github.com/szmj0/update/blob/main/extras/szmj-v6.9.2024010901.apk)神州明见6.9	
[查看更多](github.com/szmj0/Publish)	 

	''' 
	f.write(txt) 

def addZhuanlanInfo(f):
	txt ='''
# 专栏  
- [SZMJ WEB](github.com/szmj0/update/blob/main/extras/SZZD_PC/szmjweb.3.0.zip)
- [list2.txt](szzdmj.github.io/github-page-test/list2.txt)
- [dtw](j.mp/ddw2288)
- ……

	''' 

# add list2.txt
	list2_filename = 'list2.txt'	
	with open(list2_filename, "r+") as l:
		data = l.read()
	list2_text = '''
**list2.txt:**      
---
{data}
---


'''.format(data=data)	

	f.write(txt) 
	f.write(list2_text)

def addBlogInfo(f):  
	http = urllib3.PoolManager(num_pools=5, headers = headers)
	resp = http.request('GET', blogUrl)
	resp_tree = etree.HTML(resp.data.decode("utf-8"))
	# html_data = resp_tree.xpath(".//div[@class='article-item-box csdn-tracking-statistics']/h4") 
	html_data = resp_tree.xpath(".//article[@class='blog-list-box']")

def addHTMLInfo(f):
	f.write('# 精选文章')
	with open('index.html', 'r', encoding='gbk') as file:
    		html_content = file.read()
	soup = BeautifulSoup(html_content, 'html.parser')  # or 'lxml'
	articles = soup.find_all('pre')
	for article in articles[1:]:
		title = article.get('title')
		body = article.get_text()
		# articles_dict.append((title, body))
		txt = '''
### {title}
{body}
---
		'''.format(title=title, body=body)
		f.write(txt)
	# print(articles_dict)

if __name__=='__main__':
	f = open('README.md', 'w+')
	addIntro(f)
	#f.write('<table align="center"><tr>\n')
	#f.write('<td valign="top" width="33%" style="word-wrap: break-word;">\n')
	addProjectInfo(f)
	#f.write('\n</td>\n')
	# f.write('<td valign="top" width="33%">\n')
	# addBlogInfo(f)
	# f.write('\n</td>\n')
	#f.write('<td valign="top" width="33%" style="word-wrap: break-word;">\n')
	addZhuanlanInfo(f)
	#f.write('\n</td>\n')
	#f.write('</tr></table>\n')
	addHTMLInfo(f)
	f.close 
