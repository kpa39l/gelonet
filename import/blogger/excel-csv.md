Title: Excel и CSV файлы
Date: 2015-01-13 00:53
Author: Краз
Tags: Microsoft, Office, Добрые советы, Excel
Slug: excel-csv
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
::: {.separator style="clear: both; text-align: center;"}
[![](http://4.bp.blogspot.com/-tjXznRI7ucU/VLTN6wvJ57I/AAAAAAAALCI/H21lZxLSCEU/s1600/microsoft-excel-2013-06-535x535.png){width="320" height="320"}](http://4.bp.blogspot.com/-tjXznRI7ucU/VLTN6wvJ57I/AAAAAAAALCI/H21lZxLSCEU/s1600/microsoft-excel-2013-06-535x535.png)
:::

  

::: {style="text-align: justify;"}
Столкнулся с парадоксальной , на мой взгляд, проблемой. MS Excel 2007-2013 не хочет открывать файлы CSV (Comma Separated Values - Файл с разделителями параметров). Точнее открывает, но как простые TXT файлы сбрасывая каждую строку в первую ячейку и не разделяя на значения. Как выяснилось происходит это от того, что разделитель по-умолчанию привязали к разделителю в языковых настройках системы, чем в Русской версии является  ; (точка с запятой).
:::

  
Решить проблему можно несколькими способами, но исключив недалёкие из серии заменить все запятые на точки с запятой, можно выделить два основных:  
  
Первый. Создать новый файл в Excel. И в новом пустом файле перейти на вкладку "Данные" ленты - "Получить внешние данные" - "Из текста". Откроется очень простой мастер импорта данных, в котором можно указать кодировку файла, тип данных для столбцов и, естественно, символ разделителя.  

::: {.separator style="clear: both; text-align: center;"}
[![](http://3.bp.blogspot.com/-DKipm9b5Xyo/VLTckUcXHGI/AAAAAAAALCg/degsb2HvcTM/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-4.png){width="320" height="133"}](http://3.bp.blogspot.com/-DKipm9b5Xyo/VLTckUcXHGI/AAAAAAAALCg/degsb2HvcTM/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-4.png)
:::

  

::: {.separator style="clear: both; text-align: center;"}
[![](http://2.bp.blogspot.com/-r3wGIW6Y9bc/VLTclpJzjRI/AAAAAAAALCs/5KNqfXRi39o/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA.png){width="320" height="140"}](http://2.bp.blogspot.com/-r3wGIW6Y9bc/VLTclpJzjRI/AAAAAAAALCs/5KNqfXRi39o/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA.png)
:::

  

::: {.separator style="clear: both; text-align: center;"}
[![](http://3.bp.blogspot.com/-z3TuSDOdPfE/VLTcr5CWj6I/AAAAAAAALDQ/ogHjJBJ4Blo/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-1.png){width="320" height="140"}](http://3.bp.blogspot.com/-z3TuSDOdPfE/VLTcr5CWj6I/AAAAAAAALDQ/ogHjJBJ4Blo/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-1.png)
:::

  

::: {.separator style="clear: both; text-align: center;"}
[![](http://1.bp.blogspot.com/-1m7qx5qGta4/VLTck9Y1o-I/AAAAAAAALCk/Be_jKE2As2U/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-7.png){width="320" height="158"}](http://1.bp.blogspot.com/-1m7qx5qGta4/VLTck9Y1o-I/AAAAAAAALCk/Be_jKE2As2U/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-7.png)
:::

::: {.separator style="clear: both; text-align: center;"}
[![](http://4.bp.blogspot.com/-oSgbqNpNN7Y/VLTcr_8PI0I/AAAAAAAALDY/p5mWUb0Z13Q/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-3.png){width="320" height="140"}](http://4.bp.blogspot.com/-oSgbqNpNN7Y/VLTcr_8PI0I/AAAAAAAALDY/p5mWUb0Z13Q/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-3.png)
:::

  
Второй. Открыть файл Блокнотом и добавить в начало файлу строку "sep=,". Которая указывает, что разделителем (separator)в файле является запятая. После этого никаких других действий для открытия файла уже предпринимать не придётся.  

::: {.separator style="clear: both; text-align: center;"}
[![](http://1.bp.blogspot.com/-S-7XHCq0p4E/VLTckd0dlgI/AAAAAAAALCY/SQTi66HsieQ/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-5.png){width="320" height="149"}](http://1.bp.blogspot.com/-S-7XHCq0p4E/VLTckd0dlgI/AAAAAAAALCY/SQTi66HsieQ/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-5.png)
:::

  

::: {.separator style="clear: both; text-align: center;"}
[![](http://3.bp.blogspot.com/-yHz9XLttBJo/VLTckRCI4vI/AAAAAAAALCc/QJNJ0plQhLc/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-6.png){width="320" height="149"}](http://3.bp.blogspot.com/-yHz9XLttBJo/VLTckRCI4vI/AAAAAAAALCc/QJNJ0plQhLc/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-6.png)
:::

  

::: {.separator style="clear: both; text-align: center;"}
[![](http://1.bp.blogspot.com/-G4yu662kEwY/VLTclAWS7GI/AAAAAAAALDA/6heUXExeLHY/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-8-%D0%98%D0%BC%D0%BF%D0%BE%D1%80%D1%82.png){width="320" height="157"}](http://1.bp.blogspot.com/-G4yu662kEwY/VLTclAWS7GI/AAAAAAAALDA/6heUXExeLHY/s1600/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA-8-%D0%98%D0%BC%D0%BF%D0%BE%D1%80%D1%82.png)
:::

  
Естественно, мой выбор - второй вариант. Быстрее и проще, а результат тот же.
:::
