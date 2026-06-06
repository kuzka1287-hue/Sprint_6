# Проект Sprint_6: автотесты для «Яндекс.Самокат»

## Запуск
1. Установить зависимости: `pip install -r requirements.txt`
2. Скачать geckodriver и поместить в `PATH` или в корень проекта.
3. Выполнить команду: `pytest tests --browser=firefox -v`

## Allure-отчёт
```bash
pytest tests --alluredir=allure_results
allure serve allure_results
