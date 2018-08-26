#!_*_coding:utf-8_*_
# Author: Zhang Qing

import re

def verify_exp(expression):
    exp_parse = re.match(r'^[\d.+\-*/()]+$',expression)
    if not exp_parse:
        print('This expression is invalid')
        return False
    else:
        # 不能有连续符号
        exp_params = re.split(r'[+\-*/]',expression)
        for exp_param in exp_params:
            if not exp_param:
                print('This expression is invalid')
                return False
    return True

#加减运算
def add_sub_cal(expression):
    # 负数的加减
    expression = re.sub('--','+',expression)
    expression = re.sub(r'\+-', '-', expression)
    expression = re.sub('^-','0-',expression)
    params = re.split('[+-]',expression)
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

#乘除运算
def mul_div_cal(expression):
    params = re.split('[*/]',expression)
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

#基础四则运算，无括号优先计算式
def basic_cal(expression):
    while True:
        # 取出乘除项，并兼容负数
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
        # 取出括号内计算式
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

