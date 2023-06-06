# bio_labels
Данное приложение облегчает работу этмологам для создания этикеток различных насекомых. 
## Механизм создания этикетки
Так как этикеток может быть много, в приложение реализован механизм вкладок. Каждая вкладка - это отдельная этикетка, которую можно изменять.
Механизм создания этикетки: пользователь нажимает кнопку "изменить" и попадает в активное диалоговое окно с настройками этикетки. Эти настройки сохраняются даже после закрытия окна изменений. После нажатия на кнопку "применить" создается svg картинка соотвествующая настройкам пользователя.
Посмотреть картинку можно по нажатию на кнопку "посмотреть карточку".
## Механизм подготовки печати и самой печати
Сначала создается html документ где создается введенное пользователем количество каждой этикетки. Если нажат флажок "с новой строки", то каждый вид этикетки будет начинаться с новой строки.
Затем  html конвертируется в pdf с помощью wkhtmltopdf и из pdf в картинки страниц в формате png для просмотра пользователем общего вида документа перед печатью. 
Печать осуществляется с помощью Sumatra в фоновом режиме.
