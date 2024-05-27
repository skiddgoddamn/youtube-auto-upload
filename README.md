**Скрипт автоматической загрузки видео на ваш ютуб канал**


1. **Подготовка** 
1.1 Установи зависимости ```pip install requirements.txt```
1.2 В папку videos закинь видео которые требуется загрузить на YT
1.3 Открой Chrome и залогинься в YT канал в который будут загружаться видео
1.4 В настройках канала [YT ](https://studio.youtube.com/) во вкладке *Загрузка видео* в *Параметры доступа* выбери один из способов публикации видео (Открытый доступ, Ограниченный доступ или Доступ по ссылке)
1.5 Поменяй путь до User Data и chrome.exe в строках 43, 44 в файле main.py:
options.add_argument("user-data-dir=C:\\Users\\qwe qwe\\AppData\\Local\\Google\\Chrome\\User Data")  
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

2. **Запуск**
2.2 В терминале проекта youtube-auto-upload введи команду ```python main.py```
2.3 Готово


