Title: Установка проприетарного драйвера AMD/ATI Catalyst
Date: 2016-01-21 10:59
Author: Краз
Tags: Debian, Linux
Slug: amdati-catalyst
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
::: {.separator style="clear: both; text-align: center;"}
[![](http://1.bp.blogspot.com/-epb74unkcN8/VqEqo6ebAYI/AAAAAAAANE0/6wsSoKG2rqk/s320/ATI-Radeon-HD-5670.png){width="320" height="261"}](http://1.bp.blogspot.com/-epb74unkcN8/VqEqo6ebAYI/AAAAAAAANE0/6wsSoKG2rqk/s1600/ATI-Radeon-HD-5670.png)
:::

  
Мне повезло разжиться настоящей дискретной видеокартой для своего домашнего настольного компьютера. Вполне так себе вменяемая дешёвая карта даже с двумя выходами и системой охлаждения.  
  
Определил версию платы с помощью команды:  

> kpa39l\@dws:\~\$ lspci \| grep -i VGA  
> 01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. \[AMD/ATI\] Redwood XT \[Radeon HD 5670/5690/5730\]

<div>

Вывод команды содержит полное название Redwood XT \[Radeon HD 5670/5690/5730\]. Какая именно из версий у меня в руках не знаю, да мне это и не важно в разрезе установки драйверов.

</div>

  
Скачать последнюю версию драйверов можно с [официального портала поддержки AMD/ATI](http://support.amd.com/ru-ru/download). Для GNU/Linux драйвера поставляются в трёх видах для RHEL, Ubuntu  и универсальный исполняемый файл в архиве zip.  Как раз последний я и скачал, мне досталась версия 15.21.1151.  
  
Перед установкой драйвера необходимо установить заголовки ядра, если они ещё не стоят:  

> sudo aptitude search linux-headers-\$(uname -r)

Процесс будет схож с тем что изображено на снимке экрана ниже.  

::: {.separator style="clear: both; text-align: center;"}
[![](http://4.bp.blogspot.com/-iUOALqP1Fy0/VqEZfSPjvmI/AAAAAAAANEY/Wk4ssoeYWkc/s320/7_Linux-Headers_Install.png){width="320" height="121"}](http://4.bp.blogspot.com/-iUOALqP1Fy0/VqEZfSPjvmI/AAAAAAAANEY/Wk4ssoeYWkc/s1600/7_Linux-Headers_Install.png)
:::

  
Теперь переходим непосредственно к установке драйвера. Добываем файл из архива:  

> unzip amd-catalyst-15.9-linux-installer-15.201.1151-x86.x86\_64.zip 

<div>

Файл извлечётся в ту же папку. Расширение файла .run.

</div>

  
Помечаем файл как исполняемый:  

> chmod +x AMD-Catalyst-15.9-Linux-installer-15.201.1151-x86.x86\_64.run 

И запускаем его от имени суперпользователя:  

>  sudo sh AMD-Catalyst-15.9-Linux-installer-15.201.1151-x86.x86\_64.run 

::: {.separator style="clear: both; text-align: center;"}
[![](http://3.bp.blogspot.com/-0xTI0iOPkl4/VqEYT5O6TPI/AAAAAAAAND4/w8NjpXeo5c8/s320/0_ATI_Driver_Install_Start.png){width="320" height="203"}](http://3.bp.blogspot.com/-0xTI0iOPkl4/VqEYT5O6TPI/AAAAAAAAND4/w8NjpXeo5c8/s1600/0_ATI_Driver_Install_Start.png)
:::

<div>

  

</div>

<div>

Далее запускается графический установщик. Ниже снимки экранов установки в простейшем случае. Если у вас возникнут сложности то я всегда готов дополнительно пояснить и рассказать о втором, не автоматическом варианте установки.

</div>

::: {.separator style="clear: both; text-align: center;"}
[![](http://3.bp.blogspot.com/-nH3ePJcTyOo/VqEYT1JHNII/AAAAAAAANEU/QBNhfg_r4YY/s320/1_ATI_Driver_Setup.png){width="320" height="272"}](http://3.bp.blogspot.com/-nH3ePJcTyOo/VqEYT1JHNII/AAAAAAAANEU/QBNhfg_r4YY/s1600/1_ATI_Driver_Setup.png)
:::

::: {.separator style="clear: both; text-align: center;"}
[![](http://1.bp.blogspot.com/-YqbQ__tBvXs/VqEYVPby07I/AAAAAAAANEQ/efV_iSa0rwE/s320/ATI_Driver_Install_EULA.png){width="320" height="252"}](http://1.bp.blogspot.com/-YqbQ__tBvXs/VqEYVPby07I/AAAAAAAANEQ/efV_iSa0rwE/s1600/ATI_Driver_Install_EULA.png)
:::

::: {.separator style="clear: both; text-align: center;"}
[![](http://2.bp.blogspot.com/-X4U4FgVscm0/VqEYTxapeAI/AAAAAAAANEE/-lII4noIfuU/s320/3_ATI_Driver_Install_Instalation_mode.png){width="320" height="281"}](http://2.bp.blogspot.com/-X4U4FgVscm0/VqEYTxapeAI/AAAAAAAANEE/-lII4noIfuU/s1600/3_ATI_Driver_Install_Instalation_mode.png)
:::

::: {.separator style="clear: both; text-align: center;"}
[![](http://2.bp.blogspot.com/-U6VJdAAoXzU/VqEYUWu2k6I/AAAAAAAANEM/odPFOZsZans/s320/4_ATI_Driver_Install_Instalation_process.png){width="320" height="281"}](http://2.bp.blogspot.com/-U6VJdAAoXzU/VqEYUWu2k6I/AAAAAAAANEM/odPFOZsZans/s1600/4_ATI_Driver_Install_Instalation_process.png)
:::

::: {.separator style="clear: both; text-align: center;"}
[![](http://4.bp.blogspot.com/-Kwb1MTiaAdU/VqEYUmBdjEI/AAAAAAAAND8/mEHFnCHyvEA/s320/5_ATI_Driver_Install_Instalation_process_freeze.png){width="320" height="281"}](http://4.bp.blogspot.com/-Kwb1MTiaAdU/VqEYUmBdjEI/AAAAAAAAND8/mEHFnCHyvEA/s1600/5_ATI_Driver_Install_Instalation_process_freeze.png)
:::

::: {.separator style="clear: both; text-align: center;"}
[![](http://4.bp.blogspot.com/-Jrgvej2cmg8/VqEYU8I56GI/AAAAAAAANEA/Se4F4gXoskI/s320/6_ATI_Driver_Install_End_installation.png){width="320" height="281"}](http://4.bp.blogspot.com/-Jrgvej2cmg8/VqEYU8I56GI/AAAAAAAANEA/Se4F4gXoskI/s1600/6_ATI_Driver_Install_End_installation.png)
:::

<div>

  

</div>

<div>

Закрываем графический мастер установки. Система сообщит нам о том. что нужно перезагрузиться. Идём в перезагрузку:

</div>

<div>

> sudo shutdown -r now

</div>

<div>

И теперь можем запустить AMD Catalyst Control Center Хоть из меню, хоть из консоли:

</div>

> sudo aticonfig

::: {.separator style="clear: both; text-align: center;"}
[![](http://4.bp.blogspot.com/-yNepC8_yx70/VqEbbaIy9II/AAAAAAAANEk/U6r_bWpDUtc/s320/8_Menu.png){width="320" height="306"}](http://4.bp.blogspot.com/-yNepC8_yx70/VqEbbaIy9II/AAAAAAAANEk/U6r_bWpDUtc/s1600/8_Menu.png)
:::

::: {.separator style="clear: both; text-align: left;"}
  
:::

::: {.separator style="clear: both; text-align: left;"}
После установки нового ядра. Потребуется обновить модуль ядра командами:
:::

::: {.separator style="clear: both; text-align: left;"}
  
:::

::: {.separator style="clear: both; text-align: left;"}
Для видеокарт ATI есть ещё свободный драйвер. Если проприетарный драйвер вдруг по каким-то причинам будет работать неудовлетворительно, то можно установить и его.
:::

::: {.separator style="clear: both; text-align: left;"}
  
:::

::: {.separator style="clear: both; text-align: left;"}
Как всегда при любых вопросах или непонятных моментах можно обращаться ко мне по [kpa39l\@yandex.ru.](http://kpa39l@yandex.ru./)
:::

::: {.separator style="clear: both; text-align: left;"}
  
:::
:::
