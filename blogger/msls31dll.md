Title: Проблема с msls31.dll
Date: 2015-01-09 14:22
Author: Краз
Slug: msls31dll
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
В один прекрасный днл появилась у меня пробелма с кнопкой "Пуск" в моей Win7 x64 Домашняя. При нажатии на кнопку у меня стало появляться сообщение об отсутствии файла msls31.dll. Из-за чего множество программ интерфейс которых использует вэб-содержимое, например Google Drive или Google Picasa, перестали работать из-за того что не отображались никакие элементы интерфейса. ни кнопки, ни поля.  

<div>

  

</div>

<div>

Поиск решений в Сети дал несколько, совсем немного, веток с упоминанием моей ошибки суть которых сводилась к тому, что это проблема связана с неправильным процессом обновления Internet Explorer-а. Все рецепты указанные в этих ветках, включая FixIt и редактирование реестра не привели к решению проблемы.  
  
В итоге, проблема решилась сбросом всех настроек IE к первоначальному виду. Далее будут скриншоты на моей русский Windows 7 Home x64, но для всех остальных версий Windows и IE (начиная с 9-ой) этапы будут теми же самыми.  
  
Как сбросить все настройки? Очень просто:  
  
Запускаем IE.  

::: {.separator style="clear: both; text-align: center;"}
:::

  
  
В меню Настроек щёлкаем на пункт "Свойства браузера".  

::: {.separator style="clear: both; text-align: center;"}
[![](http://2.bp.blogspot.com/-LarbkcQucVI/VLBT7gfJR4I/AAAAAAAALBU/V8ivNkrddj8/s1600/2015-01-10%2B01-06-56%2B%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2B%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0.png){width="320" height="285"}](http://2.bp.blogspot.com/-LarbkcQucVI/VLBT7gfJR4I/AAAAAAAALBU/V8ivNkrddj8/s1600/2015-01-10%2B01-06-56%2B%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2B%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0.png)
:::

  
Переходим на вкладку "Дополнительно". И нажимаем кнопку "Сброс".  

::: {.separator style="clear: both; text-align: center;"}
[![](http://4.bp.blogspot.com/-U1IbQFKyJYQ/VLBT7mTssXI/AAAAAAAALBg/_Wzg6ZSQY0Q/s1600/2015-01-10%2B01-09-18%2B%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2B%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0.png){width="253" height="320"}](http://4.bp.blogspot.com/-U1IbQFKyJYQ/VLBT7mTssXI/AAAAAAAALBg/_Wzg6ZSQY0Q/s1600/2015-01-10%2B01-09-18%2B%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2B%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0.png)
:::

  
В открывшемся окне сброса параметров, ставим галку напротив очистки персональных настроек и нажимаем кнопку "Сброс"  

::: {.separator style="clear: both; text-align: center;"}
[![](http://1.bp.blogspot.com/-wO2gSXaG5ec/VLBT7q5EvUI/AAAAAAAALBw/0FyoLETD314/s1600/2015-01-10%2B01-17-27%2B%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2B%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0.png){width="320" height="183"}](http://1.bp.blogspot.com/-wO2gSXaG5ec/VLBT7q5EvUI/AAAAAAAALBw/0FyoLETD314/s1600/2015-01-10%2B01-17-27%2B%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2B%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0.png)
:::

После окончания процесса сброса настроек можно нажать кнопку "Закрыть" и перезагрузить компьютер.  

::: {.separator style="clear: both; text-align: center;"}
[![](http://1.bp.blogspot.com/-iinV7cF_FF0/VLBT73hsCEI/AAAAAAAALBk/AzH3t6dJRKg/s1600/2015-01-10%2B01-18-20%2B%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2B%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0.png){width="320" height="189"}](http://1.bp.blogspot.com/-iinV7cF_FF0/VLBT73hsCEI/AAAAAAAALBk/AzH3t6dJRKg/s1600/2015-01-10%2B01-18-20%2B%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2B%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0.png)
:::

  
  
Вот таким нехитрым путём решил свою проблему с ошибками библиотеки msls31.dll. Надеюсь, этот простой метод подойдёт и Вам.  
  

</div>
:::
