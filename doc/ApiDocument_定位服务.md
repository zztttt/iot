# 定位服务
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|getPosition|none|hmac-sha1|定位服务|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_gateway_position|ag-api.ctwing.cn/aep_gateway_position|
|沙箱环境|ag-api.ctwing.cn/aep_gateway_position||

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：getPosition   版本号: 20190301085737

#### 描述

定位服务

#### 请求信息

请求路径：/api/getPosition

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|cardId|QUERY|String|true|定位的物联网卡号|
|posReqType|QUERY|Long|true|返回的位置类型：1为初始位置；2为最新位置；3为最新or历史位置；7目前未用到，保留数字|


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": 0,
    "msg": "ok",
    "result": {
        "msid": "1064911702350",      //接入号，即入参cardId
        "msidType": "0",
        "positionResult": "2",        //定位平台返回的错误码，2表示定位成功
        "localTime": "20180622182523",//时间信息
        "latitudeType": "1",          //北纬1;南纬0
        "latitude": "32.042179",      //纬度值
        "longitudeType": "0",         //东经0;西经1
        "longitude": "118.737884",    //经度值
        "radius": "1",                //位置信息返回的扇区半径信息（固定值，建议忽略）
        "posour": "31"                //位置来源（请忽略）
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

