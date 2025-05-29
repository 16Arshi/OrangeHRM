import pytest
from pytest_metadata.plugin import pytest_addoption
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Specify the browser: chrome or edge or firefox")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



@pytest.fixture()
def setup(browser):
    global driver
    if browser=="chrome":
      driver=webdriver.Chrome()

    elif browser == "edge":
      driver = webdriver.Edge()

    elif browser == "firefox":
      driver = webdriver.Firefox()

    else:
        raise ValueError("Unsupported browser")

    return driver

from pytest_metadata.plugin import metadata_key

def pytest_configure(config):
    config.stash[metadata_key]['Project Name']='Orange HRM'
    config.stash[metadata_key]['Test Module Name']='Login page'
    config.stash[metadata_key]['Tester Name']='Arshi Khan'

#to remove the elements
#@pytest.mark.optionalhook
#def pytest_metadata(metadata):
    #metadata.pop('name of the elemnet to be removed',NONE)

