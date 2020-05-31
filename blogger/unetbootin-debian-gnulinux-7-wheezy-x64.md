Title: Unetbootin на Debian Gnu/Linux 7 Wheezy x64
Date: 2014-12-22 02:50
Author: Краз
Slug: unetbootin-debian-gnulinux-7-wheezy-x64
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
::: {.separator style="clear: both; text-align: center;"}
[![](http://1.bp.blogspot.com/-EClhXCtAg84/VJf2GZi0mAI/AAAAAAAAK5Y/5Q7wotx2mWk/s1600/icon.png){width="200" height="200"}](http://sourceforge.net/projects/unetbootin/?source=navbar)
:::

  
На 64-битных системам [Unetbootin](http://sourceforge.net/projects/unetbootin/?source=navbar) сразу после скачивания исполняемого файла не запускается. Ругается на отсутствие нужных библиотек.Поэтому для запуска нужно просто установить отсутствующие пакеты и, если не подключена архитектура i386, то подключаем её:  

> \# dpkg --add-architecture i386

и ставим нужные версии пакетов:  
  

> \# aptitude install libxrandr2:i386 libfontconfig:i386 mtools

  
Вуаля. Теперь всё заработает.  
  
Как обычно, если у тебя что-то не получается или что-то непонятно ты можешь задать мне вопрос или попросить помощи через комментарии или по моему почтовому [адресу kpa39l\@yandex.ru.](mailto:kpa39l@yandex.ru)
:::
