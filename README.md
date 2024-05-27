**Скрипт автоматической загрузки видео на ваш ютуб канал**


1. **Подготовка** 
- Установи зависимости ```pip install requirements.txt```
- В папку videos закинь видео которые требуется загрузить на YT
- Открой Chrome и залогинься в YT канал в который будут загружаться видео
- В настройках канала [YT ](https://studio.youtube.com/) во вкладке *Загрузка видео* в *Параметры доступа* выбери один из способов публикации видео (Открытый доступ, Ограниченный доступ или Доступ по ссылке)
- Поменяй путь до User Data и chrome.exe в строках 43, 44 в файле main.py:
- options.add_argument("user-data-dir=C:\\Users\\qwe qwe\\AppData\\Local\\Google\\Chrome\\User Data")  
- options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

2. **Запуск**
- В терминале проекта youtube-auto-upload введи команду ```python main.py```
- Готово


