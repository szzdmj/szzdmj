
import base64
import os
from PIL import Image
from io import BytesIO
import urllib3
from lxml import etree
import html
import re
from bs4 import BeautifulSoup
import requests
import html2text

# blogUrl = 'szmj0.github.io'
blogUrl = 'www.shenzhouzhengdao.org'
image_directory = 'images'

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'} 

def save_base64_image(base64_str, image_dir, img_index, pre_index):
    # 提取图片数据
    header, encoded = base64_str.split(',', 1)
    # 设定图片文件名
    img_format = header.split(';')[0].split('/')[1]
    image_filename = f'image_{pre_index}_{img_index}.{img_format}'
    image_path = os.path.join(image_dir, image_filename)
    
    # 解码并存储图片到本地
    image_data = base64.b64decode(encoded)
    image = Image.open(BytesIO(image_data))
    image.save(image_path)
    return image_path

def html_to_markdown_with_images(html, image_dir, pre_index):
    # 确定图片目录存在，不存在则创建
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # 初始化html2text
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True

    # 初始化BeautifulSouput
    soup = BeautifulSoup(html, 'lxml')
    markdown_lines = []
    
    # 处理<pre>标签
    for pre_tag in soup.find_all('pre'):
        title = pre_tag.get('title', '')
        if title:
            markdown_lines.append(f'## {title}\n')

        pre_content = str(pre_tag)
        pre_soup = BeautifulSoup(pre_content, 'lxml')

        # 处理<b>
        for b_tag in pre_soup.find_all('b'):
            b_tag.replace_with(f"**{b_tag.get_text()}**")

        # 处理<br>
        for br_tag in pre_soup.find_all('br'):
            br_tag.replace_with('\n')

        # 处理<img>
        img_index = 0
        for img_tag in pre_soup.find_all('img'):

            src = img_tag.get('src', '')
            if src.startswith('data:image'):
                # 存储图片并获得文件名
                img_filename = save_base64_image(src, image_dir, img_index, pre_index)
                img_index += 1
                # 修改<img>来引用存储的图片
                img_tag.replace_with(f'![Image]({img_filename})\n')
                print(pre_index, img_index)


        # 提取文字
        plain_text = pre_soup.get_text()
        markdown_lines.append(plain_text.strip())
		
        

    return '\n'.join(markdown_lines)



def addIntro(f):
	txt = '''  
![Image](https://github.com/szmj0/update/blob/main/extras/Icon-256.jpg)
# 神州明见畅游真相精简阅读版
---
简介文字
![Image](https://github.com/szmj0/update/blob/main/extras/sjmj-fg.jpg)

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
	txt ='''
# 精选文章  	 

	'''
	f.write(txt)
	f.write("\n")
	with open('index.html', 'r+', encoding='utf-8') as file:
			html_content = file.read()
	soup = BeautifulSoup(html_content, 'html.parser')  # or 'lxml'
	articles = soup.find_all('pre')
	pre_index = 0
	for article in articles[1:]:
		pre_index += 1
		markdown_output = html_to_markdown_with_images(str(article), image_directory, pre_index)
		f.write(markdown_output)
		f.write("\n")


def addHTMLVideos(f):
	txt ='''
# 本站视频	 

	''' 
	f.write(txt)
	with open('index.html', 'r+', encoding='utf-8') as file:
			html_content = file.read()
	soup = BeautifulSoup(html_content, 'html.parser')  # or 'lxml'
	video_table = soup.find('table', id='tbPlayList')

	if video_table:

		td_elements = video_table.find_all('td')

		for td in td_elements:
			print(td.text)
	else:
		print("Table not found")

def addHTMLBooks(f):
	txt ='''
# 精彩电子书下载

'''
	f.write(txt)
	with open('index.html', 'r+', encoding='utf-8') as file:
			html_content = file.read()
	soup = BeautifulSoup(html_content, 'html.parser')  # or 'lxml'
	books_table1 = soup.find('div', id='bookpage1')
	books_table2 = soup.find('div', id='bookpage2')
	html_parser = html2text.HTML2Text()
	pageMD = html_parser.handle(books_table1.prettify()) + html_parser.handle(books_table2.prettify())
	f.write(pageMD)

def addHTMLDownloads(f):
	with open('index.html', 'r+', encoding='utf-8') as file:
		html_content = file.read()
	soup = BeautifulSoup(html_content, 'html.parser')
	# 移除所有script tag
	for script in soup.find_all('script'):
		script.decompose() 
	page = soup.find('div', id='d5')
	html_parser = html2text.HTML2Text()
	pageMD = html_parser.handle(page.prettify())
	f.write(pageMD)



if __name__=='__main__':
	f = open('README.md', 'w+')
	addIntro(f)
	#f.write('<table align="center"><tr>\n')
	#f.write('<td valign="top" width="33%" style="word-wrap: break-word;">\n')
	#f.write('\n</td>\n')
	# f.write('<td valign="top" width="33%">\n')
	# addBlogInfo(f)
	# f.write('\n</td>\n')
	#f.write('<td valign="top" width="33%" style="word-wrap: break-word;">\n')
	#f.write('\n</td>\n')
	#f.write('</tr></table>\n')
	addHTMLInfo(f)
	# addHTMLVideos(f)
	addHTMLBooks(f)
	addHTMLDownloads(f)
	addProjectInfo(f)
	addZhuanlanInfo(f)
	f.close
	with open('README.md', "r+") as f:
		encoded_text = html.escape(f.read())
	with open('README.md', "w+") as f:
		f.write(encoded_text)
