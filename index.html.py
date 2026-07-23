<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anna's English School</title>
    <!-- Подключаем Telegram WebApp SDK -->
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        :root {
            --bg-color: #fdfbf7;
            --text-color: #4a3e3d;
            --accent-color: #c89d7c;
            --card-bg: #ffffff;
            --border-radius: 16px;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .header {
            text-align: center;
            margin-bottom: 24px;
        }

        .header h1 {
            font-size: 22px;
            margin: 8px 0 4px;
            font-weight: 600;
            letter-spacing: 1px;
        }

        .header p {
            font-size: 13px;
            color: #8c7a6b;
            margin: 0;
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }

        .card-grid {
            width: 100%;
            max-width: 400px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 20px;
        }

        .card {
            background: var(--card-bg);
            padding: 16px;
            border-radius: var(--border-radius);
            box-shadow: 0 4px 15px rgba(200, 157, 124, 0.08);
            border: 1px solid rgba(200, 157, 124, 0.15);
            text-align: center;
        }

        .card h3 {
            margin: 0;
            font-size: 24px;
            color: var(--accent-color);
        }

        .card p {
            margin: 4px 0 0;
            font-size: 12px;
            color: #7a6e65;
        }

        .main-btn {
            width: 100%;
            max-width: 400px;
            background-color: var(--accent-color);
            color: white;
            border: none;
            padding: 14px;
            border-radius: var(--border-radius);
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(200, 157, 124, 0.3);
            transition: transform 0.1s ease;
        }

        .main-btn:active {
            transform: scale(0.98);
        }
    </style>
</head>
<body>

    <div class="header">
        <p>Learn • Grow • Connect</p>
        <h1>ANNA'S ENGLISH SCHOOL</h1>
    </div>

    <div class="card-grid">
        <div class="card">
            <h3 id="student-count">0</h3>
            <p>Студентов</p>
        </div>
        <div class="card">
            <h3 id="lesson-count">0</h3>
            <p>Уроков сегодня</p>
        </div>
    </div>

    <button class="main-btn" onclick="addLesson()">➕ Добавить урок</button>

    <script>
        // Инициализируем Telegram WebApp
        const tg = window.Telegram.WebApp;
        tg.expand(); // Разворачиваем на весь экран

        function addLesson() {
            // Отправляем обратную связь в виде вибрации
            if (tg.HapticFeedback) {
                tg.HapticFeedback.impactOccurred('medium');
            }
            tg.showAlert("Здесь откроется форма добавления урока!");
        }
    </script>
</body>
</html>