Title: Установка загрузчика на USB диск
Date: 2014-10-16 08:06
Author: Краз
Tags: BootFlashTool
Slug: usb
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
Главное в загрузочной флэшке не то, какие программы или образы мы можем запустить, а то что она вообще загрузочная (спасибо, Кэп). Соответственно без загрузчика все перечисленные мною раньше полезные и не очень образы будут просто файлами и никак помочь в деле установки или ремонта операционной системы мне не смогут.  
  
Поскольку, помимо GNU/Linux мне хотелось бы иметь возможность загружать и использовать Windows компоненты, то мне ничего не мешает на первый взгляд использовать как привычный GRUB 2, так и его ответвление GRUB4DOS. Но правда в таком случае первыичная настройка GRUB2 будет немного сложней (как мне кажется на вскидку), а по второму варианту в Сети куча мануалов для чайников и прочих приятных возможностей. Поэтому в перовм приближении на этом варианте и остановлюсь. При том, что у большинства наверняка стоит именно Windows.  
  
Итак, GRUB4DOS.  

> [GRUB4DOS is an universal boot loader based on GNU GRUB. It can boot off DOS/LINUX, or via Windows boot manager/syslinux/lilo, or from MBR/CD. It also has builtin BIOS disk emulation, ATAPI CDROM driver, etc.]{style="background-color: white; font-family: sans-serif;"}

или  

> [GRUB4DOS это универсальный загрузчик основанный на GNU GRUB. Он может загружаться из DOS/LINUX, или через менеджер загрузки Windows/syslinux/lilo, или из MBR/CD. В нём так же есть встроенные эмуляция диска в БИОС, ATAPI драйвер CDROM и прочие полезности.]{style="background-color: white; font-family: sans-serif;"}

Официальная страница проекта : <https://gna.org/projects/grub4dos>. А вот последних версий там нет и скачивать их необходимо вот [отсюда](http://code.google.com/p/grub4dos-chenall/downloads/list) (спасибо китайским товарищам).  
  

### Установка {#установка style="text-align: left;"}

::: {style="text-align: left;"}
#### **Установка из-под Windows** {#установка-из-под-windows style="text-align: left;"}
:::

Именно для загрузочного USB диска в подавляющем большинстве случаев загрузчик будет устанавливаться в MBR (Главную Загрузочную Запись).  
Для этого есть как удобная графическая [утилита](http://greenflash.su/Files/Grub4DoS_GUI.zip), где всё просто и понятно - Для быстрой и простой установки достаточно выбрать диск на который в MBR нужно установить загрузчик и нажать кнопку "Install";  
так и в ручную не прибегая к сторонним утилитам - В состав архива с загрузчиком входит утилита bootlace.com и её 64-битная версия bootlace64.com.  
  
Использование утилиты хорошо описано в статье [Установка Grub4DOS](http://greenflash.su/publ/14-1-0-3).  
Я же подробнее остановлюсь на ручном методе установки загрузчика в MBR с использованием bootlace.com.  
  

#### **Установка из-под GNU/Linux Debian** {#установка-из-под-gnulinux-debian style="text-align: left;"}

Нам нужна утилита bootlace.com, которая идёт в составе [поставки](http://sourceforge.net/projects/grub4dos/) grub4dos. Если пользоваться будем не один раз, то имеет смысл после распаковки скопировать эту утилиту в системную директорию /bin.  
Находим свою флэшку пользуясь выводом команды  

> sudo fdisk -l

С помощью того же fdisk создаём раздел, если ntfs то нужно после создания раздела поменять его id на 7. А после чего с помощью команды  

> mkntfs -Q -v -L "ИмяРаздела" /dev/sdX1

создать файловую систему.  
  
Далее командой  

> sudo bootlace.com /dev/sde

устанавливаем загрузчик в MBR USB-диска.  
  
После установки загрузчика в MBR копируем файлы grldr и menu.lst в корень раздела.  
  
Всё после этого можно переходить к добавлению своих пунктов к загрузочному меню.  

### Источники информации {#источники-информации style="text-align: left;"}

[GRUB всемогущий, или Делаем загрузочную флешку](http://habrahabr.ru/post/99159/) - Автор: ; Дата публикации:  .  
[Создание мультизагрузочного USB HDD или флешки](http://habrahabr.ru/post/124482/) - Автор: ; Дата публикации:  .  
[Загрузчик Grub4DOS, как пользоваться, установка, возможности](http://u-proga.net/servitiva/zagruzcic-grub4dos/) - Автор: ; Дата публикации:  .  
[Создание загрузочных iso-образов на основе загрузчика grub4dos](http://rutracker.org/forum/viewtopic.php?t=2315172)  

::: {style="text-align: left;"}
[Установка Grub4DOS](http://greenflash.su/publ/14-1-0-3) - Автор: ATF; Дата публикации:  2008.03.04.  
[Установка grub4dos в ОС на базе linux](http://greenflash.su/publ/ustanovka_grub4dos_v_os_na_baze_linux/4-1-0-181) - Автор: [ ]{style="background-color: white; color: #1a1a1a; font-family: Tahoma, Arial, sans-serif; font-size: 11px;"}М\@ксим; Дата публикации: 2011.06.12[[.]{style="background-color: white; font-size: 11px;"}]{style="color: #1a1a1a; font-family: Tahoma, Arial, sans-serif;"}
:::

  
:::
