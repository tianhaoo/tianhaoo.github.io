---
layout:     post
title:      linux搭建lamp服务器
subtitle:    ""
date:       2017-02-24
author:     tianhaoo
header-img: post-bg/img/3.jpg
catalog: true
tags:
  - web
---


记录Ubuntu搭建lamp服务器的过程



### 简介

* lamp 即为linux-apache-mysql-php的缩写

* nginx 相对 apache 的优点：

>   * 轻量级，同样起web 服务，比apache 占用更少的内存及资源
>   *抗并发，nginx处理请求是异步非阻塞的，而apache则是阻塞型的，在高并发下nginx能保持低资源低消耗
>   * 高性能高度模块化的设计，编写模块相对简单社区活跃，各种高性能模块出品迅速

* apache 相对nginx 的优点：

>   * **rewrite** ，比nginx 的rewrite 强大模块超多，基本想到的都可以找到
>   * 少bug ，nginx 的bug 相对较多
>   * **超稳定**

<!-- more -->
### 安装顺序

最好是PHP在Apache之后安装，顺序可以按照单词lamp出现的顺序来安装

### 安装之前先更新一下源

```
$ sudo apt update
```

### 心情好的话还可以更新一下软件

```
$ sudo apt upgrade
```

### 安装命令

* 先安装apache2

```
$ sudo apt install apache2
```

安装完成后可以在浏览器打开127.0.0.1查看是否安装成功

* 然后是MySQL

```
$ sudo apt install mysql-server mysql-client
```
安装过程中会要求输入两次密码

* 然后是PHP7和apache的PHP7模块

```
$ sudo apt install php7.0
$ sudo apt install libapache2-mod-php7.0
```
   安装 libapache2-mod-php7.0的目的是为了让Apache支持PHP

### 运行检测

现在我的Linux就可以是一台服务器了，所有网页文件都放在

```
/var/www/html
```

这个目录里面，现在应该只有一个index.html, cd到那个目录

```
$ sudo vim test.php
```


写入如下代码

```
this is a test`:   
<?php
    phpinfo();
?>
```

在浏览器输入127.0.0.1/test.php ,如果出现PHPinfo页面，说明安装成功
