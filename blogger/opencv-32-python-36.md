Title: Подготовка окружения для работы OpenCV 3.2 на Python 3.6
Date: 2017-06-18 04:46
Author: Краз
Slug: opencv-32-python-36
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
Доброго дня, коллеги.  
  
Потребовалось мне поднять веру в свои умственные способности путём реализации какое-либо проекта. Выбор пал на платформу компьютерного зрения OpenCV. Заодно решил счистить ржавчину со своих навыков работы с Python.  
  
1. Ставим Python.  
Дистрибутив берем с официального сайта https://www.python.org/downloads/windows/. Самая свежая версия на момент написания статьи 3.6.1. Установка в Windows не должна вызвать проблем.  
2. Ставим PIP  
Скрипт установки берём <https://bootstrap.pypa.io/get-pip.py>  
Запуск установки осуществляется командой:  

> python get-pip.py

3\. Ставим пакеты Python  

> pip install numpy  
> pip install matplotlib

4\. Ставим OpenCV  
Качаем wheel файл под нужную разрядность <http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv>.  
Устанавливаем через pip  

> pip install [[[opencv\_python‑3.2.0‑cp36‑cp36m‑win\_amd64.whl]{.underline}]{style="background-color: white; border-color: rgb(136, 136, 0); white-space: nowrap;"}]{style="color: #e00000;"}

5\. Проверяем работу  
import cv2  
  
  

:::
