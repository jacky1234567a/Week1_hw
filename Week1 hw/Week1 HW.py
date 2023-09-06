# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:58:51 2023

@author: user
"""

#請求用戶輸入身高和體重

height = float(input("請輸入你的身高(公尺):"))
weight = float(input("請輸入你的體重(公斤):"))

#使用公式來計算BMI

BMI = weight/(height**2)

#顯示計算得到的BMI(小數點後兩位)

print(f"你的BMI是:{BMI:.2f}") 