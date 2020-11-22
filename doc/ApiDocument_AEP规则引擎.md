# AEP规则引擎
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|saasCreateRule|none|hmac-sha1|SAAS规则引擎创建|
|saasQueryRule|none|hmac-sha1|SAAS规则查询|
|saasUpdateRule|none|hmac-sha1|更新SAAS规则引擎|
|saasDeleteRuleEngine|none|hmac-sha1|SAAS规则删除|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_rule_engine|ag-api.ctwing.cn/aep_rule_engine|
|沙箱环境|ag-api.ctwing.cn/aep_rule_engine||

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：saasCreateRule   版本号: 20200111000503

#### 描述

SAAS规则引擎创建

#### 请求信息

请求路径：/api/v2/rule/sass/createRule

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "dataLevel": 0,
  "description": "测试add",
  "ruleForwardInfos": [
    {
      "forwardConfig": {
        "content": "{\"test\":\"%a%\"}",
        "url": "http://127.0.0.1:9090/test"
      },
      "forwardType": "HTTP",
      "operatorType": "01"
    }
  ],
  "ruleStreams": [
    {
      "productId": "10003561",
	"deviceId":"",
	"deviceGroupId":null,
      	"ruleStr": "select aa,cc from ruleengine_10106316_10003561 where aa = 1",
	"dataLevel":0
    }
  ],
  "ruleType": "1000",
  "userId": "ljtest"
}
  ruleId:修改、删除时必填，新增规则时，此参数为空

描述:
dataLevel:规则数据类型:0-产品级别;1-设备级别；2-设备分组级别[*必填]；组合规则只支持设备级别。
ruleType:规则类型；1000：简单规则，2000：组合规则
userId：用户ID[*必填]
description:规则的描述信息, 长度不超过160位的字符串[*必填]
ruleStreams：规则信息[*必填][{   
     ruleStr:规则内容，即sql。不能包含特殊字符*，修改、新增时必填,
		具体详看下面SQL描述   
	 productId:产品ID[*必填]		
	 deviceId：设备ID,可选;当dataLevel为1时则必填。
	 deviceGroupId：设备分组ID,可选;当dataLevel为2时则必填,类型为Integer型;
	 dataLevel:子数据流规则类型:0-产品级别;1-设备级别；2-设备分组级别；可选；当dataLevel填写时规则按照此定义的规则类型进行规则处理，未填写时按照上一级配置的级别处理。	
     
}]
ruleForwardInfos：JSON数组，可选[
     {
         ruleForwardId:修改规则涉及推送修改时必填，新增推送时，此参数为空
         operatorType:操作类型：“01”：新增（配合新增规则使用），
		      “10”：修改（配合修改规则使用），“00”：删除（配合修改规则使用）
         forwardType:推送类型，目前仅支持HTTP，新增、修改推送时，必填；
		     删除推送时，此参数为空
         forwardConfig:JSON格式
	 {
            url:推送地址，必填，http的url路径,例如: http://rule.ctwind.cn/test/api
            content:推送内容，必填.
            参数格式: JSON
            参数模板：配置发送给应用的消息体的定义；所填的数据全部以body的方式传递。
                      参数模板是HTTP接口请求的参数部分，应当是合法的JSON格式字符串。
		      当不需要参数时，应当填”{}”。当参数需要注入规则执行的输出结果时，
		      可以使用字符%左右包裹变量名，变量名目前不区分大小写；组合规则时指定deviceId的某个属性，格式为%deviceId1.a%。
		      规则的执行结果包括规则语句SELECT和FROM之间的字段和自定义函数的
		      执行结果
            示例:
		    规则语句
		    SELECT COL1 AS AA,COL2 AS BB,COL3 AS CC FROM topic WHERE COL1 < 3
		     参数模板
		     {"COL1":"%AA%","const":"123"}
		     测试数据
		    {"COL1":1, "COL2":"B", "COL3":"Y", "COL4":"NO"}
		    输出接口参数
		    {"COL1":1,"const":"123"}

         }
      }
  ]
