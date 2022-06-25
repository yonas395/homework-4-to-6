from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

SIN_BTN = (By.CSS_SELECTOR, "div[class='nav-signin-tt nav-flyout'] [class*='nav-action-inner']")
SIN_PAGE = (By.CSS_SELECTOR, "#a-page div[class='a-section a-padding-medium auth-workflow']")

@when('click on button from signin popup')
def click_sign_in_btn(context):
    Signin = context.driver.wait.until(
        EC.element_to_be_clickable(SIN_BTN), 'signin button not clickable'
    )
    Signin.click()



@when("Wait for {seconds} seconds")
def wait_sec(context, seconds):
    sleep(int(seconds))


@then('SignIn popup is present')
def verify_signin_popup_present(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIN_BTN), 'sign in button not clickable')



@then('verify sign in page is opened')
def verify_sign_in_page(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.'
                                              'return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.'
                                              'identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.'
                                              'assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.'
                                              'openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&'),
                              message='sign in never opened')

    expected_result = 'sign in page must opened'
    actual_result = context.driver.find_element(*SIN_PAGE)

    assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected{expected_result}'


@then('SignIn popup disappears')
def verify_sign_in_page_not_present(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIN_BTN), 'sign in btn not disappear')
