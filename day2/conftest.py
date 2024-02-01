from pytest import fixture
from selenium import webdriver
import json

data_path = 'test_data.json'


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        print(f" these are in json file: {data}")
        return data
        
@fixture(params=[webdriver.Chrome, webdriver.Edge])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()

@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data
