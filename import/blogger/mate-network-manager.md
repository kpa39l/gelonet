Title: Добавление на рабочий стол Mate апплета Network Manager для контроля сетевого подключения
Date: 2014-11-16 04:45
Author: Краз
Tags: Linux, Mate, Gnome, Настройка
Slug: mate-network-manager
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
::: {style="border: 0px; margin-bottom: 1em; padding: 0px;"}
::: {style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
Недавно перешёл на новую, пока ещё тестовую, версию Debian Jessie (номер версии - 8, если не ошибаюсь). Первое с чем столкнулся после загрузки, так это то, что в системном лотке не было апплета контроля сетевого соединения которое ставит Network Manager. А я настолько привык к этому графическому инструменты, что каждый раз при открытии консоли испытывал жутчайший дискомфорт.
:::

::: {style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
  
:::

::: {style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
Достаточно быстро было найдено следующее решение:
:::

::: {style="text-align: left;"}
[Открываем консоль]{style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}  
[Переустанавливаем пакеты network-manager и network-manager-gnome:]{style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
:::

::: {style="text-align: left;"}
:::

> [sudo aptitude install --reinstall network-manager network-manager-gnome]{style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}

[[  
]{style="font-size: 14px; line-height: 21px;"}]{style="color: #646464; font-family: Proxima Nova Regular, Helvetica Neue, Arial, Helvetica, sans-serif;"}[Настраиваем управление сетевыми подключениями Network Manager-у. В файле конфигурации /etc/NetworkManager/NetworkManager.conf меняем параметр ]{style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}[ "managed=false" на "managed=true"]{style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
:::

::: {style="border: 0px; margin-bottom: 1em; padding: 0px;"}
> [[sudo nano /etc/NetworkManager/NetworkManager.conf]{style="font-size: 14px; line-height: 21px;"}]{style="color: #646464; font-family: Proxima Nova Regular, Helvetica Neue, Arial, Helvetica, sans-serif;"}

[[  
]{style="font-size: 14px; line-height: 21px;"}]{style="color: #646464; font-family: Proxima Nova Regular, Helvetica Neue, Arial, Helvetica, sans-serif;"}[Проверяем, чтобы настройки сетевых интерфейсов не были описаны в /etc/network/interfaces. Имеющиеся настройки можно просто закомментировать. В большинстве случаев в файле должны остаться только строки:]{style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
:::

> [auto lo]{style="color: #646464; font-family: monospace; font-size: 14px; line-height: 21px;"}[iface lo ]{style="color: #646464; font-family: monospace; font-size: 14px; line-height: 21px;"}[inet loopback]{style="color: #646464; font-family: monospace; font-size: 14px; line-height: 21px;"}

::: {style="border: 0px; margin-bottom: 1em; padding: 0px;"}
[И, наконец, перезапускаем сетевую подсистему:]{style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
:::

::: {style="border: 0px; margin-bottom: 1em; padding: 0px;"}
[[sudo service networking restart]{style="font-size: 14px; line-height: 21px;"}]{style="color: #646464; font-family: Proxima Nova Regular, Helvetica Neue, Arial, Helvetica, sans-serif;"}  

::: {style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
  
:::

::: {style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
После этого апплет должен появиться, если этого не случилось, то можно попробовать один из нижеперечисленных рецептов:
:::

::: {style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
  
:::

::: {style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
В файле /etc/xdg/autostart/nm-applet.desktop удалить строку AutostartCondition=GNOME3 и перезагрузить сетевую подсистему.
:::

::: {style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
или
:::

::: {style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
Удалить файл состояния описывающий статус Network Manager-а:
:::

> sudo rm /ver/lib/NetworkManager/NetworkManager.state

::: {style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
или
:::

::: {style="color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px;"}
Перезапустить X сессию или же просто перезагрузить компьютер.
:::
:::

::: {style="border: 0px; color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px; margin-bottom: 1em; padding: 0px;"}
[Источник](http://thesave.altervista.org/2014/02/network-manager-applet-for-mate-desktop-installing-it-right/)
:::

::: {style="border: 0px; color: #646464; font-family: 'Proxima Nova Regular', 'Helvetica Neue', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 21px; margin-bottom: 1em; padding: 0px;"}
  
:::

::: {style="border: 0px; margin-bottom: 1em; padding: 0px;"}
  
:::
:::
