# BJUTCloudSign

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

README [English](#English) | [中文](#中文)

## English

### Introduction

BJUTCloudSign is a test project based on Python, it is used to auto-sign the lecture as a client of BJUT AP Sign System.

### Usage

1. Capture the traffic of AP Sign client.

2. Decode the traffic and fill following fields.

   ```json
   {
   	"checkcode":"",
   	"courseid":,
   	"courselocation":"",
   	"coursename":"",
   	"coursetime":"hh:mm-hh:mm",
   	"imei":"",
   	"signtime":"yyyy-mm-dd:hh:mm:ss",
   	"sname":"",
   	"sno":"",
   	"teachername":""
   }
   ```

2. Save the json into `data.txt`.
3. Edit the `signtime` before execution.
4. Execute the script.

## 中文

### 介绍

BJUTCloudSign（北工大 AP 云签到）是一个基于 Python 的测试项目，适用于 AP 云签到系统的远程签到。

### 使用

#### Python

1. 抓取 AP 签到的数据包。

2. 解码并填充以下字段。

   ```json
   {
   	"checkcode":"",
   	"courseid":,
   	"courselocation":"",
   	"coursename":"",
   	"coursetime":"hh:mm-hh:mm",
   	"imei":"",
   	"signtime":"yyyy-mm-dd:hh:mm:ss",
   	"sname":"",
   	"sno":"",
   	"teachername":""
   }
   ```

3. 保存 Json 至 `data.txt`。

4. 在每次签到前修改签到时间字段。

5. 执行脚本实现签到。