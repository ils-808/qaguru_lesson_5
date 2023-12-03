# Проект по тестированию сайта "DemoQA"
> <a target="_blank" href="https://demoqa.com/">Demo QA</a>

### Особенности проекта

* Оповещения о тестовых прогонах в Telegram
* Отчеты с видео, скриншотом, логами браузера, DOM моделью страницы
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Автоматизация отчетности о тестовых прогонах в Jira
* Запуск автотестов в Selenoid

----

### Используемый стэк

<img title="Python" src="qa_guru_python_8_15/icons/python-original.svg" height="40" width="40"/> <img title="Pytest" src="qa_guru_python_8_15/icons/pytest-original.svg" height="40" width="40"/> <img title="Jira" src="qa_guru_python_8_15/icons/jira-original.svg" height="40" width="40"/> <img title="Allure Report" src="qa_guru_python_8_15/icons/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="qa_guru_python_8_15/icons/AllureTestOps.png" height="40" width="40"/> <img title="GitHub" src="qa_guru_python_8_15/icons/github-original.svg" height="40" width="40"/> <img title="Selenoid" src="qa_guru_python_8_15/icons/selenoid.png" height="40" width="40"/> <img title="Selenium" src="qa_guru_python_8_15/icons/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="qa_guru_python_8_15/icons/selene.png" height="40" width="40"/> <img title="Pycharm" src="qa_guru_python_8_15/icons/pycharm.png" height="40" width="40"/> <img title="Telegram" src="qa_guru_python_8_15/icons/tg.png" height="40" width="40"/> <img title="Jenkins" src="qa_guru_python_8_15/icons/jenkins-original.svg" height="40" width="40"/>

----

### Локальный запуск автотестов

#### Выполнить в cli:
> [!NOTE]
> Ключ выбора версии `--browser-version` не обязателен
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --browser-version=100
```

#### Получение отчёта:
```bash
allure serve build/allure-results
```

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/C08-itpmkz-lesson-15/">Ссылка</a>

#### Параметры сборки
> [!NOTE]
> Параметры сборки не обязательны
```python
CONTEXT = ['local', 'stage', 'prod'] # Окружение
run_remote = true - для запуска в CI/CD
```
#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/C08-itpmkz-lesson-15/">проект</a>

![jenkins project main page](qa_guru_python_8_15/jenkins_project_main_page.JPG)

2. Нажать "Build with Parameters"
4. Из списка "CONTEXT" выбрать: PROD
5. Оставить run_remote = true
6. Нажать "Build"

![jenkins_build](qa_guru_python_8_15/jenkins_build.JPG)

----

### Allure отчет
#### Общие результаты 
![allure_report_overview](qa_guru_python_8_15/allure_report_overview.JPG)

#### Результаты прохождения теста
![allure_reports_behaviors](qa_guru_python_8_15/allure_reports_behaviors.JPG)

#### Графики

![allure_reports_graphs](qa_guru_python_8_15/alluere_reports_graphs_1.JPG)
![allure_reports_graphs](qa_guru_python_8_15/alluere_reports_graphs_2.JPG)

----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3863/dashboards">Ссылка на проект</a>

#### Дашборд с общими показателями тестовых прогонов

![allure_test_ops_dashboards](qa_guru_python_8_15/allure_testops_dashboards.JPG)

#### История запуска тестовых наборов

![allure_testops_launches](qa_guru_python_8_15/allure_testops_launches.JPG)

#### Тест кейсы

![allure_testops_suites](qa_guru_python_8_15/allure_testops_suites.JPG)

----

### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-985">Ссылка на проект</a>

![jira_project](qa_guru_python_8_15/jira_project.JPG)

----

### Оповещения в Telegram
![telegram_allert](qa_guru_python_8_15/telegram_allert.JPG)

----

### Видео прохождения автотеста
https://github.com/ils-808/qaguru_lesson_5/assets/15216590/776b415e-80e2-4b75-b229-054c7b4e7894


----
