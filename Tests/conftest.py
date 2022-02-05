import sys
import time
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
sys.path.insert(0, '/Volumes/Work/Python_courses/Project/POM')


# @pytest.fixture(scope='class')
# def printing_name_case():
#     print('\nStarting new test suit...')
#     yield
#     print('\nEnding test suit...')
#     # time.sleep(10)
#     # os.system('ls results')


@pytest.fixture(scope='function')
def logs():
    # to get the name of the test case file name at runtime
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # FileHandler class to set the location of log file
    fileHandler = logging.FileHandler('./logfile.log', mode='a', delay=False)
    # Formatter class to set the format of log file
    formatter = logging.Formatter("[%(asctime)s] -- [%(levelname)s][%(lineno)d]--[%(name)s]: \n%(message)s")
    # object of FileHandler gets formatting info from setFormatter #method
    fileHandler.setFormatter(formatter)
    # logger object gets formatting, path of log file info with addHandler #method
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(fileHandler)
    # setting logging level to INFO
    return logger


def pytest_addoption(parser):
    parser.addoption('--browser.name', action='store', default='chrome',
                     help="Choose browser: chrome or safari")
    parser.addoption('--headmode', action='store', default='true',
                     help='Choose turn on or turn off headless mode')
    # parser.addoption('--language', action='store', default=None,
    #                  help='Choose language: ru, en...(etc)')


@pytest.fixture(scope='session')
def clearing_results_folder():
    print('\nClearing results folder...')
    time.sleep(2)
    os.system("rm -rf /Volumes/MacOS/Users/maxkazliakouski/.jenkins/workspace/POM_tests/allure-results/*")


@pytest.fixture(scope='class')
def browser(request):
    browser_name = request.config.getoption('browser.name')
    headless = request.config.getoption('headmode')
    # opt = Options()
    # opt.add_argument("--disable-infobars")
    # opt.add_argument("start-maximized")
    # opt.add_argument("--disable-extensions")
    # opt.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    print(f'\nStarting browser {browser_name}...')
    global browser
    # user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        # here we set in commandline choosing for headless mode
        if headless == 'true':
            options = webdriver.ChromeOptions()
            # adding browser options!!! important
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            # options.add_argument("--disable-notifications")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
            options.headless = True
            s = Service('/Volumes/Work/Python_courses/Project/POM/Tools/chromedriver')
            browser = webdriver.Chrome(service=s, options=options)
            # browser = webdriver.Chrome('/Volumes/Work/TestProject/tools/chromedriver', options=options)
            browser.maximize_window()
            browser.implicitly_wait(5)
        else:
            # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
            options.headless = False
            s = Service('/Volumes/Work/Python_courses/Project/POM/Tools/chromedriver')
            browser = webdriver.Chrome(service=s, options=options)
            browser.maximize_window()
            browser.implicitly_wait(5)
    elif browser_name == 'safari':
        if headless == 'true':
            # options = webdriver.Safari()
            # options.headless = True
            browser = webdriver.Safari()
        else:
            # fp = webdriver.FirefoxProfile(options=options)
            # fp.set_preference("intl.accept_languages", user_language)
            # browser = webdriver.Firefox(executable_path='/Users/maxkazliakouski/Downloads/geckodriver')
            browser = webdriver.Safari()
            browser.maximize_window()
            print(f'Start {browser_name} browser for test...')
    else:
        print(f'Browser {browser_name} still not implemented')

    yield browser
    print(f'\nQuit browser {browser_name}...')
    # browser quit don't fit for safari, get the error about refuse connection
    browser.quit()

    # return os.system('allure serve results')

# def parser(section, value):
#     config = ConfigParser()
#     config.read('/Volumes/Work/Parse_project/data_for_test/test_data_hw21.ini')
#     value = config.get(section, value)
#     return value


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call' or report.when == "setup":
#         # указываем URL на котором производилось тестирование
#         extra.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="/Practice_automatization/Screen/%s"' \
#                        'alt="screenshot" style="width:400px;height:250px;"' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(file_name):
#     browser.get_screenshot_as_file('/Volumes/Work/Stepik_Python/Practice_automatization/Screen/' + file_name)
#     # driver.get_screenshot_as_file(name)
#     # report = '/Volumes/Work/Stepik_Python/Practice_automatization/Tests/report.html'
#     # new_place_for_report = '/Volumes/Work/Stepik_Python/Practice_automatization/Test_report'
#     # time.sleep(10)
#     # shutil.move(report, new_place_for_report)
