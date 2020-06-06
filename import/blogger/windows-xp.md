Title: Установка Windows XP с флэшки
Date: 2014-10-16 08:18
Author: Краз
Tags: BootFlashTool
Slug: windows-xp
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
Для ипользования [загрузочной флэшки](http://kis-gel.blogspot.com/2014/10/usb.html) в качестве  источника установки WIndows XP нужно в корень USB диска скопировать  установочный .iso образ и добавить следующий блок в файл menu.lst:  

> [[[title Install WinXP SP3]{style="line-height: 20.7999992370605px; white-space: pre-wrap;"}]{style="background-color: white;"}[[map /winxp.iso (hd32)]{style="line-height: 20.7999992370605px; white-space: pre-wrap;"}]{style="background-color: white;"}[[map --hook]{style="line-height: 20.7999992370605px; white-space: pre-wrap;"}]{style="background-color: white;"}[[chainloader (hd32)]{style="line-height: 20.7999992370605px; white-space: pre-wrap;"}]{style="background-color: white;"}]{style="font-family: inherit;"}

[Что мы тут делаем?]{style="font-family: inherit;"}  
  
[[title Install WinXP SP3 - добавляем в загрузочное меню пункт "]{style="background-color: white; line-height: 20.7999992370605px; white-space: pre-wrap;"}[Install WinXP SP3"]{style="background-color: white; line-height: 20.7999992370605px; white-space: pre-wrap;"}]{style="font-family: inherit;"}  
[[map /winxp.iso (hd32) - Эмулируем CD-Rom из .iso диска]{style="font-family: inherit;"}]{style="background-color: white; line-height: 20.7999992370605px; white-space: pre-wrap;"}  
[[chainloader (hd32) - запускаем загрузчик из образа.]{style="font-family: inherit;"}]{style="background-color: white; line-height: 20.7999992370605px; white-space: pre-wrap;"}  
  
Я буду добавлять подобные блоки для различных ОС.
:::
