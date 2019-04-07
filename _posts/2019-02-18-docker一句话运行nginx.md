---
layout:     post
title:      docker一句话运行nginx
subtitle:    ""
date:       2019-02-18
author:     tianhaoo
header-img: img/post-bg/23.jpg
catalog: true
tags:
  - docker
  - web
---

# 背景介绍

同学们难免会遇到这样的情形————有时候需要在网上放几个静态页面，或者构建几个有简单逻辑的网页服务，可能根本不需要考虑性能，不需要考虑美观可维护啥的，只需要很短时间就能跑得起来，不需要的时候直接关掉又对我们现有的服务器不会产生任何影响，甚至再次需要该服务的时候又能很快再次调用起来。我最近就碰到了这样一个需求，要在某个答辩中以网页的形式展示一下一些简单的东西，这时候才发现docker在这种应用场景下简直是无比的方便。


# 具体做法

其实官网已经介绍的很详细了 [官网链接](https://docs.docker.com/samples/library/nginx/)

只要下面一行代码


```
docker run --name front-end-nginx -v /root/wwwroot/front_end:/usr/share/nginx/html:ro -p 8080:80 -d nginx

```

不需要的时候直接 docker stop 、 rm 就行了，就像关闭一个程序一样，干净利落。