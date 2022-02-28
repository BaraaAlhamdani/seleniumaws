from selenium import webdriver  # imports selenium to the file
import moodle_locatores as locators
from time import sleep
#from selenium.webdriver.chrome.service import Service
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # add this import for drop down list
import sys

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)


def setUp():
    print(f'launch Moodle App')
    print('---------------------------------')
    # make browser full screen
    driver.maximize_window()

    # Give browser up to 30 seconds to respond
    driver.implicitly_wait(30)

    # Navigate to moodle app website
    driver.get(locators.moodle_url)

    # check that moodle URL and the whole page title are displayed
    if driver.current_url == locators.moodle_url and driver.title == locators.moodle_home_page_title:
        print('Yey! Moodle Launched successfully')
        print(f'Moodle homepage URL: {driver.current_url}\nHome page Title: {driver.title}')
        sleep(5)

    else:
        print(f'{locators.app} did not launch, check your code or application!')
        print(f'Current URL: {driver.current_url}\nHome page Title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print('------------------------------------------')
        print(f'The test completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


# login to moodle
def log_in(username, password):
    if driver.current_url == locators.moodle_url:  # check we are on the home page
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.moodle_login_page_url:  # check we are on the login page
            print(f'{locators.app} App Login page is displayed!')
            sleep(0.25)
            driver.find_element(By.ID, 'username').send_keys(username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(password)
            sleep(0.25)
            # driver.find_element(By.ID, 'loginbtn').click() #method 1 using ID
            # Locators XPATH practice
            # driver.find_element(By.XPATH, '//button[contains(.,"Log in")]').click()
            # driver.find_element(By.XPATH, '//button[contains(.,"Log in")]').click()
            # driver.find_element(By.XPATH, '//button[contains(@id,"loginbtn")]').click()
            # driver.find_element(By.XPATH, '//*[@id="loginbtn"]').click()
            driver.find_element(By.CSS_SELECTOR, 'button[id*="loginbtn"]').click()

            # validate we are at the Dashboard
            if driver.title == locators.moodle_dashboard_page_title and driver.current_url == locators.moodle_dashboard_url:
                assert driver.current_url == locators.moodle_dashboard_url
                assert driver.title == locators.moodle_dashboard_page_title
                print(f'Login Successful. {locators.app} Dashboard is displayed - Page title: {driver.title}')
            else:
                print(f'Dashboard is not displayed. Check your code and try again')


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    if driver.current_url == locators.moodle_url:
        print(f'----- Logout Successful! at {datetime.datetime.now()}')


def create_new_user():
    # navigate to site Admin
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    # validate we are on 'Add a new user'
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    assert driver.title == locators.moodle_add_new_user_page_title
    print(f'----- Navigate to Add a new user page - page Title: {driver.title}')
    # breakpoint()
    sleep(0.25)
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text(
        'Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text(locators.country)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(0.25)
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'Server files').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'sl_Frozen').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'sl_How to build a snowman').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'Course image').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'gieEd4R5T.png').click()
    # sleep(0.25)
    img_path = ['Server files', 'sl_Frozen', 'sl_How to build a snowman', 'Course image', 'gieEd4R5T.png']
    for p in img_path:
        driver.find_element(By.LINK_TEXT, p).click()
        sleep(0.25)

    driver.find_element(By.XPATH, '//input[@value="4"]').click()  # method 1
    driver.find_element(By.XPATH, '//label[contains(.,"Create an alias/shortcut to the file")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(.,"Select this file")]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_desc)
    driver.find_element(By.LINK_TEXT, 'Additional names').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.first_name)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.last_name)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.middle_name)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.first_name)
    sleep(0.25)

    driver.find_element(By.LINK_TEXT, 'Interests').click()
    for tag in locators.list_of_interests:
        # driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(tag)
        driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(tag + "\n")
        sleep(0.25)

    driver.find_element(By.LINK_TEXT, 'Optional').click()
    for i in range(len(locators.list_opt)):
        opt, ids, val = locators.list_opt[i], locators.list_ids[i], locators.list_val[i]
        # print(f'Populate {opt} field')
        driver.find_element(By.ID, ids).send_keys(val)
        sleep(0.25)

    driver.find_element(By.ID, 'id_submitbutton').click()
    sleep(0.25)
    print(f'----- New User "{locators.new_username},{locators.new_password},{locators.email}" is added -----')


def search_user():
    if driver.current_url == locators.moodle_users_main_page and driver.title == locators.moodle_users_main_page_title:
        assert driver.find_element(By.LINK_TEXT, 'Browse list of users').is_displayed()
        print('\'Browse list of users page\' is displayed')
        sleep(0.25)
        print(f'----- Search for user by email address: {locators.email} -----')
        driver.find_element(By.ID, 'id_email').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()

        if driver.find_element(By.XPATH, f'//td[contains(.,"{locators.email}")]'):
            print(f'----- user: {locators.email} is found')


def check_new_user_can_login():
    print('check_new_user_can_login()')
    if driver.title == locators.moodle_dashboard_page_title and driver.current_url == locators.moodle_dashboard_url:
        if driver.find_element(By.XPATH, f'//span[contains(.,"{locators.full_name}")]').is_displayed():
            print(f'----- user full name is: {locators.full_name}')
            logger('created')


def delete_user():
    # navigate to site Admin
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(0.25)
    search_user()
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.full_name}")]').is_displayed()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[contains(@title,"Delete")]').click()
    sleep(0.25)
    assert driver.find_element(By.TAG_NAME, 'h2').is_displayed()
    sleep(0.25)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.full_name}")]').is_displayed()
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(.,"Delete")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Browse list of users').is_displayed()
    sleep(0.25)
    print(f'User name: {locators.full_name} is deleted ')
    logger('Deleted')


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('../class/message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.new_username}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()

# -------- Create New User ------------
# setUp()
# log_in(locators.admin_username, locators.admin_password) # Login as admin
# create_new_user()
# search_user()
# log_out()
# # ----------------------------------------------
# # Login as new user
# log_in(locators.new_username, locators.new_password)
# check_new_user_can_login()
# #logger('created')
# log_out()
# # ----------------------------------------------
# # --------- Delete New user --------------------
# log_in(locators.admin_username,locators.admin_password)
# search_user()
# delete_user()
# log_out()
# # ----------------------------------------------
# tearDown()
