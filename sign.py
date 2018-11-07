# coding=utf-8
import requests

headers = {
	'Content-Type': 'text/html;charset=UTF-8',
}

# data = open('data.txt', 'rb')
data = open('data.txt', 'rb')
r = requests.post("http://39.106.53.215:8080/ap/sign/signOn?", headers=headers, data=data)

print(r.text)