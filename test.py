#!/usr/bin/env python
# coding=utf-8

import urllib


def go(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print "%.2f%%" % per


url = "http://m4.biz.itc.cn/pic/new/n/95/65/Img8686595_n.jpg"
local = "f:\python2016-a\g.jpg"
urllib.urlretrieve(url, local, go)
