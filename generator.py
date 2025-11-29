#!/usr/bin/env python3
"""
Генератор статического каталога мотоциклов
"""

import yaml
import os
import shutil

def main():
    """Основная функция"""
    print("🚀 Запуск генерации каталога...")
    
    # Создаем папку docs если её нет
    os.makedirs('docs', exist_ok=True)
    
    # Создаем простейшую главную страницу
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MotoMaster Каталог</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container">
                <a class="navbar-brand" href="/">🏍️ MotoMaster Каталог</a>
            </div>
        </nav>
        <div class="container mt-4">
            <h1>Добро пожаловать в каталог мотоциклов!</h1>
            <p>Скоро здесь появятся технические характеристики.</p>
            <div class="alert alert-info">
                Сайт в разработке. Возвращайтесь позже!
            </div>
        </div>
    </body>
    </html>
    """
    
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Базовая страница создана!")

if __name__ == "__main__":
    main()
