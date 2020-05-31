Title: Как восстановить MBR Windows раздела из-под WIndows
Date: 2014-08-06 10:12
Author: Краз
Tags: Linux, Добрые советы
Slug: mbr-windows-windows
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
Есть у меня загрузочная флешка с WIndows. Но после очередного залитого образа с неё перестал грузиться инсталятор. Всё дело было в повреждённой записи MBR (Master boot record). Под Windows я то легко смог восстановить загрузочную запись командой из консоли ["fdisk /mbr", но как быть если у меня нет под рукой установленной Windows?]{style="background-color: white;"}  
[  
]{style="background-color: white;"}[Для этой цели проще всего использовать программу [ms-sys](http://ms-sys.sourceforge.net/).]{style="background-color: white;"}  
[  
]{style="background-color: white;"}[К сожалению, пакетов разработчики не собирают. Но собрать эту программу проще простого.]{style="background-color: white;"}  

``` {style="background-color: black; color: white;"}
Usage:
 ms-sys [options] [device]
Options:
    -1, --fat12     Write a FAT12 floppy boot record to device
    -2, --fat32nt   Write a FAT32 partition NT boot record to device
    -3, --fat32     Write a FAT32 partition DOS boot record to device
    -4, --fat32free Write a FAT32 partition FreeDOS boot record to device
    -5, --fat16free Write a FAT16 partition FreeDOS boot record to device
    -6, --fat16     Write a FAT16 partition DOS boot record to device
    -n, --ntfs      Write a NTFS partition Windows 7 boot record to device
    -l, --wipelabel Reset partition disk label in boot record
    -p, --partition Write partition info (hidden sectors, heads and drive id)
                    to boot record
    -H, --heads  Manually set number of heads if partition info is written
    -7, --mbr7      Write a Windows 7 MBR to device
    -i, --mbrvista  Write a Windows Vista MBR to device
    -m, --mbr       Write a Windows 2000/XP/2003 MBR to device
    -9, --mbr95b    Write a Windows 95B/98/98SE/ME MBR to device
    -d, --mbrdos    Write a DOS/Windows NT MBR to device
    -s, --mbrsyslinux    Write a syslinux MBR to device
    -t, --mbrgptsyslinux Write a syslinux GPT MBR to device
    -z, --mbrzero   Write an empty (zeroed) MBR to device
    -f, --force     Force writing of boot record
    -h, --help      Display this help and exit
    -v, --version   Show program version
    -w, --write     Write automatically selected boot record to device

    Default         Inspect current boot record

Warning: Writing the wrong kind of boot record to a device might
destroy partition information or file system!
     
```

[Пользоваться тоже. Например, для запись MBR Windows 7 достаточно выполнить следующую команду:]{style="background-color: white;"}  

> [ms-sys -7 /dev/sde]{style="background-color: white; color: #222222; font-family: Menlo, Monaco, 'Courier New', monospace; font-size: 13px; line-height: 20.799999237060547px;"}

[[Где /dev/sde это моя флэшка.]{style="background-color: white; line-height: 20.799999237060547px;"}]{style="color: #222222; font-family: Menlo, Monaco, Courier New, monospace; font-size: x-small;"}  
[  
]{style="background-color: white;"}
:::
