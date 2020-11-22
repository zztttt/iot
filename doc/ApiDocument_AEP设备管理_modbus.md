# AEP设备管理_modbus
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|UpdateDevice|none|hmac-sha1|modbus更新设备信息|
|CreateDevice|none|hmac-sha1|modbus创建设备|
|QueryDevice|none|hmac-sha1|modbus获取单个设备详情|
|QueryDeviceList|none|hmac-sha1|modbus批量获取设备信息|
|DeleteDevice|none|hmac-sha1|modbus删除设备|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_modbus_device_management|ag-api.ctwing.cn/aep_modbus_device_management|
|沙箱环境|ag-api.ctwing.cn/aep_modbus_device_management||

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：UpdateDevice   版本号: 20200404012440

#### 描述

modbus更新设备信息

#### 请求信息

请求路径：/modbus/device

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true||
|deviceId|QUERY|String|true||

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "deviceName": "string",
  "productId": 0
}

描述：
deviceName: 设备名称，必填
productId: 产品ID，必填

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "string",
  "result": {}
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

### API名称：CreateDevice   版本号: 20200404012437

#### 描述

modbus创建设备

#### 请求信息

请求路径：/modbus/device

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "deviceName": "string",
  "deviceSn": "string",
  "productId": 0
}

描述：
deviceName: 设备名称，必填
deviceSn: 设备编号,必填
productId: 产品ID，必填

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
	"code": 0,
	"msg": "ok",
	"result": {
		"deviceId": "89e920fa0eda47a89f04f52a88b17146",
		"deviceName": "test003",
		"tenantId": "300",
		"productId": 10003304,
		"deviceSn": "ddd"
	}
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

### API名称：QueryDevice   版本号: 20200404012435

#### 描述

modbus获取单个设备详情

#### 请求信息

请求路径：/modbus/device

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|deviceId|QUERY|String|true||
|productId|QUERY|Long|true||


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "deviceSn": "4444",//string，设备编号
    "deviceId": "100054604444",//string，设备id
    "deviceName": "4444",//string，终端名称
    "tenantId": "10007903",//string，租户id
    "productId": 10005460,//Integer，产品id
    "firmwareVersion": "",//string，版本信息
    "deviceStatus": 2,//Integer，设备状态 0:已注册，1：已激活，2：已注销
    "createTime": 1555557239000,//Timestamp，创建时间
    "updateTime": 1555557274000,//Timestamp，修改时间
    "activeTime": 1555557243000,//Timestamp，激活时间
    "logoutTime": 1555557274000,//Timestamp，注销时间
    "netStatus": 2,//设备在线状态
    "onlineAt": 1555557243483,//Long，设备最后上线时间
    "offlineAt": 1555557244923,//Long，设备最后下线时间
    "productProtocol": 16//设备所在产品协议：16.modbus协议
  }
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

### API名称：QueryDeviceList   版本号: 20200404012428

#### 描述

modbus批量获取设备信息

#### 请求信息

请求路径：/modbus/devices

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|productId|QUERY|Long|true||
|searchValue|QUERY|String|false|设备名称，设备编号，设备Id|
|pageNow|QUERY|Long|false||
|pageSize|QUERY|Long|false||


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "pageNum": 1,
    "pageSize": 1,
    "total": 3,
    "list": [
      {
       "deviceSn": "4444",//string，设备编号
       "deviceId": "100054604444",//string，设备id
       "deviceName": "4444",//string，终端名称
       "tenantId": "10007903",//string，租户id
       "productId": 10005460,//Integer，产品id
       "firmwareVersion": "",//string，版本信息
       "deviceStatus": 2,//Integer，设备状态 0:已注册，1：已激活，2：已注销
       "createTime": 1555557239000,//Timestamp，创建时间
       "updateTime": 1555557274000,//Timestamp，修改时间
       "activeTime": 1555557243000,//Timestamp，激活时间
       "logoutTime": 1555557274000,//Timestamp，注销时间
       "netStatus": 2,//设备在线状态
       "onlineAt": 1555557243483,//Long，设备最后上线时间
       "offlineAt": 1555557244923,//Long，设备最后下线时间
       "productProtocol": 16// 设备所在产品协议：16.modbus协议
      }
    ]
  }
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

### API名称：DeleteDevice   版本号: 20200404012425

#### 描述

modbus删除设备

#### 请求信息

请求路径：/modbus/device

请求方法：DELETE

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|productId|QUERY|Long|true||
|deviceIds|QUERY|String|true||


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "string",
  "result": {}
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