SQL描述:
	为了容易理解，把规则抽象成SQL表达式(类似Mysql语法)  
	注意，设备消息只有json格式才运行！
	1. SELECT
	select的属性来源于消息的payload，查询字段与payload字段对应，
	可以使用AS指定别名引用，也可以来源于函数比如deviceName()。
	若查询字段既不是来自于产品的属性字段(物模型)，也不在自定义函数列表中，
	则无法创建规则。
	如：select a, b, deviceId() as devId from ruleengine_100987211_10292321;
	其中a，b字段均为该产品的属性字段，devId 为deviceId()函数的别名。
	2. AS
	可以为表名称或列名称指定别名。 
	3. FROM
	FROM用来指定数据来源，表名拼接格式为ruleengine_tenantId_productId，
	如：ruleengine_10039191_10001079。
	当有符合规则的消息到达时，消息的payload数据以json形式被上下文环境使用
	(如果消息格式不合法,将忽略此消息)。 
	4. WHERE
	规则触发条件，条件表达式。当符合topic的消息到达时，这条消息触发规则的条件。
	在WHERE中使用到字段或者别名，需要在SELECT中明确获取，或者是该产品的属性。
	 如：select a, b from ruleengine_10039191_10001079 where a = ‘1’ and c = ‘2’;
	 其中where字段的a，c均为该产品的属性。
	5. Sql示例
	单条数据通过条件进行筛选。
	//查询字段掘payload字段对应，此处仅为示例
	SELECT 
	COL1 AS AA,
	COL2 AS BB,
	COL3 AS CC
	FROM ruleengine_100000_1000001
	WHERE AA< 3

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result": {
        "ruleForwardInfos": [
            {
                "forwardConfig": {
                    "content": "{\"test\":\"%a%\"}",
                    "url": "http://127.0.0.1:9090/test"
                },
                "forwardType": "HTTP",
                "operatorType": "01",
                "ruleForwardId": "317a66be-a578-538a-b3ca-344fed801b19"
            }
        ],
        "ruleId": "c68c7769-3e3a-c2f9-383d-ab8e73122a0b"
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

### API名称：saasQueryRule   版本号: 20200111000633

#### 描述

SAAS规则查询

#### 请求信息

请求路径：/api/v2/rule/sass/queryRule

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|ruleId|QUERY|String|false||
|productId|QUERY|String|false||
|pageNow|QUERY|Long|false||
|pageSize|QUERY|Long|false||


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result": {
        "endRow": 1,
        "firstPage": 0,
        "hasNextPage": false,
        "hasPreviousPage": false,
        "isFirstPage": false,
        "isLastPage": true,
        "lastPage": 0,
        "list": [
            {               
                "dataLevel": 0,
                "description": "修改规则，看转发是否存在",
                "productId": "10003561",
                "ruleForwardInfos": [],
                "ruleId": "be334616-d858-b382-9352-a50aaeb3fa1f",
                "ruleString": "select aa,cc from ruleengine_10106316_10003561 where aa = 1",
                "ruleType": "1000",
                "userId": "10107390"
            }
        ],
        "navigatePages": 8,
        "navigatepageNums": [],
        "nextPage": 0,
        "pageNum": 0,
        "pageSize": 0,
        "pages": 0,
        "prePage": 0,
        "size": 1,
        "startRow": 1,
        "total": 0
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

### API名称：saasUpdateRule   版本号: 20200111000540

#### 描述

更新SAAS规则引擎

#### 请求信息

请求路径：/api/v2/rule/sass/updateRule

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "ruleId": "c68c7769-3e3a-c2f9-383d-ab8e73122a0b",
   "dataLevel": 1,
  "description": "修改规则",
  "ruleType": "1000",
  "userId": "ljupdate",
  "ruleStreams": [
    {
	   "deviceId": "123",
       "productId": "10003561",
	   "deviceGroupId":null,
	   "dataLevel": 1,
       "ruleStr": "select aa,cc from ruleengine_10106316_10003561 where aa = 1 and deviceId()='123'"
    }
  ],
  "ruleForwardInfos": [
    {
        "forwardConfig": {
        "content": "{\"test\":\"%a%\"}",
        "url": "http://127.0.0.1:9090/test"
      },
      "forwardType": "HTTP",
      "operatorType": "01"
    }
    
  ]  

}

