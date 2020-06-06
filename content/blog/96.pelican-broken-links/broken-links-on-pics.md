Title: "Сломанные" ссылки изображений на страницах статей в Pelican
Category: Блог
Tags: pelican
Summary: Как починить  битые ссылки на изображения на страницах отличных от индекса
Image: cover.png
---
![Cover]({attach}cover.png){width="320" height="195"}
# Проблема

Есть Markdown-страница в каталоге content/mypage.md, на основе которой был сгенерирован файл `localhost:8000/mypage.html`, и в нем есть рабочая ссылка на изображение:
`![Alt text](content/myimage.png)`
которая в сгенерированном файле выглядит как:
`<img src="content/myimage.png" />`
и ссылается на адрес `localhost:8000/content/myimage.png`. Однако, если открыть тот же самый файл HTML со страницы с категориями, то так же ссылка на картинку
`![Alt text](content/myimage.png)`
с тем же самым HTML кодом
`<img src="content/myimage.png" />`
но со страницы со списком статей по категории `localhost:8000/categories/mycategory.html`, этот относительный URL-адрес картинкитеперь ссылается на `localhost:8000/categories/content/myimage.png` и изображение не отображется со страниц категорий или тэгов, поскольку ссылка битая.
В итоге получается что проблема заключается в том, что используются относительные URL-адреса изображений.
# Решение
Решение очень простое: использвоать еще один `/`. Используйте абсолютные ссылки на изображения в Markdown файлах добавляя в начало ведущий `/`.  Вместо использования ссылок вида `content/myimage.png`, пользуйтесь `/content/myimage.png`:
`![Alt text](/content/myimage.png)`
И такая ссылка на изображение всегда будет генерировать ссылку  `localhost:8000/content/myimage.png`, вне зависимости от того на какой странице это будет.

Я так чинил ссылки на аватарку. На Индексной странице она отображалась нормально, но на странице категорий, тэгов или даже самих статей ссылка билась. Для исправления в файле настроек `pelicanconf.py` я указал следующие настройки с абсолютными ссылками:
`SITELOGO = '/images/avatar1.jpg'
FAVICON = '/images/favicon.ico'`
И это полностью решило проблему.

[Источник](https://stackoverflow.com/questions/30794909/pelican-image-links-break-when-viewing-article-through-categories)
