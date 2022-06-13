from selenium import webdriver
from creds import username, password, code
import time

def deleteVideo():
    url = f"https://steamcommunity.com/login/home/?goto="
    options = webdriver.ChromeOptions()

    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36")

    driver = webdriver.Chrome(
        executable_path="chromedriver.exe",
        options=options
    )
    driver.get(url=url)
    time.sleep(2)
    my_username = driver.find_element_by_id("input_username")
    my_username.clear()
    my_username.send_keys(username)
    my_password = driver.find_element_by_id("input_password")
    my_password.clear()
    my_password.send_keys(password)
    login_button = driver.find_element_by_class_name("login_btn").click()
    time.sleep(15)
    family_code = driver.find_element_by_id("steam_parental_password_box")
    family_code.clear()
    family_code.send_keys(code)
    send_button = driver.find_element_by_id("submit_btn").click()
    time.sleep(3)
    url = f"https://steamcommunity.com/id/D4SuCE/videos/"
    driver.get(url=url)
    time.sleep(3)
    page_numbers = driver.find_elements_by_class_name("pagingPageLink")[-1].text
    time.sleep(1)
    for i in range(65):
        manage_button = driver.find_element_by_id("ScreenshotManagementToggle").click()
        time.sleep(1)
        select_all_button = driver.find_element_by_id("ScreenshotManagementButtonSelectAll").click()
        time.sleep(1)
        select_all_button = driver.find_element_by_id("button_submit_manage").click()
        time.sleep(1)
        select_all_button = driver.find_element_by_id("modalWarningContinueBtn").click()
        time.sleep(3)

def main():
    deleteVideo();

if (__name__ == "__main__"):
    main()
