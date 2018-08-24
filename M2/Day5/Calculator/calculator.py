#!_*_coding:utf-8_*_
# Author: Zhang Qing

import re

def verify_exp(expression):
    exp_parse = re.match(r'^[\d.+\-*/()]+$',expression)
    if not exp_parse:
        print('This expression is invalid')
        return False
    else:
        exp_params = re.split(r'[+\-*/]',expression) #不能有连续符号
        for exp_param in exp_params:
            if not exp_param:
                print('This expression is invalid')
                return False
    return True

def add_sub_cal(expression):  #加减运算
    expression = re.sub('--','+',expression)
    expression = re.sub(r'\+-', '-', expression)  #负数的加减
    expression = re.sub('^-','0-',expression)
    params = re.split('[+-]',expression)
    # for param in params:
    #     if not param:
    #         print('This expression is invalid')
    #         return
    if params.__len__() == 1:
        return  params
    symbols = re.findall('[+-]',expression)
    sum = float(params[0])
    for n in range(symbols.__len__()):
        if symbols[n] == '+':
            sum = sum + float(params[n+1])
        elif symbols[n] == '-':
            sum = sum - float(params[n+1])
    return str(sum)

def mul_div_cal(expression):   #乘除运算
    params = re.split('[*/]',expression)
    # for param in params:
    #     if not param:
    #         print('This expression is invalid')
    #         return
    if params.__len__() == 1:
        return  params
    symbols = re.findall('[*/]',expression)
    sum = float(params[0])
    for n in range(symbols.__len__()):
        if symbols[n] == '*':
            sum = sum * float(params[n+1])
        elif symbols[n] == '/':
            sum = sum / float(params[n+1])
    return str(sum)

def basic_cal(expression):  #基础四则运算，无括号优先
    while True:
        mul_div_parse = re.search(r'([\d.]*([*/]|\*-|/-)[\d.]+)+', expression)
        if not mul_div_parse:
            break
        else:
            mul_div_exp = mul_div_parse.group()
        mul_div_result = mul_div_cal(mul_div_exp)
        expression = expression.replace(mul_div_exp,mul_div_result)
    res = add_sub_cal(expression)
    return str(res)

def calculate(expression):
    while True:
        parse = re.search(r'\([^()]+\)', expression)
        if not parse:
            res = basic_cal(expression)
            return res
        parsed_exp = parse.group().strip('()')
        parsed_result = basic_cal(parsed_exp)
        expression = expression.replace(parse.group(),parsed_result)

while True:
    expression = input('Please enter the expression(enter q to exit):')
    expression = re.sub('\s+','',expression)
    if expression == 'q':
        exit()
    if not verify_exp(expression):
        continue
    print(calculate(expression))
    # print(basic_cal(expression))
