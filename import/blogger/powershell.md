Title: Удаление службы с помощью Powershell
Date: 2017-11-04 08:47
Author: Краз
Tags: PowerShell
Slug: powershell
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
::: {.separator style="clear: both; text-align: center;"}
[![](https://1.bp.blogspot.com/-qy4P9gMhUuU/Wf3c1qlOIEI/AAAAAAAAOM8/lY2TFPbOIQgthroWPrZFeaq2-5HluVJ8QCLcBGAs/s640/powershell_5_dsc.png){width="640" height="358"}](https://1.bp.blogspot.com/-qy4P9gMhUuU/Wf3c1qlOIEI/AAAAAAAAOM8/lY2TFPbOIQgthroWPrZFeaq2-5HluVJ8QCLcBGAs/s1600/powershell_5_dsc.png)
:::

  
Подхватил недавно Adware которые насоздавал кучу лишних служб, таких как updater.mail.ru. Конечно, в состав Windows 10 входит отличная утилита SC с помощью которой их легко можно удалить:  
  
 sc delete updater.mail.ru.  
  
Но удивил тот факт что в составе Powershell есть командлеты для создания, настройки и управления службами, но вот для удаления нет.  Есть костыли использующие WMI  
  
(Get-WmiObject win32\_service -Filter ″name=′updater.mail.ru′″).delete()  
  
или прямое удаление ветки реестра относящийся к службе в разделе:  
  
HKLM:\\SYSTEM\\CurrentControlSet\\Services\\  
  
но вот командлета нет. Искал на powershelgallery.com и в стандартной поставке. Отличный пример когда соберусь изучать создание командлетов. наверняка это из-за каких-подводных камней. хотя конечно можно просто обёртку для sc.exe написать, что совсем не интересно.
:::
