Title: Активируем/деактивируем переадресацию вызовов станции со своего телефона (по занятости/неответу или безусловную)
Date: 2014-12-23 23:14
Author: Краз
Tags: Avaya, Телефоны
Slug: blog-post_23
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
  

::: {#rt-content-bottom-fake style="-webkit-text-stroke-width: 0px; background: rgb(235, 232, 213); border: 0px; color: #313439; font-family: Helvetica, Arial, sans-serif; font-size: 12px; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: 20.3999996185303px; margin: 0px; orphans: auto; outline: 0px; padding: 0px; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px;"}
::: {.rt-grid-fake style="background: transparent; border: 0px; display: table-cell; float: none; font-size: 12px; margin: 0px; outline: 0px; padding: 0px; position: relative; vertical-align: top; width: 1199px;"}
:::
:::

  

::: {.rt-block .component-block style="-webkit-text-stroke-width: 0px; background: rgb(255, 255, 255); border: 0px; color: #313439; font-family: Helvetica, Arial, sans-serif; font-size: 12px; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: 20.3999996185303px; margin: 0px 1px; orphans: auto; outline: 0px; padding: 0px; position: relative; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px;"}
::: {.component-content style="background: transparent; border: 0px; font-size: 12px; margin: 0px; outline: 0px; padding: 20px;"}
::: {.item-page style="background: transparent; border: 0px; font-size: 12px; margin: 0px; outline: 0px; padding: 0px;"}
::: {.separator style="clear: both; text-align: center;"}
[![](http://4.bp.blogspot.com/-qKWggY3tNFQ/VJpn1-W1QaI/AAAAAAAAK7Q/_M08x6iHTFo/s1600/IMG_20141224_101039.jpg){width="180" height="320"}](http://4.bp.blogspot.com/-qKWggY3tNFQ/VJpn1-W1QaI/AAAAAAAAK7Q/_M08x6iHTFo/s1600/IMG_20141224_101039.jpg)
:::

####  {#section style="background: transparent; border: 0px; font-size: 14px; line-height: 1.1em; margin: 15px 0px; outline: 0px; padding: 0px;"}

::: {style="background: transparent; border: 0px; font-size: 12px; margin: 0px 0px 15px; outline: 0px; padding: 0px;"}
Для пользования данной функцией (**Call Forwarding**) необходимо настроить feature-access-codes (**Call Forwarding Activation Busy/DA: All: Deactivation: **), если хотим использовать форвард по занятости/неответу, то разрешить это в COS-ах, которые используются на ТА.
:::

::: {style="background: transparent; border: 0px; font-size: 12px; margin: 0px 0px 15px; outline: 0px; padding: 0px;"}
**change feature-access-codes**
:::

::: {style="background: transparent; border: 0px; font-size: 12px; margin: 0px 0px 15px; outline: 0px; padding: 0px;"}
**Call Forwarding Activation Busy/DA: \*3     All: \*1     Deactivation: \#1**
:::

::: {style="background: transparent; border: 0px; font-size: 12px; margin: 0px 0px 15px; outline: 0px; padding: 0px;"}
[Процесс активации/деактивации функции **Call Forwarding** отличается для телефонов с правами Console Permissions, и телефонами, у которых этих прав нет.]{.message style="background: transparent; border: 0px; font-size: 12px; margin: 0px; outline: 0px; padding: 0px;"}
:::

::: {style="background: transparent; border: 0px; font-size: 12px; margin: 0px 0px 15px; outline: 0px; padding: 0px;"}
Рассмотрим несколько поясняющих примеров:
:::

#### Пример перевода всех вызовов (Call Forwarding All) с номера 1234  (с правами Console Premissions) на номер 5678 {#пример-перевода-всех-вызовов-call-forwarding-all-с-номера-1234-с-правами-console-premissions-на-номер-5678 style="background: transparent; border: 0px; font-size: 14px; line-height: 1.1em; margin: 15px 0px; outline: 0px; padding: 0px;"}

1.  набираем FAC для СF ALL - \*1
2.  ждем dialtone
3.  набираем номер телефона, с которого будет переадресация - 1234
4.  ждем dialtone
5.  набираем номер телефона, на который будем переводить звонки - 5678
6.  ждем подтверждающий тон
7.  делаем тестовый вызов

::: {style="background: transparent; border: 0px; font-size: 12px; margin: 0px 0px 15px; outline: 0px; padding: 0px;"}
  
:::

#### Пример перевода всех вызовов (Call Forwarding All) с номера 2345  (без прав Console Premissions) на номер 6789 {#пример-перевода-всех-вызовов-call-forwarding-all-с-номера-2345-без-прав-console-premissions-на-номер-6789 style="background: transparent; border: 0px; font-size: 14px; line-height: 1.1em; margin: 15px 0px; outline: 0px; padding: 0px;"}

1.  набираем FAC для СF ALL - \*1
2.  ждем dialtone
3.  набираем номер телефона, на который будем переводить звонки - 6789
4.  ждем подтверждающий тон
5.  делаем тестовый вызов

::: {style="background: transparent; border: 0px; font-size: 12px; margin: 0px 0px 15px; outline: 0px; padding: 0px;"}
  
:::

#### Пример снятия переадресации всех вызовов (Call Forwarding All) с номера без прав Console Premissions {#пример-снятия-переадресации-всех-вызовов-call-forwarding-all-с-номера-без-прав-console-premissions style="background: transparent; border: 0px; font-size: 14px; line-height: 1.1em; margin: 15px 0px; outline: 0px; padding: 0px;"}

1.  набираем FAC для СF Deactivation - \#1
2.  ждем подтверждающий тон
3.  делаем тестовый вызов

::: {style="background: transparent; border: 0px; font-size: 12px; margin: 0px 0px 15px; outline: 0px; padding: 0px;"}
  
:::

#### Пример снятия переадресации всех вызовов (Call Forwarding All) с номера c правами Console Premissions {#пример-снятия-переадресации-всех-вызовов-call-forwarding-all-с-номера-c-правами-console-premissions style="background: transparent; border: 0px; font-size: 14px; line-height: 1.1em; margin: 15px 0px; outline: 0px; padding: 0px;"}

1.  набираем FAC для СF Deactivation - \#1
2.  ждем dialtone
3.  набираем номер телефона, на котором стоит переадресация
4.  ждем подтверждающий тон
5.  делаем тестовый вызов
:::

::: {.clear style="background: none; border: 0px; clear: both; display: block; float: none; font-size: 0px; height: 0px; list-style: none; margin: 0px; outline: 0px; overflow: hidden; padding: 0px; visibility: hidden; width: 0px;"}
:::
:::

::: {.clear style="background: none; border: 0px; clear: both; display: block; float: none; font-size: 0px; height: 0px; list-style: none; margin: 0px; outline: 0px; overflow: hidden; padding: 0px; visibility: hidden; width: 0px;"}
:::
:::
:::
