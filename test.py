#!/usr/bin/python
# encoding=utf-8
import sys
sys.path.append('..')
import apis.aep_device_status
import datetime
import json

if __name__ == '__main__':
  #  result = apis.aep_device_status.QueryDeviceStatus('GPvZaoo8eU2', '31nw67zu6O', '{"productId":"15011727","deviceId":"9a0aff904d3a4f3382388eaf0d3b39de","datasetId":"humidity_data"}')
  #  print('result='+str(result))

 #   result = apis.aep_device_status.QueryDeviceStatusList('GPvZaoo8eU2', '31nw67zu6O', '{"productId":"15011727","deviceId":"9a0aff904d3a4f3382388eaf0d3b39de"}')
 #   print('result='+str(result)+'\n')
 #   print(result.decode('utf-8'))

 #   result = apis.aep_device_status.getDeviceStatusHisInTotal('GPvZaoo8eU2', '31nw67zu6O', '{}')
 #   print('result='+str(result))

    # one dat duration
    now = datetime.datetime.now()
    last = now - datetime.timedelta(days=1)
    print(now.timestamp())
    # 13-timestamp
    nowts = int(now.timestamp()*1000)
    lastts = int(last.timestamp()*1000)
    print(nowts)
    print(lastts)


    '''
    request body
    productId
    deviceId
    begin_timestamp
    end_timestamp
    page_size       希望获取的 page_size 条记录
    page_timestamp，希望获取的 page_size 条记录的最近时间，第一次调用可以置空，会返回最后一条记录的ts，作为第二次调用的 page_timestamp即是第二次调用的最近记录时间戳
    '''
    param = '"productId":"15011727","deviceId":"9a0aff904d3a4f3382388eaf0d3b39de",\
            "begin_timestamp":"{0}","end_timestamp":"{1}",\
            "page_size":{2},"page_timestamp":"{3}"'.format(lastts, nowts, 10, '')
    body = '{'+param+'}'
    print(body)

    ''' mark
    timestamp length
    python          10    1606045690.159878
    begin_timestamp 13    1606043129251
    end_timestamp   13    1606029974699
    page_timestamp  17    16060299746991318
    '''

    result = apis.aep_device_status.getDeviceStatusHisInPage('GPvZaoo8eU2', '31nw67zu6O', body)
    print('result='+str(result))

    jsonR = json.loads(result)
    #print(jsonR['page_timestamp'][5]['timestamp'])

    # python use 10-timestamp
    lastResponeseTS = datetime.datetime.fromtimestamp(int(jsonR['page_timestamp'])/10000000)

    print(lastResponeseTS)