#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_gateway_position

if __name__ == '__main__':
    result = apis.aep_gateway_position.getPosition('dFI1lzE0EN2', 'xQcjrfNLvQ')
    print('result='+str(result))

