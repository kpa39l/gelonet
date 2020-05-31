Title: Удалить Windows Store
Date: 2017-10-21 10:31
Author: Краз
Tags: PowerShell, Windows
Slug: windows-store
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
[![](https://3.bp.blogspot.com/-qunXRw-HdWk/Wet-UapUxrI/AAAAAAAAOJ4/X4a7IljpKTkKLr_JGHyVfLXuvyeQi3YeQCK4BGAYYCw/s640/windows-store-05_story.jpg){width="640" height="340"}](http://3.bp.blogspot.com/-qunXRw-HdWk/Wet-UapUxrI/AAAAAAAAOJ4/X4a7IljpKTkKLr_JGHyVfLXuvyeQi3YeQCK4BGAYYCw/s1600/windows-store-05_story.jpg)  
Как-то так сложилось, что я не устанавливаю приложения из Windows Store. А системные службы регулярно мешают мне работать создавая нагрузку на диск или процессор в виде сервиса wsappx. Поэтому пришло в голову удалить этот магазин из системы.  
  
Выполнить это можно из консоли powershell в 3 шага:  
  

1.  Команда "Get-AppxPackage \*windowsstore\* \| Remove-AppxPackage", не забываем про автодополнение команд с помощью клавиши Tab.
2.  ?????
3.  Результат!

<div>

Как результат система быстрее запускается и меньше тормозит. Кстати, Очень полезно бывает отключить все живые плитки, чтобы коварная служба wsappx не тормозила работу. В той же консоли PowerShell вводим:

</div>

> Set-ItemProperty -Path "HKCU:/Software/Policies/Microsoft/Windows/CurrentVersion/PushNotifications" -Name "NoTileApplicationNotification" –Value "1"

<div>

  

</div>

<div>

Так же до кучи можем очистить кэш плиток командой:

</div>

<div>

<div>

  

</div>

> Set-ItemProperty -Path "HKCU:/SOFTWARE/Policies/Microsoft/Windows/Explorer" -Name "ClearTilesOnExit" -Value "1"

<div>

Конечно всё это можно запихнуть в сценарий, но надо ли?

</div>

</div>
:::
