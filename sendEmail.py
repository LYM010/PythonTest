#!/usr/bin/env python3
# coding:UTF-8
# https://blog.csdn.net/u011846143/article/details/78274911?locationNum=9&fps=1
import smtplib
smtpObj = smtplib.SMTP('smtp.126.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('klsmuej@126.com','901129ming')
smtpObj.sendmail('klsmuej@126.com','715555876@qq.com','Subject:Test\nThis is a test text.')
smtpObj.quit()