---
layout:     post
title:      使用githubpage和Hexo搭建个人博客
subtitle:    "\"Hello World, Hello Blog\""
date:       2017-02-04
author:     tianhaoo
header-img: img/post-bg/1.jpg
catalog: true
tags:
  - 日常
---

本文将会介绍这篇博客的搭建过程

和一些简单的配置

以及如何做到在多机间同步等





### 准备工作

在GitHub里创建一个名为username.github.io的repository

### 安装node.js和npm

```
sudo apt install nodejs-legacy
sudo apt install npm
npm -v
```

<!-- more -->
### 安装git

```
sudo apt install git
```

### 安装hexo

首先进入~/blog目录

```
sudo npm install hexo-deployer-git
sudo npm install hexo-cli -g
```
* npm安装模块

  `npm install xxx`利用 npm 安装xxx模块到当前命令行所在目录；
  `npm install -g xxx`利用npm安装全局模块xxx；

* 本地安装时将模块写入package.json中：

  `npm install xxx`安装但不写入package.json；
  `npm install xxx –save` 安装并写入package.json的”dependencies”中；
  `npm install xxx –save-dev`安装并写入package.json的”devDependencies”中。

* npm 删除模块

  `npm uninstall xxx`删除xxx模块；
  `npm uninstall -g xxx`删除全局模块xxx；

### 建立工作区
```
hexo init Blog   # 此操作会在当前目录下生成一个Blog文件夹
```
### 给自己的github添加公钥

* `ssh-keygen -t rsa -C "注册Github用的邮箱" `

* 将**id_rsa.pub**里的内容复制到github里

* `ssh -T git@github.com`

### 简单配置

配置文件路径：blog/_comfig.yml


1. title ： 博客的标题。

2. language: zh-Hans

2. timezone: Aisa/shanghai

2. author： 作者。

3. url： 博客的地址。

4. root: 这个十分重要，就是你项目所在的文件夹的名称（如果你选择使用github page做站点，就写YourUserName.github.io， 如果你选择使用自己的服务器来做站点，就写你服务器上存放代码的文件夹名称，你会用YourIP/YourRoot的方式来访问。

5. Directory：块下的几行你可以全部打开，但是其中的某些东西需要进一步配置。

6. theme：主题

7. `deploy： type: git, repo: git@github.com:YourUserName/YourUserName.github.io.git, branch: master。`


### 开始写博客

```
cd blog

hexo new {artical name}
```

### 部署

```
hexo g -d
```

* deploy报错的话 `npm install hexo-deployer-git --save `

### 多机同步

用分支的思路！一个分支用来存放Hexo生成的网站原始的文件，另一个分支用来存放生成的静态网页。

1. 新建一个hexo分支，设为默认分支

2. 将这个分支拷贝下来，我们只要他的`.git`文件，放入blog目录

3. 执行`git add .`, `git commit -m "backups"`, `git push [origin hexo]`, “origin hexo”不加也行，因为hexo本来就是默认分支

4. 部署的话，只需要按照以下流程
  - `git add .`
  - `git commit -m "backups"`
  - `git push`
  - `hexo g -d`

5. 如果更换了电脑，只需要
  - `git clone {your repository} ~/blog`
  - `npm install hexo`
  - `npm install`
  - `npm install hexo-deployer-git`
  - 不需要`hexo init`

### 更换博客主题

