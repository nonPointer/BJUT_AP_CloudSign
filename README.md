# BJUTCloudSign

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

README [English](#English) | [中文](#中文)

## Todo

- [x] Auto fetch course information
- [x] Auto generate checkcode
- [x] Auto generate sign time
- [ ] Fetch sign history
- [ ] Custom User-Agent
- [ ] Batch sign in
- [ ] Auto generate imei

## English

### Introduction

BJUTCloudSign is a test project based on Python, it is used to auto-sign the lecture as a client of BJUT AP Sign System.

### Usage

Learn Chinese, then following the Chinese version instruction.

## 中文

### 介绍

BJUTCloudSign（北工大 AP 云签到）是一个基于 Python 的测试项目，用于 AP 课堂签到系统的远程签到。

### 使用

1. 记录签到数据包的imei字段（并非标准的手机iemi）、教室内 AP 的 mac 地址，以及 checkcode 的盐。

2. 填充以下字段。

   ```python
   studentNumber = ""
   studentName = ""
   apMacAddress = ""
   checkcodeSalt = ""
   imei = ""
   ```

3. 执行脚本实现签到。