描述:
ruleId:修改、删除时必填，新增规则时，此参数为空
dataLevel:规则数据类型:0-产品级别;1-设备级别；2-设备分组级别[*必填];组合规则时只支持设备级别。
description:规则的描述信息, 长度不超过160位的字符串[*必填]
ruleType:规则类型;1000：简单规则，2000：组合规则
userId：用户ID[*必填]
ruleStreams：规则信息[*必填][{   
     ruleStr:规则内容，即sql。不能包含特殊字符*，修改、新增时必填,
		具体详看下面SQL描述   
	 productId:产品ID[*必填]		
	 deviceId：设备ID,可选;当dataLevel为1时则必填。
	 deviceGroupId：设备分组ID,可选;当dataLevel为2时则必填,类型为Integer型。
	 dataLevel:子数据流规则类型:0-产品级别;1-设备级别；2-设备分组级别；可选；当dataLevel填写时规则按照此定义的规则类型进行规则处理，未填写时按照上一级配置的级别处理。	
     
}]
ruleForwardInfos：JSON数组，可选[
     {
         ruleForwardId:修改规则涉及推送修改时必填，新增推送时，此参数为空
         operatorType:操作类型：“01”：新增（配合新增规则使用），
		      “10”：修改（配合修改规则使用），“00”：删除（配合修改规则使用）
         forwardType:推送类型，目前仅支持HTTP，新增、修改推送时，必填；
		     删除推送时，此参数为空
         forwardConfig:JSON格式
	 {
            url:推送地址，必填，http的url路径,例如: http://rule.ctwind.cn/test/api
            content:推送内容，必填.
            参数格式: JSON
            参数模板：配置发送给应用的消息体的定义；所填的数据全部以body的方式传递。
                      参数模板是HTTP接口请求的参数部分，应当是合法的JSON格式字符串。
		      当不需要参数时，应当填”{}”。当参数需要注入规则执行的输出结果时，
		      可以使用字符%左右包裹变量名，变量名目前不区分大小写；变量名目前不区分大小写；
                      组合规则时指定deviceId的某个属性，格式为%deviceId1.a%。
		      规则的执行结果包括规则语句SELECT和FROM之间的字段和自定义函数的
		      执行结果
            示例:
		    规则语句
		    SELECT COL1 AS AA,COL2 AS BB,COL3 AS CC FROM topic WHERE COL1 < 3
		     参数模板
		     {"COL1":"%AA%","const":"123"}
		     测试数据
		    {"COL1":1, "COL2":"B", "COL3":"Y", "COL4":"NO"}
		    输出接口参数
		    {"COL1":1,"const":"123"}

         }
      }
  ]
SQL描述:
	为了容易理解，把规则抽象成SQL表达式(类似Mysql语法)  
	注意，设备消息只有json格式才运行！
	1. SELECT
	select的属性来源于消息的payload，查询字段与payload字段对应，
	可以使用AS指定别名引用，也可以来源于函数比如deviceName()。
	若查询字段既不是来自于产品的属性字段(物模型)，也不在自定义函数列表中，
	则无法创建规则。
	如：select a, b, deviceId() as devId from ruleengine_100987211_10292321;
	其中a，b字段均为该产品的属性字段，devId 为deviceId()函数的别名。
	2. AS
	可以为表名称或列名称指定别名。 
	3. FROM
	FROM用来指定数据来源，表名拼接格式为ruleengine_tenantId_productId，
	如：ruleengine_10039191_10001079。
	当有符合规则的消息到达时，消息的payload数据以json形式被上下文环境使用
	(如果消息格式不合法,将忽略此消息)。 
	4. WHERE
	规则触发条件，条件表达式。当符合topic的消息到达时，这条消息触发规则的条件。
	在WHERE中使用到字段或者别名，需要在SELECT中明确获取，或者是该产品的属性。
	 如：select a, b from ruleengine_10039191_10001079 where a = ‘1’ and c = ‘2’;
	 其中where字段的a，c均为该产品的属性。
	5. Sql示例
	单条数据通过条件进行筛选。
	//查询字段掘payload字段对应，此处仅为示例
	SELECT 
	COL1 AS AA,
	COL2 AS BB,
	COL3 AS CC
	FROM ruleengine_100000_1000001
	WHERE AA< 3

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result": {
        "ruleForwardInfos": [
            {
                "forwardConfig": {
                    "content": "{\"test\":\"%a%\"}",
                    "url": "http://127.0.0.1:9090/test1"
                },
                "forwardType": "HTTP",
                "operatorType": "01",
                "ruleForwardId": "3eba4769-c64c-6681-d8b6-c2eacac52ff3"
            }
        ],
        "ruleId": "c68c7769-3e3a-c2f9-383d-ab8e73122a0b"
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

### API名称：saasDeleteRuleEngine   版本号: 20200111000611

#### 描述

SAAS规则删除

#### 请求信息

请求路径：/api/v2/rule/sass/deleteRule

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{ 
  "ruleId": "c68c7769-3e3a-c2f9-383d-ab8e73122a0b"
}
描述;
ruleId:规则Id[*必填]

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok"
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

