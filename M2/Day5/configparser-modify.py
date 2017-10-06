# Author: Zhang Qing

import configparser

config = configparser.ConfigParser()
config.read('i.cfg')

# ########## 读 ##########
# secs = config.sections()
# print(secs)
# options = config.options('section1')
# print(options)
#
# item_list = config.items('section1')
# print(item_list)
#
# print(config.get('section1', 'k1'))
# print(config.getint('section1', 'k1'))

# ########## 改写 ##########
config.remove_section('section1')  #删
config.write(open('i.cfg', "w"))

config.has_section('wupeiqi')
config.add_section('wupeiqi')      #增
config.set('wupeiqi','name','wupeiqi')  #option增
config.write(open('i.cfg', "w"))

config.set('section2','k1','11111')  #改
config.write(open('i.cfg', "w"))

config.remove_option('section2','age')  #删
config.write(open('i.cfg', "w"))