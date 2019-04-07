---
layout:     post
title:      AWS服务器搭建SSserver并开启BBR加速
subtitle:    ""
date:       2019-02-14
author:     tianhaoo
header-img: img/post-bg/22.jpg
catalog: true
tags:
  - 翻墙
  - 薅羊毛
---

# 背景

之前使用github薅羊毛的方法只能持续一年，现在一年已经过去了，想要继续FQ就得寻找新的羊毛薅，幸运的是“羊毛薅不尽，春风吹又生”，本篇博客是使用AWS的免费服务器搭建SSserver的过程，仅做记录。


# 前期准备

1. 启动一个免费的EC2实例（需要VISA卡）

2. 设置安全组，邮件提醒，开放相应的端口，至少要有22和ssserver的端口（默认是8000）

3. 连接到相应的服务器`ssh -i "my_key_pair.pem" ubuntu@{your_public_IP}`

4. 更新和安装必要的依赖 `apt-get update`

# 安装ss

```
sudo apt install shadowsocks

sudo vi /etc/myss.json

 {
     "server":"1.1.1.1",
     "server_port":8388,
     "local_address": "127.0.0.1",
     "local_port":1080,
     "password":"your passwd",
     "timeout":600,
     "method":"aes-256-cfb"
 }

```

**注意这里server的配置方法与其他服务器不同！**

**使用AWS的EC2搭建ssserver时"server"必须是VPS的私有IP才行，否则无法运行成功**


# 启动ssserver


```
ssserver -c /etc/myss.json -d start

```


# 查看输出信息

```
less /var/log/shadowsocks.log

```

如果没有报错信息，而且一切输出正常的话，此时使用客户端连上就可以用了，但是现在的速度太慢，下面介绍使用BBR进行加速的方法


# 开启BBR加速

## 介绍

BBR是一种TCP拥堵控制算法，是由google开发的，现在应用已经相当成熟，Linux Kernel 4.10 以上内核已经默认开启了，所以我们只要将ubuntu的内核升级到4.10+就可以直接开启了

## 查看当前可使用的控制算法

```
sysctl net.ipv4.tcp_available_congestion_control
```

在我的server上返回了

```
net.ipv4.tcp_available_congestion_control = reno cubic
```

代表可使用的有 reno 和 cubic 两种控制算法，并没有bbr

## 查看当前使用的拥塞控制算法

```
sysctl net.ipv4.tcp_congestion_control
```

在我的server上返回了

```
net.ipv4.tcp_congestion_control = cubic
```
代表当前使用的是cubic这种算法，我们要做的就是将他改成bbr

## 为 Ubuntu 安装 4.10 + 新内核

这个操作在Ubuntu下面非常方便，就像安装一个新的软件包一样

```
sudo apt-get install linux-generic-hwe-16.04
```

## 开启bbr

```
sudo modprobe tcp_bbr

echo "tcp_bbr" | sudo tee -a /etc/modules-load.d/modules.conf

sysctl net.ipv4.tcp_available_congestion_control
```

这时候会输出可用的算法有
```
net.ipv4.tcp_available_congestion_control = reno cubic bbr
```
就可以直接开启了
```
echo "net.core.default_qdisc=fq" | sudo tee -a /etc/sysctl.conf

echo "net.ipv4.tcp_congestion_control=bbr" | sudo tee -a /etc/sysctl.conf

sudo sysctl -p

sysctl net.ipv4.tcp_congestion_control
```
这时候会输出
```
net.ipv4.tcp_congestion_control = bbr
```
代表bbr开启成功

# 报错

根据报错的提示信息定位到`openssl.py`文件里面有个函数`libcrypto.EVP_CIPHER_CTX_cleanup.argtypes`已经弃用，将他改成`libcrypto.EVP_CIPHER_CTX_reset.argtypes`就行了，一共有两处。

此外，ssserver有时候会用着用着突然挂掉，这时候可以试一下重启EC2或者重建一个EC2实例也即换一个公网IP。















