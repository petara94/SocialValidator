import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import json
from src.resource.config import CONFIG
import warnings


class SimpleChecker(object):
    def __init__(self):
        self.__url = ""

    def seturl(self, url):
        self.__url = url

    def isValidUser(self, url):
        self.seturl(url)
        try:
            req = requests.get(url)
        except:
            return "Bad connection"

        return req.status_code == 200


class XingChecker(object):
    def __init__(self, cookies):
        self.__url = ""

        self.__BASE_REQ_DATA = CONFIG["REQUEST_DATA"]

        self.__BASE_HEADERS = CONFIG["REQUEST_HEADERS"]
        self.__BASE_HEADERS["Cookie"] = cookies

    def IsXingUser(self, url="-1"):
        if url != "-1":
            self.__url = url
        else:
            url = self.__url

        self.__BASE_REQ_DATA["variables"]["profileId"] = self._linkToUserName(url)
        self.__BASE_HEADERS["Content-Length"] = str(len(json.dumps(self.__BASE_REQ_DATA)))

        req = requests.post(CONFIG["XING_API_URL"], json=self.__BASE_REQ_DATA, headers=self.__BASE_HEADERS)
        return "\"errors\":" not in req.text

    def _linkToUserName(self, url):
        url = url.split('/')
        return url[url.index("profile") + 1]


class XingAuth(object):
    def __init__(self, login, password):
        warnings.filterwarnings("ignore")
        self.__driver = webdriver.PhantomJS(
            executable_path="src\\driver\\phantomjs.exe")
        self.__authdata = dict()
        self.__login = login
        self.__password = password

    def authdict(self):
        return self.__authdata

    def __Login(self):
        self.__driver.get("https://login.xing.com/")
        inputs = self.__driver.find_element_by_css_selector(
            "form").find_elements_by_css_selector("input")[:2]
        inputs[0].send_keys(self.__login)
        inputs[1].send_keys(self.__password)
        self.__driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)

    def Close(self):
        self.__driver.quit()

    def GetAuth(self):
        self.__Login()
        self.__authdata["visitor_id"] = self.__driver.get_cookie("visitor_id")#["value"]
        self.__authdata["login"] = self.__driver.get_cookie("login")#["value"]
        return self.__authdata
