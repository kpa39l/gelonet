Title: Записываем содержимое файла grldr.mbr на первую дорожку жёсткого диска
Date: 2014-10-16 08:59
Author: Краз
Tags: BootFlashTool, GRUB4DOS, Перевод
Slug: grldrmbr
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
Простой, прямой и быстрый перевод части файла README из поставки универсального загрузчика GRUB4DOS.  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
 grldr.mbr - Записываем содержимое файла на первую дорожку жёсткого диска  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Файл grldr.mbr содержит код, который может быть использован в качестве Master Boot Record (MBR, Главной Загрузочной Записи) жесткого диска. Этот код отвечает за поиск и загрузку все разделов для загрузчика grldr. В настоящее время поддерживаются следующие типы разделов жесткого диска: FAT12/FAT16/FAT32, NTFS, EXT2/EXT3. Логические разделы так же поддерживаются, но тип у содержащих их расширенных разделов должен быть Microsoft совместимым. По факту используемый в Linux тип расширенного раздела (0x85) не полностью проверен в работе механизма поиска разделов.  
  
Как же записать  GRLDR.MBR в Master Boot Track жесткого диска?  
  
Сначала, нужно скопировать метку диска Windows и байты данных о разделе (всего 72 байта из сектора MBR, начиная со смещения 0x01b8 до 0x01ff) и поместить их в тот же диапазон данных с 0x01b8 до 0x01ff в начале сохранённого в файл GRLDR.MBR сектора.  
  
Дополнительно, если MBR на жестком диске это односекторный MBR созданный FDISK от Microsoft-а, он может быть просто скопирован во второй сектор файла GRLDR.MBR.  
  
Второй сектор GRLDR.MBR называется "previous MBR" (предыдущий MBR). Когда GRLDR не найден, то запускается загрузчик из "previous MBR".  
  
Больше никаких действий, кроме описанных выше, предпринимать не нужно, теперь просто запишите GRLDR.MBR в Master Boot Track (первая дорожка) жесткого диска. Всё.  
  
Заметка: Загрузочный код GRLDR.MBR всего лишь находит файл загрузчика GRLDR в корневой директории раздела. Файл menu.lst лучше всего положить рядом с загрузчиком (в той же директории и том же разделе) GRLDR.  
  
Имя файла "grldr" на ext2 разделах должнго быть в нижнем регистре, и тип файла должен быть указан как plain regular. Все остальные типы файлов, например символическая ссылка, не будут работать.  
  
Дополнение: bootlace.com это DOS/Linux утилита для установки содержимого файла grldr.mbr в MBR. Все данные из grldr.mbr содержаться в коде утилиты, поэтому её можно использовать отдельно.
:::
