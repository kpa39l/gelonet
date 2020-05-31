Title: Формирование HTML из Powershell кода в ISE
Date: 2017-11-04 08:03
Author: Краз
Tags: PowerShell
Slug: html-powershell-ise
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
::: {.separator style="clear: both; text-align: center;"}
[![](https://1.bp.blogspot.com/-BILJpDACao8/Wf3RPO55_iI/AAAAAAAAOMo/sG5pqylWy58TGL6tYSPZ_Lnu26GEnq9bgCLcBGAs/s640/powershell.jpg){width="640" height="640"}](https://1.bp.blogspot.com/-BILJpDACao8/Wf3RPO55_iI/AAAAAAAAOMo/sG5pqylWy58TGL6tYSPZ_Lnu26GEnq9bgCLcBGAs/s1600/powershell.jpg)
:::

::: {style="text-align: justify;"}
  
:::

::: {style="text-align: justify;"}
Увидел как убого выглядит вставляемый код и поискал способ для формирования расцвеченного HTML кода для вставки в статьи блога. Поскольку я использую Powershell совсем не часто, то функционала стандартного ISE мне выше крыши. Так что первым делом попытался найти способ сделать это из этого инструмента.
:::

  
Нашёл хорошую статью на wiki technet [Wiki: Как вставить отформатированный код сценария PowerShell в TechNet Wiki.](https://social.technet.microsoft.com/wiki/ru-ru/contents/articles/20783.wiki-powershell-technet-wiki.aspx) Но увы PowerShellPack уже вышел в тираж.  
  
Зато на той же wiki нашёл [страницу с дополнениями](https://social.technet.microsoft.com/wiki/contents/articles/2969.windows-powershell-ise-add-on-tools.aspx) для самого ISE. Одним из которых был [Copy As HTML Add-On](http://blog.falchionconsulting.com/index.php/tag/ise/). Удобная штука с собственным установщиком. Пришлось правда использовать set-executionpolicy, но это и так пришлось бы делать. [Схоронил](https://yadi.sk/d/6WQZyMbw3PQfkg) у себя этот архивчик.  
  
В статью Блогера код вставляется в режиме HTML. И выглядит один-в-один как в редакторе:  
  

::: {style="color: black; font-family: "segoe ui"; font-size: 12; font-style: normal; font-weight: normal; text-align: left;"}
::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[ ]{style="font-size: 16;"}[\$path]{style="color: orangered;"} [=]{style="color: darkgrey;"} ["d:\\temp\\"]{style="color: darkred;"}
:::

  

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\$files]{style="color: orangered;"} [=]{style="color: darkgrey;"} [Get-ChildItem]{style="color: blue;"} [\$path]{style="color: orangered;"}
:::

  

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\$excel]{style="color: orangered;"} [=]{style="color: darkgrey;"} [New-Object]{style="color: blue;"} [-ComObject]{style="color: navy;"} [Excel.Application]{style="color: blueviolet;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\$excel]{style="color: orangered;"}[.]{style="color: darkgrey;"}Visible [=]{style="color: darkgrey;"} [\$false]{style="color: orangered;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\$excel]{style="color: orangered;"}[.]{style="color: darkgrey;"}DisplayAlerts [=]{style="color: darkgrey;"} [\$false]{style="color: orangered;"}
:::

  

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\$Summary]{style="color: orangered;"} [=]{style="color: darkgrey;"} @()
:::

  

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[foreach]{style="color: darkblue;"} ([\$file]{style="color: orangered;"} [in]{style="color: darkblue;"} [\$files]{style="color: orangered;"}) {
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
     [\#Открываем каждый из полученных файлов]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    [\$excel]{style="color: orangered;"}[.]{style="color: darkgrey;"}Workbooks[.]{style="color: darkgrey;"}Open([\$file]{style="color: orangered;"}[.]{style="color: darkgrey;"}fullname) [\|]{style="color: darkgrey;"} [Out-Null]{style="color: blue;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    [\[]{style="color: darkgrey;"}[int]{style="color: teal;"}[\]]{style="color: darkgrey;"} [\$Year]{style="color: orangered;"} [=]{style="color: darkgrey;"} ["20"]{style="color: darkred;"} [+]{style="color: darkgrey;"}[\$File]{style="color: orangered;"}[.]{style="color: darkgrey;"}name[.]{style="color: darkgrey;"}substring([\$file]{style="color: orangered;"}[.]{style="color: darkgrey;"}name[.]{style="color: darkgrey;"}Length [-]{style="color: darkgrey;"} [6]{style="color: purple;"}[,]{style="color: darkgrey;"}[2]{style="color: purple;"});
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    [\[]{style="color: darkgrey;"}[int]{style="color: teal;"}[\]]{style="color: darkgrey;"} [\$Month]{style="color: orangered;"} [=]{style="color: darkgrey;"} [\$file]{style="color: orangered;"}[.]{style="color: darkgrey;"}name[.]{style="color: darkgrey;"}substring([\$file]{style="color: orangered;"}[.]{style="color: darkgrey;"}name[.]{style="color: darkgrey;"}Length [-]{style="color: darkgrey;"} [9]{style="color: purple;"}[,]{style="color: darkgrey;"}[2]{style="color: purple;"});
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    [Write-Host]{style="color: blue;"} ["Open file: "]{style="color: darkred;"} [\$file]{style="color: orangered;"}[.]{style="color: darkgrey;"}FullName ["; Year = "]{style="color: darkred;"} [\$Year]{style="color: orangered;"} ["; Month = "]{style="color: darkred;"} [\$month]{style="color: orangered;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    [\#Получаем перечень с именами листов длиной менее трёх символов - листы с данными по дням имеют имена в два символа]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    [\$Sheets]{style="color: orangered;"} [=]{style="color: darkgrey;"} [\$excel]{style="color: orangered;"}[.]{style="color: darkgrey;"}worksheets [\|]{style="color: darkgrey;"} [where]{style="color: blue;"} {[\$\_]{style="color: orangered;"}[.]{style="color: darkgrey;"}Name[.]{style="color: darkgrey;"}length [-lt]{style="color: darkgrey;"} [3]{style="color: purple;"}}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    [\$plan]{style="color: orangered;"} [=]{style="color: darkgrey;"} [0]{style="color: purple;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    [\$fact]{style="color: orangered;"} [=]{style="color: darkgrey;"} [0]{style="color: purple;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    [\#Для каждого из полученных листов в файле проводим разбор]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    [foreach]{style="color: darkblue;"} ([\$Sheet]{style="color: orangered;"} [in]{style="color: darkblue;"} [\$Sheets]{style="color: orangered;"})  {
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
        [\[]{style="color: darkgrey;"}[int]{style="color: teal;"}[\]]{style="color: darkgrey;"} [\$Day]{style="color: orangered;"} [=]{style="color: darkgrey;"} [\$Sheet]{style="color: orangered;"}[.]{style="color: darkgrey;"}Name
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
        
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
        [for]{style="color: darkblue;"} ([\$Col]{style="color: orangered;"} [=]{style="color: darkgrey;"} [7]{style="color: purple;"}; [\$Col]{style="color: orangered;"} [-le]{style="color: darkgrey;"} [8]{style="color: purple;"}; [\$Col]{style="color: orangered;"}[++]{style="color: darkgrey;"}) {
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
            [For]{style="color: darkblue;"} ([\$Row]{style="color: orangered;"} [=]{style="color: darkgrey;"}[14]{style="color: purple;"}; [\$Row]{style="color: orangered;"} [-le]{style="color: darkgrey;"} [16]{style="color: purple;"}; [\$Row]{style="color: orangered;"}[++]{style="color: darkgrey;"}) {
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                [if]{style="color: darkblue;"} ([\$sheet]{style="color: orangered;"}[.]{style="color: darkgrey;"}cells[.]{style="color: darkgrey;"}item([\$Row]{style="color: orangered;"}[,]{style="color: darkgrey;"} [\$Col]{style="color: orangered;"})[.]{style="color: darkgrey;"}Value2 [-eq]{style="color: darkgrey;"} ["Койко/мест"]{style="color: darkred;"}) {
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\#Write-host \$year \$Month \$Day "-" \$Col ":" \$Row  = "YES!"]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\#Write-Host "Day = " \$Day "; Fact Value = " \$sheet.cells.item(\$Row, \$Col + 2).Value2 "; PlanValue = " \$sheet.cells.item(\$Row + 1, \$Col + 2).Value2]{style="color: darkgreen;"}
:::

  

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\#\$DataDay = New-Object PsObject]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\#\$DataDay \| Add-Member -MemberType noteproperty -Name Year -Value \$Year]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\#\$DataDay \| Add-Member -MemberType noteproperty -Name Month -Value \$Month]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\#\$DataDay \| Add-Member -MemberType noteproperty -Name Day -Value \$Day]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\#\$DataDay \| Add-Member -MemberType noteproperty -Name FactValue -Value \$sheet.cells.item(\$Row, \$Col + 2).Value2]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\#\$DataDay \| Add-Member -MemberType noteproperty -Name PlanValue -Value \$sheet.cells.item(\$Row + 1, \$Col + 2).Value2]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\#\$Summary += \$DataDay]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\$plan]{style="color: orangered;"} [+=]{style="color: darkgrey;"}[\$sheet]{style="color: orangered;"}[.]{style="color: darkgrey;"}cells[.]{style="color: darkgrey;"}item([\$Row]{style="color: orangered;"} [+]{style="color: darkgrey;"} [1]{style="color: purple;"}[,]{style="color: darkgrey;"} [\$Col]{style="color: orangered;"} [+]{style="color: darkgrey;"} [2]{style="color: purple;"})[.]{style="color: darkgrey;"}Value2
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\$fact]{style="color: orangered;"} [+=]{style="color: darkgrey;"}[\$sheet]{style="color: orangered;"}[.]{style="color: darkgrey;"}cells[.]{style="color: darkgrey;"}item([\$Row]{style="color: orangered;"}[,]{style="color: darkgrey;"} [\$Col]{style="color: orangered;"} [+]{style="color: darkgrey;"} [2]{style="color: purple;"})[.]{style="color: darkgrey;"}Value2
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                }
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
            }
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
        }
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
    }
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                [\$DateMonth]{style="color: orangered;"} [=]{style="color: darkgrey;"} [New-Object]{style="color: blue;"} [PsObject]{style="color: blueviolet;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\$DateMonth]{style="color: orangered;"} [\|]{style="color: darkgrey;"} [Add-Member]{style="color: blue;"} [-MemberType]{style="color: navy;"} [noteproperty]{style="color: blueviolet;"} [-Name]{style="color: navy;"} [Year]{style="color: blueviolet;"} [-Value]{style="color: navy;"} [\$Year]{style="color: orangered;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\$DateMonth]{style="color: orangered;"} [\|]{style="color: darkgrey;"} [Add-Member]{style="color: blue;"} [-MemberType]{style="color: navy;"} [noteproperty]{style="color: blueviolet;"} [-Name]{style="color: navy;"} [Month]{style="color: blueviolet;"} [-Value]{style="color: navy;"} [\$Month]{style="color: orangered;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\$DateMonth]{style="color: orangered;"} [\|]{style="color: darkgrey;"} [Add-Member]{style="color: blue;"} [-MemberType]{style="color: navy;"} [noteproperty]{style="color: blueviolet;"} [-Name]{style="color: navy;"} [FactValue]{style="color: blueviolet;"} [-Value]{style="color: navy;"} [\$Fact]{style="color: orangered;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
                    [\$DateMOnth]{style="color: orangered;"} [\|]{style="color: darkgrey;"} [Add-Member]{style="color: blue;"} [-MemberType]{style="color: navy;"} [noteproperty]{style="color: blueviolet;"} [-Name]{style="color: navy;"} [PlanValue]{style="color: blueviolet;"} [-Value]{style="color: navy;"} [\$Plan]{style="color: orangered;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
            [\$Summary]{style="color: orangered;"} [+=]{style="color: darkgrey;"} [\$DateMonth]{style="color: orangered;"}
:::

  

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\$Summary]{style="color: orangered;"} [\|]{style="color: darkgrey;"} [Out-GridView]{style="color: blue;"}
:::

  

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#\$table = @()]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#   for (\$i=2010; \$i -le 2011; \$i++) {]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#        For (\$j = 1; \$j -le 12; \$j++) {]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#            \$temp = \$summary \| where {\$\_.Month = \$j} \| where {\$\_.Year = \$i}]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#            \$Fact = 0]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#            \$Plan = 0]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#            foreach (\$t in \$temp) {]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#                \$fact += \$t.FactValue]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#                \$plan += \$t.PlanValue]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#            }]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#            ]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#            \$DateMonth = New-Object PsObject]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#                    \$DataMonth \| Add-Member -MemberType noteproperty -Name Year -Value \$Year]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#                    \$DataMonth \| Add-Member -MemberType noteproperty -Name Month -Value \$Month]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#                    \$DataMonth \| Add-Member -MemberType noteproperty -Name FactValue -Value \$Fact]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#                    \$DataMOnth \| Add-Member -MemberType noteproperty -Name PlanValue -Value \$Plan]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#            \$table += \$dateMonth]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#        }]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#    ]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
[\#    }]{style="color: darkgreen;"}
:::

::: {style="background-color: white; font-family: "lucida console"; margin: 0 0 0 0;"}
:::

  
  
  
  
  
  
:::
:::
