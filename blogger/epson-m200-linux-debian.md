Title: Установка Epson M200 на Linux Debian
Date: 2014-11-27 21:25
Author: Краз
Slug: epson-m200-linux-debian
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
Драйвера скачиваем с сайта [Epson Download Center](http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX). При всём при том, что Cups увидел моё МФУ через usb сам.  
  
Нам понадобятся:  
  

  ------------- ---------------- ------- -------------------- ----------------------------- -------------- ------------ --
  M200 Series   Printer Driver   Linux   latest               ESC/P Driver (full feature)   All language   12-06-2012   
  M200 Series   Scanner Driver   Linux   Ver. 2.30.0/1.32.0   core package&data package     All language   11-05-2014   
  M200 Series   Scanner Driver   Linux   latest               network plugin package        All language   12-12-2013   
  ------------- ---------------- ------- -------------------- ----------------------------- -------------- ------------ --

  
Настройка Сканера  
Чтобы настроить пакет Image Scan! for Linux нужно внести изменения в файл /etc/sane.d/epkowa.conf. Для этого потребуются права администратора. Файл очень хорошо прокомментирован, так что определить как и для чего изменять каждую опцию очень просто. На всякий случай привожу ниже свой файл конфигурации.  
Так же требуется отключить конфликтующий модуль SANE epson2, закомментировав строку в файле конфигурации /etc/sane.d/dll.conf. Для этого находим строку содержащую "epson2" и меняем её на "\#epson2".  
  
Мой файл конфигурации:  
[]{#more}  

<div>

[[http://download.ebz.epson.net/faq/linux/faq\_ls\_00007.html]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[]{style="color: #333333; font-family: Arial, sans-serif;"}  

<div>

<div>

[[\# epkowa.conf -- sample configuration for the EPKOWA SANE backend]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# Copyright (C) 2004, 2008, 2009  Olaf Meeuwissen]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# See sane-epkowa(5), sane-usb(5) and sane-scsi(5) for details.]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[  
]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# Detect all devices supported by the backend.]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# If you don't have a SCSI device, you can comment out the "scsi"]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# keyword.  Similarly for the other keywords.]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[usb]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#scsi]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[  
]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[  
]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# For any USB scanner not known to the backend (yet), you may, at your]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# own peril(!!), force the backend to recognise and use it via libusb.]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# You can do so by the following configuration command:]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#   usb \<USB vendor ID\> \<USB product ID\>]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# SEIKO EPSON's USB vendor ID is '0x04b8' (without quotes).  In order]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# to find the USB product ID, use lsusb(1).]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# A sample configuration for the Epson Perfection 1650 (Epson GT-8200),]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# which has a product ID of 0x0110, would look as follows:]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[usb 0x04b8 0x08aa]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[  
]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[  
]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# For SCSI devices not detected, you can add an entry like:]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#   scsi EPSON GT-20000]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# where the GT-20000 bit corresponds to the SCSI model information as]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# shown in the output of dmesg(1) or in the /var/log/kern.log file.]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[  
]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[  
]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# Network attached devices may be made to work by first installing the]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# (non-free) iscan-network-nt package and then adding configuration lines]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# as per information below.]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# For each network attached device, you must add an entry as follows:]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#   net \<IP-address\|hostname\> \[port-number\]]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# Ask your network administrator for the device's IP address or check]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# for yourself on the panel (if it has one).  The port-number is very]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# optional and defaults to 1865.]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# Note that network attached devices are not queried unless configured]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# in this file.]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# Examples:]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[net 192.168.1.208 1865]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#net scanner.mydomain.com]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[  
]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[  
]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# Some backend behaviour can be customized by using the option keyword]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# followed by an option name, as shown below.]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#   option \<option-name\>]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# Currently available options:]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\#]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[\# Makes the automatic document feeder the default document source]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

<div>

[[option prefer-adf]{style="font-size: 12px; line-height: 24.9600009918213px;"}]{style="color: #333333; font-family: Arial, sans-serif;"}

</div>

::: {style="line-height: 24.9600009918213px; text-align: left;"}
  
:::

</div>

::: {style="text-align: left;"}
[Узнать сетевое имя МФУ можно распечатав отчёт из меню устройства:]{style="font-family: inherit; line-height: 24.9600009918213px;"}
:::

::: {style="text-align: left;"}
[8. Настройки сети -\> 3. Напечатать лист состояния сети.]{style="font-family: inherit; line-height: 24.9600009918213px;"}
:::

::: {style="text-align: left;"}
[Строка "Host name".]{style="font-family: inherit; line-height: 24.9600009918213px;"}  
  
[  
]{style="font-family: inherit; line-height: 24.9600009918213px;"} [Как всегда, если у вас приведенные настройки не дали положительного результата, не стесняйтесь обращаться. Через комментарии или электронную [почту](mailto:kpa39l@yandex.ru).]{style="font-family: inherit; line-height: 24.9600009918213px;"}
:::
:::
