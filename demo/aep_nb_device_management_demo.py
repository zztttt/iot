#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_nb_device_management

if __name__ == '__main__':
    result = apis.aep_nb_device_management.BatchCreateNBDevice('dFI1lzE0EN2', 'xQcjrfNLvQ', '{}')
    print('result='+str(result))

