Title: Карманный справочник по администрированию Avaya
Date: 2014-11-27 21:13
Author: Краз
Tags: Avaya, Телефоны, Документация
Slug: avaya
Status: published

::: {dir="ltr" style="text-align: left;" trbidi="on"}
::: {style="color: #333333; font-family: Arial, Helvetica, sans-serif; font-size: 12px; line-height: 18px; margin-bottom: 1em; margin-top: 1em; padding: 0px;"}
[Регулярно приходится возвращаться к настройке станции Avaya S8400 и в поисках давно забытых опций часто перелопачивать интернет где множество таких эпизодических админов задают каждый раз одни и те же вопросы. Когда нашёл это справочник очень обрадовался тому что большинство часто задаваемых вопросов здесь упоминаются. И хотя решения не дают полного понимания, зато позволяют сформировать точку отчёта для дальнейших поисков.  Делюсь имеющимся справочником и буду по мере сил и возможностей дополнять своими граблями.]{style="background-color: white;"}  
[]{style="background-color: white;"}  
[]{#more}  
:::

[№]{style="background-color: white;"}
:::

[Функция]{style="background-color: white;"}

[Что надо смотреть]{style="background-color: white;"}

[Особенности]{style="background-color: white;"}

[Пример]{style="background-color: white;"}

[1]{style="background-color: white;"}

[Сокращенный набор номера ( Abbreviated  Dialing Enhanced List)]{style="background-color: white;"}

[display system-parameters customer-options]{style="background-color: white;"}

[Должно быть активизировано поле Abbreviated Dialing Enhanced  List]{style="background-color: white;"}

[add abbreviated-dialing group next                                                           add abbreviated-dialing sys]{style="background-color: white;"}

[В поле Group  Name введите имя для этого списка. В поле Size введите число, кратное 5. Это число определяет количество записей в списке набора номеров. В поле Program  Ext введите внутренний номер. Каждый телефонный номер может иметь длину до 24 цифр.]{style="background-color: white;"}

[change station n]{style="background-color: white;"}

[Введите group или system в любом из трех полей List                                  Назначение кнопки быстрого набора abrv-dial]{style="background-color: white;"}

[change feature-access-codes]{style="background-color: white;"}

[Назначение кодов  активации функции                                                           Для использовании функции необходимо набрать активацию функции и диал код( присвоенный данному номеру)]{style="background-color: white;"}

[\#0701]{style="background-color: white;"}

[2]{style="background-color: white;"}

[Как узнать сведения о конфигурации АТС]{style="background-color: white;"}

[display system-parameters customer-options                                                      display capacity             list configuration all]{style="background-color: white;"}

[Первая закладка ПО- G3 Version]{style="background-color: white;"}

[3]{style="background-color: white;"}

[Изменение времени ( летнее и зимнее)]{style="background-color: white;"}

[change locations ( должны быть прописаны rule )    change daylight-savings-rules ( прописывается переход на иное время)   set time]{style="background-color: white;"}

[На S8400 и.т.д не актуально]{style="background-color: white;"}

[4]{style="background-color: white;"}

[Проверка где задействован  номер]{style="background-color: white;"}

[list usage extension 0000]{style="background-color: white;"}

[5]{style="background-color: white;"}

[Синхронизация станций]{style="background-color: white;"}

[status health]{style="background-color: white;"}

[( состояние должно быть UP ) Если они рассинхронизированны то следует набрать команду change system-parameters ess]{style="background-color: white;"}

[сейчас не актуально]{style="background-color: white;"}

[change system-parameters ess]{style="background-color: white;"}

[Где на последней закладке назначить руками время начала синхронизации.]{style="background-color: white;"}

[сейчас не актуально]{style="background-color: white;"}

[status ess port-networks]{style="background-color: white;"}

[get forced-takeover ipserver-interface port-network 2]{style="background-color: white;"}

[В случае рассинхронизации необхлодимо дать эту команду что бы основной сервер взял управление выживающим. Если не сделать то будут работать независимо друг от друга.]{style="background-color: white;"}

[status ess clusters]{style="background-color: white;"}

[https://ip1https://ip2](https://ip1https//ip2)

[В случаи если не удается синхронизировать станции надо проверить видят ли они друг друга. Заходим на сервер по веб-интерфейсу, вводи логин и пароль, выбираем меню Launch Maintenance Web Interface , в нем Diagnostics  — Ping . Запустив пинги  All IPSIs, UPS(s)  можно увидеть видят ли друг друга станции.]{style="background-color: white;"}

[6]{style="background-color: white;"}

[Настройка вектора для многоканального телефона]{style="background-color: white;"}

[add vdn next]{style="background-color: white;"}

[01 wait-time 0 secs hearing silence 02 collect 4 digits after announcement  (номер сообщения) 03 route-to digits with coverage n 04 stop]{style="background-color: white;"}

[8]{style="background-color: white;"}

[Изменение ip-адреса (для лоступа к станции)]{style="background-color: white;"}

[ch. Node-name ip                                                                        change ip-services]{style="background-color: white;"}

[9]{style="background-color: white;"}

[Заведение новых абонентов]{style="background-color: white;"}

[add st XXXX]{style="background-color: white;"}

[Обязательно указываются поля: type — ставим или номер модели или поддерживаемый тип port — адрес порта name — латинскими буквами]{style="background-color: white;"}

[10]{style="background-color: white;"}

[Приорететный звонок]{style="background-color: white;"}

[change feature-access-codes]{style="background-color: white;"}

[Определение FAC для функции  change feature-access-codes — 3я страница Priority Calling Access Code.Назначение функциональной кнопки для функции  «Приоритетный вызов» для внутреннего номера  телефонного аппарата- priority.]{style="background-color: white;"}

[\#464545]{style="background-color: white;"}

[11]{style="background-color: white;"}

[Переадресация городского номера на другую станцию]{style="background-color: white;"}

[add station next ; add coverage path next ;  change coverage remote]{style="background-color: white;"}

[12]{style="background-color: white;"}

[состояние транка  в станции]{style="background-color: white;"}

[status trunk X]{style="background-color: white;"}

[Где X- номер интересующего транка.]{style="background-color: white;"}

[13]{style="background-color: white;"}

[просмотр существующих абонентов в станции]{style="background-color: white;"}

[List station]{style="background-color: white;"}

[Выводится список всех заведенных в станцию номеров.]{style="background-color: white;"}

[14]{style="background-color: white;"}

[Параметры звукового файла]{style="background-color: white;"}

[.wav (8KHz, 8bit mono, PCM)]{style="background-color: white;"}

[можно править с помощью программы «Звукозапись» 9 ( в win она имеется в стандартных)]{style="background-color: white;"}

[15]{style="background-color: white;"}

[Изменение параметров абонента]{style="background-color: white;"}

[Change station XXXX]{style="background-color: white;"}

[Позволяет производить изменения и настройку абонентов]{style="background-color: white;"}

[17]{style="background-color: white;"}

[Показывает активные перадресации ( включенные с телефона \#02)]{style="background-color: white;"}

[list call-forwarding]{style="background-color: white;"}

[показывает переадресации включенные руками с телефона(\#02)]{style="background-color: white;"}

[18]{style="background-color: white;"}

[Принудительный первод звонков ( «не беспокоить» )]{style="background-color: white;"}

[dn-dst (на свободную  кнопку)]{style="background-color: white;"}

[Пописываем coverage path, в нем везде ставим No,  кроме DND\\SAC\\Goto cover. В пункте Point указываем номер на который переходит звонок. На апарате прописываем coverage , и назначаем кнопку dn-dst/Принажатии  кнопки загорается зеленый индикатор,  активируется переадресация  и  все звонки переходят на  другого абонента.]{style="background-color: white;"}

[19]{style="background-color: white;"}

[Перехват вызова]{style="background-color: white;"}

[add pickup-group n    кнопка call-pkup]{style="background-color: white;"}

[Абоненты внутри комнаты могут отвечать на звонки соседа со своего аппарата. Для начала создается группа абонентов add pickup-group n, в нее заносятся номера абонентов входящих в группу. Далее всем абонентам назначается кнопка call-pkup, нажимая на котрую они могут перехватывать звонки.]{style="background-color: white;"}

[21]{style="background-color: white;"}

[Настройка таблицы маршрутизации для связи с РГЦ]{style="background-color: white;"}

[change uniform-dialplan  0]{style="background-color: white;"}

[22]{style="background-color: white;"}

[Пеленг баз для Дект]{style="background-color: white;"}

[На трубке набрать \*99989\*V                                                                   На трубке набрать \*99981\*V]{style="background-color: white;"}

[23]{style="background-color: white;"}

[Запараллевание телефона и мобильного]{style="background-color: white;"}

[change off-pbx-telephone station-mapping                                   change xmobile configuration-set]{style="background-color: white;"}

[на телефоне кнопка EC500]{style="background-color: white;"}

[24]{style="background-color: white;"}

[Насколько загружены кодеки]{style="background-color: white;"}

[list measurements ip dsp-resource summary today-peak]{style="background-color: white;"}

[25]{style="background-color: white;"}

[Настройка исходящего АОНа]{style="background-color: white;"}

[change public-unknown-numbering                                                change private-numbering 0           change route-pattern]{style="background-color: white;"}

[26]{style="background-color: white;"}

[Настройка исходящих наружу звонков]{style="background-color: white;"}

[change ars analysis 1     change route-pattern X                                                                change partition-route-table 1]{style="background-color: white;"}

[27]{style="background-color: white;"}

[Запись сообщения]{style="background-color: white;"}

[У телефона в COS должен стоять console permision: y  (cos 15)]{style="background-color: white;"}

[\*11 XXXX(номер анонсмента)  1 — записать  2- прослушать              3 — удалить]{style="background-color: white;"}

[28]{style="background-color: white;"}

[Перезагрузка станции с консоли]{style="background-color: white;"}

[reset system  4]{style="background-color: white;"}

[30]{style="background-color: white;"}

[Настройка «Барсум» на станции]{style="background-color: white;"}

[change node-names ip                change ip-services              change system-parameters cdr]{style="background-color: white;"}

[31]{style="background-color: white;"}

[Загруженность транков]{style="background-color: white;"}

[list measurements trunk-group summary yesterday-peak]{style="background-color: white;"}

[последнее значение выбирается по необходимости]{style="background-color: white;"}

[32]{style="background-color: white;"}

[Отчеты по конфигурации станции ( все сразу)]{style="background-color: white;"}

[i con a; li cab; disp cab 1; disp ci; disp cap;  disp sys cu; disp sys sp; disp sys of]{style="background-color: white;"}

[Для  быстрого получения отчётов в Avaya Site Administrator нажмите Ctrl-R, вставьте в появившемся окне в поле Commands строку ниже: li con a; li cab; disp cab 1; disp ci; disp cap;  disp sys cu; disp sys sp; disp sys of (пример команд) Затем выберите Export screen capture to file и укажите путь к файлу. Нажмите OK. Все отчёты окажутся в одном файле]{style="background-color: white;"}

[36]{style="background-color: white;"}

[Настройка «Барсум» на станции для тарификации внутренних звонков]{style="background-color: white;"}

[change intra-switch-cdr     change system-parameters cdr]{style="background-color: white;"}

[параметр Intra-switch CDR -  y]{style="background-color: white;"}

[39]{style="background-color: white;"}

[При попытке перезвонить из call loga подставляет 9]{style="background-color: white;"}

[В файле 46xxseting.txt впараметре ENHANCED LOCAL DIALING RULES  в пункте Internal extension number length правим строчку SET PHNDPLENGTH X]{style="background-color: white;"}

[где X- длинна внутренненго номера принятого в станции]{style="background-color: white;"}

[40]{style="background-color: white;"}

[Ограничение длительности разговора]{style="background-color: white;"}

[После ввода команды change system-parameters features на 5-й странице параметр Use Trunk COR for Outgoing Trunk Disconnect. У этого параметра может быть два значения:n — Default. Время ограничения звонка определяется COR абонента y — Время ограничения звонка определяется COR исходящего транка.Далее в форме COR на второй странице выставить ограничение длительности: Outgoing Trunk Disconnect Timer (minutes) от 2 до 999 минут. За 1 минуту до окончания таймера пойдет гудок предупреждения, за 30 секунд второй, еще через 30 секунд – разъединение]{style="background-color: white;"}

[41]{style="background-color: white;"}

[Настройка звонков в РГЦ]{style="background-color: white;"}

[list uniform-dialplan]{style="background-color: white;"}

[42]{style="background-color: white;"}

[Показать последние команды]{style="background-color: white;"}

[list history]{style="background-color: white;"}

[43]{style="background-color: white;"}

[Показать незарегестрированные телефоны]{style="background-color: white;"}

[display errors]{style="background-color: white;"}

[где Error Type — 1  Category — station]{style="background-color: white;"}

[46]{style="background-color: white;"}

[Для редактирования таблицы АОН]{style="background-color: white;"}

[change public-unknown-numbering 4 ext-digits n]{style="background-color: white;"}

[Где N- номер телефона]{style="background-color: white;"}

[47]{style="background-color: white;"}

[Подвисание Барсума]{style="background-color: white;"}

[status cdr-link; busyout cdr-link primary; release cdr-link primary]{style="background-color: white;"}

[В случае корректной работы барсума CDR buffer должен быть пустым]{style="background-color: white;"}

[  
]{style="background-color: white;"}[  
]{style="background-color: white;"}[Источник](http://systemadmins.ru/avaya/287-spravochnik-po-administrirovaniyu-avaya.html)
