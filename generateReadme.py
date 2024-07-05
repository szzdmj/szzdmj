# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re

blogUrl = 'https://szmj0.github.io'

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'} 

def addIntro(f):
	txt = '''  
<p align="center">
  <img src="https://github.com/szmj0/update/blob/main/extras/Icon-256.jpg"/>
</p>	
<p align="center">
  <img src="https://github.com/szmj0/update/blob/main/extras/sjmj-fg.jpg"/>
</p>

<p align="center">test</p>  


''' 
	f.write(txt)

def addProjectInfo(f):
	txt ='''
### 开源项目  
- [app](https://github.com/szmj0/update/blob/main/extras/szmj-v6.9.2024010901.apk)神州明见6.9	
   
[查看更多](https://github.com/szmj0/Publish)	 

	''' 
	f.write(txt) 

def addZhuanlanInfo(f):
	txt ='''
### 专栏  
- [SZMJ WEB](https://github.com/szmj0/update/blob/main/extras/SZZD_PC/szmjweb.3.0.zip)
  
- ……

	''' 
	f.write(txt) 


def addBlogInfo(f):  
	http = urllib3.PoolManager(num_pools=5, headers = headers)
	resp = http.request('GET', blogUrl)
	resp_tree = etree.HTML(resp.data.decode("utf-8"))
	# html_data = resp_tree.xpath(".//div[@class='article-item-box csdn-tracking-statistics']/h4") 
	html_data = resp_tree.xpath(".//article[@class='blog-list-box']")

 

if __name__=='__main__':
	f = open('README.md', 'w+')
	addIntro(f)
	f.write('<table align="center"><tr>\n')
	f.write('<td valign="top" width="33%">\n')
	addProjectInfo(f)
	f.write('\n</td>\n')
	f.write('<td valign="top" width="33%">\n')
	addBlogInfo(f)
	f.write('\n</td>\n')
	f.write('<td valign="top" width="33%">\n')
	addZhuanlanInfo(f)
	f.write('\n</td>\n')
	f.write('</tr></table>\n')
	f.close 

