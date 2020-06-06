Title: Отключить Защитник Windows
Date: 2017-10-21 12:38
Author: Краз
Tags: PowerShell, Windows
Slug: windows
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
::: {.tr_bq}
[![](https://4.bp.blogspot.com/-2GC84hKYr1o/WeuiAsiUipI/AAAAAAAAOKM/0XXHC3zPl74Atl3IA_4IJvQtrUd0dJnVwCK4BGAYYCw/s640/windows-defender-768x432.jpg){width="640" height="360"}](http://4.bp.blogspot.com/-2GC84hKYr1o/WeuiAsiUipI/AAAAAAAAOKM/0XXHC3zPl74Atl3IA_4IJvQtrUd0dJnVwCK4BGAYYCw/s1600/windows-defender-768x432.jpg)Еще одна напрягающая мой старый ноутбук служба Windows - это её защитник.
:::

Опять призываем на помощь себе запущенную рот имени системного администратора консоль PowerShell.  
  
Отключаем все запланированные задания  
  

::: {style="color: black; font-family: "segoe ui"; font-size: 12; font-style: normal; font-weight: normal; text-align: left;"}
::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[ ]{style="font-size: 16;"}[Get-ScheduledTask]{style="color: blue;"} [\*defender\*]{style="color: blueviolet;"} [\|]{style="color: darkgrey;"} [Disable-ScheduledTask]{style="color: blue;"}  
:::
:::

  
И добавляем в реестр параметр  
  

::: {style="color: black; font-family: "segoe ui"; font-size: 12; font-style: normal; font-weight: normal; text-align: left;"}
::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[ ]{style="font-size: 16;"} [New-ItemProperty]{style="color: blue;"} [-path]{style="color: navy;"} ["HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender"]{style="color: darkred;"} [-Name]{style="color: navy;"} ["DisableAntiSpyware"]{style="color: darkred;"} [-Value]{style="color: navy;"} ["1"]{style="color: darkred;"} [-PropertyType]{style="color: navy;"} ["Dword"]{style="color: darkred;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[New-ItemProperty]{style="color: blue;"} [-path]{style="color: navy;"} ["HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender"]{style="color: darkred;"} [-Name]{style="color: navy;"} ["AllowFastServiceStartup"]{style="color: darkred;"} [-Value]{style="color: navy;"} ["0"]{style="color: darkred;"} [-PropertyType]{style="color: navy;"} ["Dword"]{style="color: darkred;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[New-ItemProperty]{style="color: blue;"} [-path]{style="color: navy;"} ["HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender"]{style="color: darkred;"} [-Name]{style="color: navy;"} ["ServiceKeepAlive"]{style="color: darkred;"} [-Value]{style="color: navy;"} ["0"]{style="color: darkred;"} [-PropertyType]{style="color: navy;"} ["Dword" ]{style="color: darkred;"}
:::
:::

  
Перезагрузка. И ничего... оказывается Windows 10 Creator Update несколько по другому работает. Добавляем:  
  

::: {style="color: black; font-family: "segoe ui"; font-size: 12; font-style: normal; font-weight: normal; text-align: left;"}
::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[ ]{style="font-size: 16;"}[MkDir]{style="color: blue;"} [-path]{style="color: navy;"} ["HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender"]{style="color: darkred;"} [-Name]{style="color: navy;"} ["Real-Time Protection"]{style="color: darkred;"}
:::

  

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[New-ItemProperty]{style="color: blue;"} [-Path]{style="color: navy;"} ["HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection"]{style="color: darkred;"} [-Name]{style="color: navy;"} ["DisableBehaviorMonitoring"]{style="color: darkred;"} [-Value]{style="color: navy;"} ["1"]{style="color: darkred;"} [-PropertyType]{style="color: navy;"} ["Dword"]{style="color: darkred;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[New-ItemProperty]{style="color: blue;"} [-Path]{style="color: navy;"} ["HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection"]{style="color: darkred;"} [-Name]{style="color: navy;"} ["DisableOAVProtection"]{style="color: darkred;"} [-Value]{style="color: navy;"} ["1"]{style="color: darkred;"} [-PropertyType]{style="color: navy;"} ["Dword"]{style="color: darkred;"}
:::

  

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[MkDir]{style="color: blue;"} [-path]{style="color: navy;"} ["HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender"]{style="color: darkred;"} [-Name]{style="color: navy;"} ["Spynet"]{style="color: darkred;"}
:::

  

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[New-ItemProperty]{style="color: blue;"} [-Path]{style="color: navy;"} ["HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Spynet"]{style="color: darkred;"} [-Name]{style="color: navy;"} ["DisableBlockAtFirstSeen"]{style="color: darkred;"} [-Value]{style="color: navy;"} ["1"]{style="color: darkred;"} [-PropertyType]{style="color: navy;"} ["Dword"]{style="color: darkred;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[New-ItemProperty]{style="color: blue;"} [-Path]{style="color: navy;"} ["HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Spynet"]{style="color: darkred;"} [-Name]{style="color: navy;"} ["LocalSettingOverrideSpynetReporting"]{style="color: darkred;"} [-Value]{style="color: navy;"} ["0"]{style="color: darkred;"} [-PropertyType]{style="color: navy;"} ["Dword"]{style="color: darkred;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[New-ItemProperty]{style="color: blue;"} [-Path]{style="color: navy;"} ["HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Spynet"]{style="color: darkred;"} [-Name]{style="color: navy;"} ["SubmitSamplesConsent"]{style="color: darkred;"} [-Value]{style="color: navy;"} ["2"]{style="color: darkred;"} [-PropertyType]{style="color: navy;"} ["Dword" ]{style="color: darkred;"}
:::

  
  
:::

  
Вот теперь отключились сервисы высвободив немного оперативной памяти и перестав нервировать меня проверкой по включению машины.
:::
