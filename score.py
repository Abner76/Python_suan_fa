#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Abner Han 
# time:2019/7/20

def score():
    while True:
        Maths = int(input("Please input your Maths' score:"))
        if Maths >=0 and Maths <= 100:
            break
        else:
            print("Please try again!!(0~100)")
    while True:
        English = int(input("Please input your English's score:"))
        if English >=0 and English <= 100:
            break
        else:
            print("Please try again!!(0~100)")
    while True:
        History = int(input("Please input your History's score:"))
        if History >= 0 and History <= 100:
            break
        else:
            print("Please try again!!(0~100)")
    return Maths, English, History

def judge_score(m, e, h):
    if m < 75:
        m_c = "Bad"
    elif m < 85:
        m_c = "Good"
    else:
        m_c = "Great"

    if e < 80:
        e_c = "Bad"
    elif e < 90:
        e_c = "Good"
    else:
        e_c = "Great"

    if h < 70:
        h_c = "Bad"
    elif h <78:
        h_c = "Good"
    else:
        h_c = "Great"

    return m_c, e_c , h_c

def total_score(m, e, h):
    total = m*0.8 + e*1.1 + h*1.1
    t = float("%.1f" % total)
    print("Total is {}".format(total))
    return t

def judge_total(total):
    if total >= 270:
        t_c = "A+"
    elif total >= 240:
        t_c = "A"
    elif total >= 210:
        t_c = "B+"
    elif total >= 190:
        t_c = "B"
    else:
        t_c = "C"
    print("YOUR LEVEL is {}".format(t_c))

def snd_msg(math, m_c, english, e_c, history, h_c):
    print("Your Math score is {0}, level is {1}".format(math, m_c))
    print("Your Math score is {0}, level is {1}".format(english, e_c))
    print("Your Math score is {0}, level is {1}".format(history, h_c))

if __name__ == "__main__":
    m, e, h, = score()
    m_c, e_c, h_c = judge_score(m, e, h)
    snd_msg(m, m_c, e, e_c, h, h_c)
    total = total_score(m, e, h)
    judge_total(total)