* [next](https://github.com/iissnan/hexo-theme-next)

* 添加标签页
  - hexo new page tags
  - 确认站点配置文件里有tag_dir: tags
  - 确认主题配置文件里有tags: /tags
  - 编辑站点的source/tags/index.md，添加
  ```
  title: tags
  date: 2015-10-20 06:49:50
  type: "tags"
  comments: false
  ```
### next主题配置

1. 在右上角或者左上角实现fork me on github

```
<a href="https://your-url" class="github-corner" aria-label="View source on Github"><svg width="80" height="80" viewBox="0 0 250 250" style="fill:#151513; color:#fff; position: absolute; top: 0; border: 0; right: 0;" aria-hidden="true"><path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path><path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path><path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path></svg></a><style>.github-corner:hover .octo-arm{animation:octocat-wave 560ms ease-in-out}@keyframes octocat-wave{0%,100%{transform:rotate(0)}20%,60%{transform:rotate(-25deg)}40%,80%{transform:rotate(10deg)}}@media (max-width:500px){.github-corner:hover .octo-arm{animation:none}.github-corner .octo-arm{animation:octocat-wave 560ms ease-in-out}}</style>
```

然后粘贴刚才复制的代码到`themes/next/layout/_layout.swig`文件中(放在`<div class="headband"></div>`的下面)，并把`href`改为你的github地址

2. 修改文章底部的那个带#号的标签

修改模板`/themes/next/layout/_macro/post.swig`，搜索 `rel="tag">#`，将 `#` 换成`<i class="fa fa-tag"></i>`

3. 在网站底部加上访问量(不蒜子)

打开/theme/next/_config.yml，找到如下的配置项
```
# Show PV/UV of the website/page with busuanzi.
# Get more information on http://ibruce.info/2015/04/04/busuanzi/
busuanzi_count:
  # count values only if the other configs are false
  enable: false
  # custom uv span for the whole site
  site_uv: true
  site_uv_header: <i class="fa fa-user"></i>
  site_uv_footer:
  # custom pv span for the whole site
  site_pv: true
  site_pv_header: <i class="fa fa-eye"></i>
  site_pv_footer:
  # custom pv span for one page only
  page_pv: true
  page_pv_header: <i class="fa fa-file-o"></i>
  page_pv_footer:
```

将enable的值由false修改为true后，重新部署即可看到效果。

[alternatives](http://shenzekun.cn/hexo%E7%9A%84next%E4%B8%BB%E9%A2%98%E4%B8%AA%E6%80%A7%E5%8C%96%E9%85%8D%E7%BD%AE%E6%95%99%E7%A8%8B.html)

### next配置站点地图

####　执行命令安装sitemap
```
npm install hexo-generator-sitemap --save
```

#### 在Hexo站点配置文件_config.yml中加入sitemap插件

```
# Extensions
plugins: hexo-generator-sitemap
```

#### 执行命令生成sitemap文件
```
hexo clean
hexo g
```

以上操作顺利无误的话，我们可以在Hexo站点的public文件夹中找到sitemap.xml文件，可以通过 http://yoursite.com/sitemap.xml 的方式访问进行查看，如果无法生成sitemap.xml，可能是因为执行安装命令的时候没有加--save.

#### 提交sitemap到Google
这块在官方文档里面有提到（官方文档其实很容易上手，跟着官方走还是很容易的，有些地方可能不够详细，但是网上关于next的配置博客也不少，如｜Hexo优化｜如何向google提交sitemap（详细）），这里给出傻瓜式详细步骤：

1. 进入Google Webmaster Central
2. 点击红色的”ADD A PROPERTY”
3. 在弹出来的小框中加入你的站点地址 http://yoursite.com ，然后点击”Continue”
4. Tab栏选择”Alternate methods”，选中HTML tag可以看见

```
<meta name="google-site-verification" content="xxxxxxxxxxxxxxxxxx" /> 
```
#### 复制content的值
5. 打开next主题的配置文件_config.yml，找到google_site_verification字段（找不到就新建）：

```
# Google Webmaster tools verification setting
# See: https://www.google.com/webmasters/
google_site_verification: xxxxxxxxxxxxxxxxxx #4中content的值
```

6. 执行命令重新发布站点
```
hexo d -g
```

7. 回到4中的Google Webmaster Central页面，点击骚红色的”VERIFY”，done！

#### 提交sitemap到百度
[Hexo搭建GitHub博客（三）- NexT主题配置使用 #baidusitemap安装配置 ](http://zhiho.github.io/2015/09/29/hexo-next/)中也已经提到了，“普通的Sitemap格式不符合百度的要求”，所以我们需要对度娘特殊处理：

1. 执行命令安装百度sitemap
```
npm install hexo-generator-baidu-sitemap --save
```

2. 站点配置文件中加入百度sitemap插件
```
# Extensions
plugins: hexo-generator-baidu-sitemap
```
3. 执行命令生成百度sitemap文件
```
hexo clean
hexo g
```
4. 与Google一样，以上操作顺利无误的话，我们可以在Hexo站点的public文件夹中找到baidusitemap.xml文件

5. 进入百度链接提交通道，点击验证网站所有权（或者直接进入）
输入你的站点地址http://yoursite.com ，然后点击“下一步”
选中“HTML标签验证”可以看见

```
<meta name="baidu-site-verification" content="xxxxxxxx" />
```

6. 与Google不同的是，我们并不能通过在_config.yml中新建baidu_site_verification字段的方式进行验证（我试过好像不行），所以我们直接在Hexo站点的public文件夹中找到index.html文件，并在其中加上3中的验证标签

7. 执行命令重新发布站点

```
hexo d -g
```

8. 回到3中的百度验证网站页面，点击“完成验证”，done！


