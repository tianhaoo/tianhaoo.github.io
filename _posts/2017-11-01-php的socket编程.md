---
layout:     post
title:      php的socket编程
subtitle:    ""
date:       2017-11-01
author:     tianhaoo
header-img: img/13.jpg
catalog: true
tags:
  - php
  - web
---


php的socket编程



## GET方法的socket通信

### client.php
<!-- more -->
```php
<?php

    // 创建连接
    $fp = fsockopen('localhost', 80, $errno, $errstr, 80);

    // 检测
    if(!$fp) {
        echo $errstr; die;
    }

    // 拼接http请求报文
    $http = '';

    // 请求报文包括三个部分 请求行 请求头 请求体
    $http .= "GET /http/server.php HTTP/1.1\r\n"; // 请求头包括三个部分 请求方式 请求脚本的绝对路径 协议的版本号

    // 请求头信息
    $http .= "HOST: localhost\r\n";
    $http .= "Connection: close\r\n\r\n"; //创建完连接后立刻断开，还有一种是keep-alive

    // 请求体 无


    // 发送请求
    fwrite($fp, $http);

    // 获取结果
    $res = '';
    while(!feof($fp)) {
        $res .= fgets($fp);
    }

    echo $res;
```

### server.php
```php
<?php

    echo "Hello world!";
```

### 响应内容
```
// 响应行
HTTP/1.1 200 OK  

// 响应头
Date: Thu, 25 Jan 2018 05:58:21 GMT
Server: Apache
X-Frame-Options: SAMEORIGIN
X-Powered-By: PHP/7.1.8
Content-Length: 12
Connection: close
Content-Type: text/html; charset=UTF-8

// 响应体
Hello world!
```


## POST方法的socket通信

### post.php

```php
<?php

    // 创建连接
    $fp = fsockopen('localhost', 80, $errno, $errstr, 10);

    // 判断
    if(!$fp) {
        echo $errstr; die;
    }

    $http = '';

    // 请求行
    $http .= "POST /http/server.php HTTP/1.1\r\n";

    // 请求头
    $http .= "Host: localhost\r\n";
    $http .= "Connection: close\r\n";
    $http .= "Cookie: username=admin;uid=200\r\n";
    $http .= "user-agent: chrome-firefox\r\n";
    $http .= "Content-type: application/x-www-form-urlencoded\r\n";
    $http .= "Content-length: 39\r\n\r\n";

    // 请求行和请求体之间必须加两个\r\n

    // 请求体
    $http .= "email=tianhaoo@gmail.com&username=admin\r\n";

    // 发送
    fwrite($fp, $http);

    $res = '';
    // 获取结果
    while(!feof($fp)) {
        $res .= fgets($fp);
    }

    echo $res;



```

### server.php

```
<?php

    echo "Hello world!1234";

    // var_dump($_GET);
    // var_dump($_POST);

    // 打印cookie
     var_dump($_COOKIE);


    // var_dump($GLOBALS);
     // var_dump($_SERVER);
```

## 用[API](http://wxlink.jd.com/market/api/10610)请求天气

### weather.php
```
<?php
/**
 * Created by PhpStorm.
 * User: Tianhaoo
 * Date: 2018/1/26
 * Time: 6:42
 */
    // 72ae96aaf8cf7af9d7bc1267c938b146
    $fp = fsockopen('way.jd.com', 80,$errno, $errstr, 10);

    if(!$fp) {
        echo $errstr; die;
    }

    $http = '';

    // 请求行
    $http .= "GET /he/freeweather?city=beijing&appkey=72ae96aaf8cf7af9d7bc1267c938b146 HTTP/1.1\r\n";

    // 请求头
    $http .= "Host: way.jd.com\r\n";
    $http .= "Connection: close\r\n";
    $http .= "appkey: 72ae96aaf8cf7af9d7bc1267c938b146\r\n\r\n";

    //发送
    fwrite($fp, $http);

    // 获取结果
    $res = '';

    while(!feof($fp)) {
        $res .= fgets($fp);
    }

    echo $res;
```

