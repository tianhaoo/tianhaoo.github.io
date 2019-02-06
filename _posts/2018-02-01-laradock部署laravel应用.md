---
layout:     post
title:      laradock部署laravel应用
subtitle:    "部署环境为腾讯云服务器"
date:       2018-02-01
author:     tianhaoo
header-img: img/5.jpg
catalog: true
tags:
  - laravel
  - docker
---



### 安装docker

ubuntu16.04
```
curl -sSL https://get.daocloud.io/docker | sh
```
ubuntu18.04

```bash
$ sudo apt install docker.io
$ sudo systemctl start docker
$ sudo systemctl enable docker
```
#### Adding a user to the "docker" group will grant the ability to run
```
sudo groupadd docker
```
<!--more-->
### 安装docker-compose
```
//ubuntu注意权限问题
sudo -i

curl -L https://get.daocloud.io/docker/compose/releases/download/1.13.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

exit
```

### 开启国内镜像加速
```
curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://1f637783.m.daocloud.io
```

### 下载laradock
```
git clone https://github.com/Laradock/laradock.git
```


### 编辑配置文件
```
cd laradock
cp env-example .env
vi .env
```

#### .env 配置说明
```
APPLICATION=../wwwroot
DATA_SAVE_PATH=../wwwroot/data
```

### 启动相关
```
docker-compose up apache2 mysql
```

### 进入工作空间
```
docker-compose exec workspace bash
```

### 每次修改.env之后要重新构建相应的容器
```
docker-compose build
```

### 返回上级目录克隆相应的web应用文件
```
cd ..
git clone
```

### 
```
sudo chown -R www-data:www-data 
sudo chmod -R 775 storage/
sudo chown -R www-data:www-data /var/www/laravel-blog
```


### laravel应用的配置文件
```
DB_CONNECTION=mysql
DB_HOST=mysql
DB_PORT=3306
DB_DATABASE=
DB_USERNAME=root
DB_PASSWORD=

// 邮箱服务
MAIL_DRIVER=smtp
MAIL_HOST=smtp.qq.com
MAIL_PORT=465
MAIL_FROM_ADDRESS=
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM_NAME=
MAIL_ENCRYPTION=ssl
```

```
### Application Path
# Point to your application code, will be available at `/var/www`.

APPLICATION=../kyjj/
```

```
sudo /etc/init.d/apache2 start restart stop
sudo /etc/init.d/mysql start restart stop
```

```
sudo update-rc.d -f nginx remove 删除mysql随机器启动的服务
sudo update-rc.d -f apache2 remove 删除apache2随机器启动的服务
```

查看/etc/rc2.d/里面的apache和nginx启动脚本，通常都是【一个英文字母 + 两个阿拉伯数字 + 脚本名称】。英文字母是S的都是会自动启动的，K则相反。所以只要找到apache和nginx的启动脚本，把S改成K就可以了。

README
```
To disable a service in this runlevel, rename its script in this
directory so that the new name begins with a 'K' and a two-digit
number, and run 'update-rc.d script defaults' to reorder the scripts
according to dependencies.  A warning about the current runlevels
being enabled not matching the LSB header in the init.d script will be
printed.  To re-enable the service, rename the script back to its
original name beginning with 'S' and run update-rc.d again.
```

### 出现奇怪的mysql报错的解决办法

首先查看自己`.env`文件中有没有配置正确，host要配置为mysql而不是127.0.0.1

然后再报错的话，有可能是mysql版本问题，在.env里面修改mysql版本为5.7即可
如果坚持想用mysql8.0的话（没错就是喜欢用最新的），按照以下步骤配置
1. 报错代号[2054]
```mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
ALTER USER 'default'@'%' IDENTIFIED WITH mysql_native_password BY 'secret';
```
2. 报错代号[42000]
在`config/database.php`中的mysql部分添加`mode`配置
```env
    'mysql' => [
        'driver' => 'mysql',
        'host' => env('DB_HOST', '127.0.0.1'),
        'port' => env('DB_PORT', '3306'),
        'database' => env('DB_DATABASE', 'forge'),
        'username' => env('DB_USERNAME', 'forge'),
        'password' => env('DB_PASSWORD', ''),
        'unix_socket' => env('DB_SOCKET', ''),
        'charset' => 'utf8mb4',
        'collation' => 'utf8mb4_unicode_ci',
        'prefix' => '',
        'strict' => true,
        'engine' => null,
        'modes'  => [
            'ONLY_FULL_GROUP_BY',
            'STRICT_TRANS_TABLES',
            'NO_ZERO_IN_DATE',
            'NO_ZERO_DATE',
            'ERROR_FOR_DIVISION_BY_ZERO',
            'NO_ENGINE_SUBSTITUTION',
        ],
    ],
```

### 修改时区
.env 下的WORKSPACE_TIMEZONE=UTC更改 为WORKSPACE_TIMEZONE=Asia/Shanghai，php-fpm\laravel.ini中将 date.timezone=UTC更改为date.timezone=Asia/Shanghai

然后docker-compose build php-fpm workspace

### 添加端口映射
有可能你的laradock里面跑了不止一个应用，想利用nginx的反向代理，但学校不给子域名。你还有另一种方法，利用frp的路由匹配功能，给不同的应用设置不同的端口，再通过不同的路由匹配就达到了内网穿透的功能。这时你发现laradock在build的时候就只开了一个80和443端口，不用担心，可以按照以下方法开启想要的端口映射

修改docker-compose.yml文件中的 Workspace Utilities配置项

```
      ports:
        - "${WORKSPACE_SSH_PORT}:22"
      ## 将host 9501端口映射容器的9501端口  格式：hostPort:containerPort  host代表主机   container 代表容器
        - "9501:9501"
        - "9502:9502"
```

然后docker-compose build workspace