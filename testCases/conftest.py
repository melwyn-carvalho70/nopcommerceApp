from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        # service object
        serv_object = Service("C:/Users/User/OneDrive/Documents/Webdrivers/chromedriver.exe")
        driver = webdriver.Chrome(service=serv_object)  # object for chrome class
        print("Launching Chrome")

    elif browser == 'firefox':
        # service object
        options = Options()
        options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
        serv_object = Service("C:/Users/User/OneDrive/Documents/Webdrivers/geckodriver.exe")
        driver = webdriver.Firefox(options=options, service=serv_object)  # object for chrome class
        print("Launching Firefox")

    elif browser == 'edge':
        # service object
        serv_object = Service("C:/Users/User/OneDrive/Documents/Webdrivers/msedgedriver.exe")
        driver = webdriver.Edge(service=serv_object)  # object for chrome class
        print("Launching Edge")

    return driver

def pytest_addoption(parser):    # This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This wll return browser value to setup method
    return request.config.getoption("--browser")


################# Pytest HTML Report ###################

# Hook for Adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['module Name'] = 'Customers'
    config._metadata['Tester'] = 'Melwyn'

# Hook for delete/modify environment info to HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


