import re
import requests
import time

url = "http://www.xicidaili.com/wn/1"
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'}


ip1 = 'the ip address is : 1.2.3.4'
ip2 = 'Leon"s ip is: 10.16.10.10'
ip3 = 'check this:255.245.255.255'

ipRegex = re.compile(r'((25[0-5]|2[0-4]\d|(1\d{2})|([1-9]?\d))\.){3}(25[0-5]|2[0-4]\d|(1\d{2})|([1-9]?\d))')

ip_a = ipRegex.search(ip1).group()
ip_b = ipRegex.finditer(ip1 + ip2 + ip3)

res = requests.get(url, headers=headers)
lineRegex = re.compile(r'<td>\d{2,5}</td>')
ports = lineRegex.findall(res.text, re.S)
ips = ipRegex.finditer(res.text, re.S)
ipList = []

for ip in ips:
    ipList.append(ip.group())

for i in range(len(ipList)):
    ipList[i] = ":".join((ipList[i], re.search(r'\d{2,5}', ports[i]).group()))
    time.sleep(0.5)
    print(ipList[i])
