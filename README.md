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

<img title="Python" src="qa_guru_python_8_15/pictures/icons/python-original.svg" height="40" width="40"/> <img title="Pytest" src="qa_guru_python_8_15/pictures/icons/pytest-original.svg" height="40" width="40"/> <img title="Jira" src="qa_guru_python_8_15/pictures/icons/jira-original.svg" height="40" width="40"/> <img title="Allure Report" src="qa_guru_python_8_15/pictures/icons/Allure_Report.jpg" height="40" width="40"/> <img title="Allure TestOps" src="qa_guru_python_8_15/pictures/icons/AllureTestOps.jpg" height="40" width="40"/> <img title="GitHub" src="qa_guru_python_8_15/pictures/icons/github-original.svg" height="40" width="40"/> <img title="Selenoid" src="qa_guru_python_8_15/pictures/icons/selenoid.jpg" height="40" width="40"/> <img title="Selenium" src="qa_guru_python_8_15/pictures/icons/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="qa_guru_python_8_15/pictures/icons/selene.jpg" height="40" width="40"/> <img title="Pycharm" src="qa_guru_python_8_15/pictures/icons/pycharm.jpg" height="40" width="40"/> <img title="Telegram" src="qa_guru_python_8_15/pictures/icons/tg.jpg" height="40" width="40"/> <img title="Jenkins" src="qa_guru_python_8_15/pictures/icons/jenkins-original.svg" height="40" width="40"/>

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

![jenkins project main page](qa_guru_python_8_15/pictures/jenkins_project_main_page.jpg)

2. Нажать "Build with Parameters"
4. Из списка "CONTEXT" выбрать: PROD
5. Оставить run_remote = true
6. Нажать "Build"

![jenkins_build](qa_guru_python_8_15/pictures/jenkins_build.jpg)

----

### Allure отчет
#### Общие результаты 
![allure_report_overview](qa_guru_python_8_15/pictures/allure_report_overview.jpg)

#### Результаты прохождения теста
![allure_reports_behaviors](qa_guru_python_8_15/pictures/allure_reports_behaviors.jpg)

#### Графики

![allure_reports_graphs](qa_guru_python_8_15/pictures/alluere_reports_graphs_1.jpg)
![allure_reports_graphs](qa_guru_python_8_15/pictures/alluere_reports_graphs_2.jpg)

----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3863/dashboards">Ссылка на проект</a>

#### Дашборд с общими показателями тестовых прогонов

![allure_test_ops_dashboards](qa_guru_python_8_15/pictures/allure_testops_dashboards.jpg)

#### История запуска тестовых наборов

![allure_testops_launches](qa_guru_python_8_15/pictures/allure_testops_launches.jpg)

#### Тест кейсы

![allure_testops_suites](qa_guru_python_8_15/pictures/allure_testops_suites.jpg)

----

### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-985">Ссылка на проект</a>

![jira_project](qa_guru_python_8_15/pictures/jira_project.jpg)

----

### Оповещения в Telegram
![telegram_allert](qa_guru_python_8_15/pictures/telegram_allert.jpg)

----

### Видео прохождения автотеста
![autotest_mp4](qa_guru_python_8_15/pictures/autotest.mp4)

----

### Mind map тест плана

![allure_reports_graphs](qa_guru_python_8_15/pictures/test-case-mind-map.jpg)
