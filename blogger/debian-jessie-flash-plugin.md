Title: Debian Jessie + Flash Plugin в Яндекс.Браузере
Date: 2016-12-26 11:36
Author: Краз
Slug: debian-jessie-flash-plugin
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
В Iceweasel после установки  
flahplugin-nonfree  
pepperflashplugin-nonfree  
всё замечательно работает.  
  
А в Хроме и Яндекс.Браузере нет. Причём в Я.Б нет даже такого плагина в списке на странице browser://plugins. В Хроме на странице chrome://plugins всё есть и даже включено, но всё равно не работает.  
  
Каталог /usr/lib/pepperflashplugin-nonfree пуст за исключением файла с открытом ключом.  
  
При установке пакетов через aptitude или с помощью update-pepperflashpluin-nonfree --install  пакет скачивается и ставится, но ссылается что файл собственно с библиотекой плагина недоступен:  
  
mv: не удалось выполнить stat для «unpackchrome/opt/google/chrome/PepperFlash/libpepflashplayer.so»: Нет такого файла или каталога  

<div>

  

</div>

<div>

Что делаем для исправления ситуации.

</div>

<div>

  

</div>

<div>

Удаляем полностью chrome.

</div>

<div>

Удаляем полностью пакеты pepperflashplugin-nonfree и flashplugin-nonfree.

</div>

<div>

  

</div>

<div>

При установке пакетов получаем сообщение что управлять одной из нескольких реализаций флэша можно воспользоваться командой:

</div>

update-alternatives --auto flash\_mozilla.so  
Для того чтобы вручную выбрать одну из реализаций плагина нужно воспользоваться командой  
update-alternatives --config flash\_mozilla.so  
  
Но это не понадобилось, поскольку всё заработало =) В Яндекс.Браузере по крайней мере.  
Ставим сверху Chrome. В списке плагинов Флэш есть, он включен, но киношки не показывает.  
  
Пробуем запускать Хром с параметрами командной строки:  
/usr/bin/chromium --ppapi-flash-path=/usr/lib/pepperflashplugin-nonfree/libpepflashplayer.so --ppapi-flash-verson=24.0.0.186  
  
Версию плагина можно узнать командой:  
sudo update-peperflshplugin-nonfree --status  
  
  
:::
