from lxml import html
import requests
import os
#page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
sessionID = "4255ef36512d781d33b3bbc858ddc4f3";
cmdString = "curl -s 'http://192.168.1.254/index.cgi?active%5fpage=9143&active%5fpage%5fstr=page%5fevent&req%5fmode=1&mimic%5fbutton%5ffield=onchange%3a+category%5fdropdown%2e%2e&request%5fid=529478445&button%5fvalue=category%5fdropdown' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36 Vivaldi/1.1.453.59' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Referer: http://192.168.1.254/index.cgi?active%5fpage=9143&active%5fpage%5fstr=page%5fevent&req%5fmode=1&mimic%5fbutton%5ffield=submit%5fbutton%5flogin%5fsubmit%3a+%2e%2e&request%5fid=529478445&button%5fvalue=' -H 'Cookie: rg_cookie_session_id=" + sessionID + "' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' > output.xml"
os.system(cmdString)
file = open('output.xml','r')
string = file.read()
tree = html.fromstring(string)
cells = tree.xpath('//td[@class="bt_border"]/text()')
#This will create a list of buyers:
#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')
#print 'Buyers: ', buyers
#print 'Prices: ', prices

numberOfRows = len(cells) / 2
#print "numberOfRows : " + str(numberOfRows)
row = numberOfRows
while row > 0:
	#print "row : " + str(row)
	decodedString = cells[(row - 1) * 2] + ", " + cells[((row - 1) * 2) + 1]
	decodedString = decodedString.encode('utf8')
	print decodedString
	row -= 1
