from urllib.request import urlopen
#https://www.cnblogs.com/angle6-liu/p/10579983.html
# link = 'http://www.baidu.com/' 
link = 'http://192.168.3.7:24000'
try:
    f = urlopen(link)
    print(f)
    html = f.read()
    print(html)
    htmldecoded = html.decode()
    print(htmldecoded)
except Exception as ex:
    print('*** Failed to get Html! ***\n\n' + str(ex))