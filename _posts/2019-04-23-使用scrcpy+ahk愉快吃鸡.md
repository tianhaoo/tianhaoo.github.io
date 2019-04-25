---
layout:     post
title:      使用scrcpy+ahk愉快吃鸡
subtitle:   ""
date:       2019-04-23
author:     tianhaoo
header-img: img/post-bg/33.jpg
catalog: true
tags:
  - 日常
---

## 背景
众所周知，腾讯推出的吃鸡类游戏——刺激战场本意是还原端游PUBG，但是在小手机屏幕上瞄准打人实在是太蛋疼了，解决这个问题的正常思路是用模拟器在电脑上玩。**但是**腾讯为了公平起见，会检测到模拟器并且会给模拟器玩家匹配同样是使用模拟器的玩家，要知道菜鸡是相对的，在手游平台的菜鸡跑到端游平台依旧是菜鸡。虽然网上有不少尝试，但大多都会被检测出来并封号。但我们是有程序员的双手和大脑的菜鸡，所以为了能在电脑端匹配手机玩家虐他们，本篇博客提出一种理论上不可能被检测到的方法。

## 简介
思路就是使用手机投屏工具，再在电脑上模拟**电脑屏幕**的点击事件，注意一定是模拟电脑屏幕的点击事件，这也就在理论上保证了不可能被手机端检测到。（考虑到模拟手机的触摸输入会很容易被检测到，但未查证，若腾讯未做相关的检测的话安卓开发者就可以直接使用adb进行模拟输入，会更方便一点）。这样一来就可以使用键鼠操作外加大显示屏，用来和手机端的玩家对枪，肯定能打的对面怀疑人生。

## 环境和依赖

* 实验环境: `win10 x64`, `安卓手机小米6`

* 需要使用两个工具: 
  1. [scrcpy](https://github.com/Genymobile/scrcpy)
  2. [AHK](https://www.autohotkey.com/)

### csrcpy
scrcpy是一款开源的手机投屏的工具，相比于win10自带的投屏而言，增加了模拟触屏输入功能，但是不支持音频，而且没有图形化界面。有钱的话可以使用Vysoro pro。

具体的用法和介绍见github

[https://github.com/Genymobile/scrcpy](https://github.com/Genymobile/scrcpy)

### AHK

AHK的全称是AutoHotkey，是一个开源的用在windows上面的脚本语言，功能强大，安装简单，文档齐全，类似于中国的软件按键精灵，但是要干净稳定安全许多，唯一的不足就是全英文。本博客主要是用该语言的模拟鼠标功能。

安装和使用见官网

[https://www.autohotkey.com/](https://www.autohotkey.com/)

## 具体步骤

1. 使用scrcpy连接手机

```
.\scrcpy.exe
```

2. 编写ahk脚本

```ahk
#MaxHotkeysPerInterval 100
 
w::
; MouseClickDrag, left, 343, 783, 344, 663
SendEvent {Click 343, 783, down}{click 344, 663 down}
KeyWait, w
SendEvent {click 344, 663 up}
MouseMove, 343, 783
return 


a::
; MouseClickDrag, left, 343, 783, 221, 784
SendEvent {Click 343, 783, down}{click 221, 784 down}
KeyWait, a
SendEvent {click 221, 784 down}
MouseMove, 343, 783
return

s::
; MouseClickDrag, left, 343, 783, 344, 905
SendEvent {Click 343, 783, down}{click 344, 905 down}
KeyWait, s
SendEvent {click 344, 905 down}
MouseMove, 343, 783
return 

d::
; MouseClickDrag, left, 343, 783, 465, 783
SendEvent {Click 343, 783, down}{click 465, 783 down}
KeyWait, d
SendEvent {click 465, 783 down}
MouseMove, 465, 78re
return 
```

3. 启动ahk脚本

4. 开始吃鸡


## 效果展示

![](/img/20190423/raw.gif)

## 

