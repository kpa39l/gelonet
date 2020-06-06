Title: Отключение адаптивной смены яркости в Windows 10
Date: 2017-11-12 02:13
Author: Краз
Tags: Windows
Slug: windows-10
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
::: {.separator style="clear: both; text-align: center;"}
[![](https://2.bp.blogspot.com/-hTE6rgZGmts/WggYmUO7eBI/AAAAAAAAONs/bVbFEUZS68o0vjHKDljii0uEZhOcTFvGQCLcBGAs/s640/4k-Windows-10-Wallpaper-5.png){width="640" height="400"}](https://2.bp.blogspot.com/-hTE6rgZGmts/WggYmUO7eBI/AAAAAAAAONs/bVbFEUZS68o0vjHKDljii0uEZhOcTFvGQCLcBGAs/s1600/4k-Windows-10-Wallpaper-5.png)
:::

Долгое время не мог понять, что же меня раздражает при активной работе на ноутбуке сWindows 10. Оказалось, что при изменении картинки на экране,  например при смене вкладки браузера со светлой страницы Яндекса на странцу с видео YouTube, происходило адаптивное изменение яркости подсветки экрана. Очень раздражающая штука.  
  
Легко отключить это не получилось, в настройках электропитания уже была отключена.  

::: {.separator style="clear: both; text-align: center;"}
[![](https://1.bp.blogspot.com/-5Se35YR0O1c/Wgga2FULt6I/AAAAAAAAOOI/OMavmKQiErITLSX4MEmjMK7QP4_iLZPkgCLcBGAs/s640/2017-11-12_12-52-59.png){width="640" height="336"}](https://1.bp.blogspot.com/-5Se35YR0O1c/Wgga2FULt6I/AAAAAAAAOOI/OMavmKQiErITLSX4MEmjMK7QP4_iLZPkgCLcBGAs/s1600/2017-11-12_12-52-59.png)
:::

::: {.separator style="clear: both; text-align: center;"}
  
:::

::: {.separator style="clear: both; text-align: left;"}
Поэтому пришлось лезть глубже. Оказалось, что проблема известная и связана сдрайверами видеоадптеров. В частности в моем случае пришлось для интегрированной видеокарты изменить драйвер на стандартный от Microsoft, потому что обновление драйвера от ATI не принесло результата. 
:::

::: {.separator style="clear: both; text-align: left;"}
  
:::

::: {.separator style="clear: both; text-align: left;"}
Делается это в диспетчере устройств. Правой клавишей на видеоадаптере, из контекстного меню выбираем пункт "Обновить драйвер..." \>  "Выполнить поиск драйверов на этом компьютере" \> "Выбрать драйвер из списка доступных драйверов на этом компьютере". Откроется окно выбора драйвера,  в котором выбираем "Базовый видеоадаптер (Microsoft)".
:::

::: {.separator style="clear: both; text-align: center;"}
[![](https://3.bp.blogspot.com/-bzyVUB2hjt0/Wgged3g0FBI/AAAAAAAAOOU/bxCHsMSLF7o_W9nJSwdKmvIwiAD_37nQwCLcBGAs/s640/2017-11-12_13-09-26.png){width="640" height="428"}](https://3.bp.blogspot.com/-bzyVUB2hjt0/Wgged3g0FBI/AAAAAAAAOOU/bxCHsMSLF7o_W9nJSwdKmvIwiAD_37nQwCLcBGAs/s1600/2017-11-12_13-09-26.png)
:::

::: {.separator style="clear: both; text-align: left;"}
  
:::

::: {.separator style="clear: both; text-align: left;"}
Во время установки драйвера экран будет выключаться на несколько секунд. В моем случае раздражающая адаптивная регулировка яркости подсветка отключилась сразу и перезагрузка не понадобилась.
:::

::: {.separator style="clear: both; text-align: left;"}
  
:::
:::