### 请求结果
```
HTTP/1.1 200 OK
Server: jfe
Date: Fri, 26 Jan 2018 07:08:26 GMT
Content-Type: application/json;charset=utf-8
Content-Length: 5420
Connection: close
Expires: Fri, 26 Jan 2018 07:08:25 GMT
Cache-Control: max-age=0

{
  "code": "10000",
  "charge": false,
  "msg": "查询成功",
  "result": {
    "HeWeather5": [
      {
        "aqi": {
          "city": {
            "aqi": "46",
            "qlty": "优",
            "pm25": "32",
            "pm10": "44",
            "no2": "42",
            "so2": "10",
            "co": "1",
            "o3": "42"
          }
        },
        "basic": {
          "city": "北京",
          "cnty": "中国",
          "id": "CN101010100",
          "lat": "39.90498734",
          "lon": "116.4052887",
          "update": {
            "loc": "2018-01-26 14:15",
            "utc": "2018-01-26 06:15"
          }
        },
        "daily_forecast": [
          {
            "astro": {
              "mr": "12:33",
              "ms": "01:33",
              "sr": "07:27",
              "ss": "17:27"
            },
            "cond": {
              "code_d": "100",
              "code_n": "101",
              "txt_d": "晴",
              "txt_n": "多云"
            },
            "date": "2018-01-26",
            "hum": "21",
            "pcpn": "0.0",
            "pop": "0",
            "pres": "1038",
            "tmp": {
              "max": "-4",
              "min": "-10"
            },
            "uv": "2",
            "vis": "20",
            "wind": {
              "deg": "189",
              "dir": "南风",
              "sc": "微风",
              "spd": "7"
            }
          },
          {
            "astro": {
              "mr": "13:16",
              "ms": "02:41",
              "sr": "07:26",
              "ss": "17:28"
            },
            "cond": {
              "code_d": "101",
              "code_n": "101",
              "txt_d": "多云",
              "txt_n": "多云"
            },
            "date": "2018-01-27",
            "hum": "37",
            "pcpn": "0.0",
            "pop": "0",
            "pres": "1032",
            "tmp": {
              "max": "-1",
              "min": "-9"
            },
            "uv": "2",
            "vis": "20",
            "wind": {
              "deg": "184",
              "dir": "南风",
              "sc": "微风",
              "spd": "6"
            }
          },
          {
            "astro": {
              "mr": "14:05",
              "ms": "03:50",
              "sr": "07:25",
              "ss": "17:29"
            },
            "cond": {
              "code_d": "100",
              "code_n": "100",
              "txt_d": "晴",
              "txt_n": "晴"
            },
            "date": "2018-01-28",
            "hum": "16",
            "pcpn": "0.0",
            "pop": "0",
            "pres": "1035",
            "tmp": {
              "max": "0",
              "min": "-8"
            },
            "uv": "2",
            "vis": "20",
            "wind": {
              "deg": "5",
              "dir": "北风",
              "sc": "微风",
              "spd": "8"
            }
          },
          {
            "astro": {
              "mr": "15:03",
              "ms": "04:57",
              "sr": "07:24",
              "ss": "17:31"
            },
            "cond": {
              "code_d": "100",
              "code_n": "100",
              "txt_d": "晴",
              "txt_n": "晴"
            },
            "date": "2018-01-29",
            "hum": "21",
            "pcpn": "0.0",
            "pop": "0",
            "pres": "1032",
            "tmp": {
              "max": "1",
              "min": "-8"
            },
            "uv": "2",
            "vis": "20",
            "wind": {
              "deg": "228",
              "dir": "西南风",
              "sc": "微风",
              "spd": "8"
            }
          },
          {
            "astro": {
              "mr": "16:07",
              "ms": "06:00",
              "sr": "07:24",
              "ss": "17:32"
            },
            "cond": {
              "code_d": "101",
              "code_n": "101",
              "txt_d": "多云",
              "txt_n": "多云"
            },
            "date": "2018-01-30",
            "hum": "20",
            "pcpn": "0.0",
            "pop": "0",
            "pres": "1029",
            "tmp": {
              "max": "4",
              "min": "-5"
            },
            "uv": "1",
            "vis": "20",
            "wind": {
              "deg": "247",
              "dir": "西南风",
              "sc": "微风",
              "spd": "4"
            }
          },
          {
            "astro": {
              "mr": "17:18",
              "ms": "06:57",
              "sr": "07:23",
              "ss": "17:33"
            },
            "cond": {
              "code_d": "101",
              "code_n": "101",
              "txt_d": "多云",
              "txt_n": "多云"
            },
            "date": "2018-01-31",
            "hum": "19",
            "pcpn": "0.0",
            "pop": "0",
            "pres": "1029",
            "tmp": {
              "max": "4",
              "min": "-5"
            },
            "uv": "2",
            "vis": "20",
            "wind": {
              "deg": "281",
              "dir": "西北风",
              "sc": "微风",
              "spd": "8"
            }
          },
          {
            "astro": {
              "mr": "18:29",
              "ms": "07:46",
              "sr": "07:22",
              "ss": "17:34"
            },
            "cond": {
              "code_d": "101",
              "code_n": "101",
              "txt_d": "多云",
              "txt_n": "多云"
            },
            "date": "2018-02-01",
            "hum": "21",
            "pcpn": "0.0",
            "pop": "0",
            "pres": "1030",
            "tmp": {
              "max": "2",
              "min": "-8"
            },
            "uv": "2",
            "vis": "20",
            "wind": {
              "deg": "1",
              "dir": "北风",
              "sc": "3-4",
              "spd": "14"
            }
          }
        ],
        "hourly_forecast": [
          {
            "cond": {
              "code": "103",
              "txt": "晴间多云"
            },
            "date": "2018-01-26 16:00",
            "hum": "19",
            "pop": "0",
            "pres": "1035",
            "tmp": "-3",
            "wind": {
              "deg": "154",
              "dir": "东南风",
              "sc": "微风",
              "spd": "5"
            }
          },
          {
            "cond": {
              "code": "103",
              "txt": "晴间多云"
            },
            "date": "2018-01-26 19:00",
            "hum": "22",
            "pop": "0",
            "pres": "1034",
            "tmp": "-3",
            "wind": {
              "deg": "118",
              "dir": "东南风",
              "sc": "微风",
              "spd": "3"
            }
          },
          {
            "cond": {
              "code": "103",
              "txt": "晴间多云"
            },
            "date": "2018-01-26 22:00",
            "hum": "24",
            "pop": "0",
            "pres": "1034",
            "tmp": "-5",
            "wind": {
              "deg": "88",
              "dir": "东风",
              "sc": "微风",
              "spd": "3"
            }
          },
          {
            "cond": {
              "code": "103",
              "txt": "晴间多云"
            },
            "date": "2018-01-27 01:00",
            "hum": "33",
            "pop": "0",
            "pres": "1037",
            "tmp": "-5",
            "wind": {
              "deg": "63",
              "dir": "东北风",
              "sc": "微风",
              "spd": "3"
            }
          },
          {
            "cond": {
              "code": "103",
              "txt": "晴间多云"
            },
            "date": "2018-01-27 04:00",
            "hum": "29",
            "pop": "0",
            "pres": "1037",
            "tmp": "-6",
            "wind": {
              "deg": "26",
              "dir": "东北风",
              "sc": "微风",
              "spd": "4"
            }
          },
          {
            "cond": {
              "code": "103",
              "txt": "晴间多云"
            },
            "date": "2018-01-27 07:00",
            "hum": "30",
            "pop": "0",
            "pres": "1036",
            "tmp": "-8",
            "wind": {
              "deg": "21",
              "dir": "东北风",
              "sc": "微风",
              "spd": "4"
            }
          },
          {
            "cond": {
              "code": "103",
              "txt": "晴间多云"
            },
            "date": "2018-01-27 10:00",
            "hum": "19",
            "pop": "0",
            "pres": "1036",
            "tmp": "-7",
            "wind": {
              "deg": "15",
              "dir": "东北风",
              "sc": "微风",
              "spd": "4"
            }
          },
          {
            "cond": {
              "code": "103",
              "txt": "晴间多云"
            },
            "date": "2018-01-27 13:00",
            "hum": "14",
            "pop": "0",
            "pres": "1033",
            "tmp": "-2",
            "wind": {
              "deg": "237",
              "dir": "西南风",
              "sc": "微风",
              "spd": "6"
            }
          }
        ],
        "now": {
          "cond": {
            "code": "100",
            "txt": "晴"
          },
          "fl": "-9",
          "hum": "26",
          "pcpn": "0.0",
          "pres": "1037",
          "tmp": "-5",
          "vis": "10",
          "wind": {
            "deg": "267",
            "dir": "西风",
            "sc": "微风",
            "spd": "7"
          }
        },
        "status": "ok",
        "suggestion": {
          "air": {
            "brf": "中",
            "txt": "气象条件对空气污染物稀释、扩散和清除无明显影响，易感人群应适当减少室外活动时间。"
          },
          "comf": {
            "brf": "较不舒适",
            "txt": "白天天气晴好，但仍会使您感觉偏冷，不很舒适，请注意适时添加衣物，以防感冒。"
          },
          "cw": {
            "brf": "较适宜",
            "txt": "较适宜洗车，未来一天无雨，风力较小，擦洗一新的汽车至少能保持一天。"
          },
          "drsg": {
            "brf": "寒冷",
            "txt": "天气寒冷，建议着厚羽绒服、毛皮大衣加厚毛衣等隆冬服装。年老体弱者尤其要注意保暖防冻。"
          },
          "flu": {
            "brf": "较易发",
            "txt": "天气较凉，较易发生感冒，请适当增加衣服。体质较弱的朋友尤其应该注意防护。"
          },
          "sport": {
            "brf": "较不宜",
            "txt": "天气较好，但考虑天气寒冷，推荐您进行室内运动，户外运动时请注意保暖并做好准备活动。"
          },
          "trav": {
            "brf": "较适宜",
            "txt": "天气较好，同时又有微风伴您一路同行。稍冷，较适宜旅游，您仍可陶醉于大自然的美丽风光中。"
          },
          "uv": {
            "brf": "最弱",
            "txt": "属弱紫外线辐射天气，无需特别防护。若长期在户外，建议涂擦SPF在8-12之间的防晒护肤品。"
          }
        }
      }
    ]
  }
}
```



好玩！
