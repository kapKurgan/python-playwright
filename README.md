# Тестирование UI (python - playwright)

---

# Над проектом ведётся работа

---

## Цель

Создание автоматизированного тестового фреймворка для проверки функциональности UI с генерацией тестовых данных, системой отчетности.
Тестовый стенд:
```bash
http://selenium1py.pythonanywhere.com/
```


## Задачи

- Проверка локализации (5 тестов)
- Проверка регистрации (2 теста)
- Проверка авторизации (2 теста)

---

## Оглавление

- [CI/CD](#cicd)
- [URL отчетов GitHub Pages](#url-отчетов-github-pages)
- [Интеграция с GitHub Actions](#интеграция-с-github-actions)

---

## CI/CD

В этом проекте включена интеграция с GitHub Actions. 

Конфигурацию можно найти в [ui-tests.yml](./.github/workflows/ui-tests.yml).

---

## URL отчетов GitHub Pages

### HTML
```bash
https://kapKurgan.github.io/python-playwright/<run_id>/pytest-report.html
```

Например:
https://kapKurgan.github.io/python-playwright/20694656893/pytest_report.html


### ALLURE 
```bash
https://kapKurgan.github.io/python-playwright/<run_id>/allure-report/index.html
```

Например:
https://kapKurgan.github.io/python-playwright/20694656893/allure-report/index.html

---

## Требования
- Python 3.12+
- GitHub account (для CI/CD и GitHub Pages)

Установка зависимостей:
```bash
pip install -r requirements.txt
```

--- 

## Интеграция с GitHub Actions

Workflow автоматически:
- Устанавливает Python 3.12
- Устанавливает зависимости
- Запускает тесты к реальному UI
- Генерирует HTML-отчеты
- Публикует отчеты в GitHub Pages

---
