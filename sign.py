# coding=utf-8
import requests
import hashlib
import json
import time
import sys

# Parameters
studentNumber = ""
studentName = ""
apMacAddress = ""
checkcodeSalt = ""
imei = ""


# Global
baseURL = "http://39.106.53.215:8080/ap/"
locationURL = "ap/getLocation"
courseURL = "ap/getCourse"


def getLocation(apMacAddress):
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
	}
	r = requests.post(baseURL + locationURL, headers=headers,data=str("mac=" + apMacAddress))


def getCourse(apMacAddress):
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
	}
	r = requests.post(baseURL + courseURL, headers=headers, data=("mac=" + apMacAddress))
	r.encoding = 'utf-8'
	json_dict = json.loads(r.text)
	json_dumps = json.dumps(json_dict['t'], ensure_ascii=False)
	json_dict = json.loads(json_dumps)
	return json_dict[0]


def getCheckcode(studentNumber):
	checkcode = hashlib.md5((studentNumber + checkcodeSalt).encode("utf-8")).hexdigest()
	return checkcode


def getTime():
	currentTime = time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime(time.time()))
	return currentTime


def getSign():
	resp = getCourse(apMacAddress)

	headers = {
		'Content-Type': 'text/html;charset=UTF-8',
	}
	signData = {
		"checkcode":(str)(getCheckcode(studentNumber)),
		"courseid":(int)(resp['id']),
		"courselocation":(str)(resp['location']),
		"coursename":(str)(resp['coursename']),
		"coursetime":(str)(resp['begintime']),
		"imei":(str)(imei),
		"signtime":(str)(getTime()),
		"sname":(str)(studentName),
		"sno":(str)(studentNumber),
		"teachername":(str)(resp['teachername'])
	}
	signData = json.dumps(signData)
	r = requests.post("http://39.106.53.215:8080/ap/sign/signOn?", headers=headers, data=signData)
	print(r.text)
	

if __name__ == "__main__":
	getSign()