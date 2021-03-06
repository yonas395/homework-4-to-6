from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SEARCH_INPUT = (By.XPATH, "//input[@type='search']")
SEARCH_BTN = (By.CSS_SELECTOR, "div.a-box-inner .help-content")
BB_SEARCH = (By.ID, 'twotabsearchtextbox')
SUBMIT = (By.ID, 'nav-search-submit-button')
F_ITEM = (By.XPATH, "//div[@data-component-type='s-impression-counter']//div[@class='a-price-whole']")
BST_SELL = (By.CSS_SELECTOR, "#zg_header a")
COLOR_OPT = (By.CSS_SELECTOR, '#softlinesTwister_feature_div ul')
COLOR_NAME = (By.CSS_SELECTOR, "#a-autoid-7-announce .imgSwatch")


@given('open amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f"https://www.amazon.com/gp/product/B07X8XJRS9/?th=1/")


@given('open {search_word}')
def open_amazon(context, search_word):
    context.driver.get("https://www.amazon.com/")


@when('search for {search_word}')
def open_customer_service(context, search_word):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")
    sleep(1)


@then('open{search_word}')
def open_best_sellers_page(context, search_word):
     context.driver.get("https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab")
     sleep(3)


@then('search for {search_word}')
def open_canceled_items(context, search_word):
    context.driver.find_element(*SEARCH_INPUT).send_keys('cancel order', Keys.ENTER)
    context.driver.find_element(*BB_SEARCH).send_keys('basketball', Keys.ENTER)
    sleep(1)


@then('verify the {search_word} page comes')
def verify_canceled_page(context, search_word):
    expected_result = context.driver.get("https://www.amazon.com/gp/help/customer/display.html?help_keywords=canceled+order&search")
    actual_result = context.driver.get("https://www.amazon.com/gp/help/customer/display.html?help_keywords=canceled+order&search")

    assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected{expected_result}'


@then('verify there are {expected_amount} links')
def verify_there_are_links(context, expected_amount):
    header_links = context.driver.find_elements(*BST_SELL)
    expected_amount = context.driver.find_elements(*BST_SELL)
    assert len(header_links) == len(expected_amount), f'Expected {expected_amount} links, but got {len(header_links)}'


@then('verify user can click through colors')
def verify_colors(context):
    expected_colors = ['black', 'Blue, Over Dye', 'White', 'Dark Blue Vintage', 'Dark Wash']
    actual_colors = []

    color_options = context.driver.find_elements(*COLOR_OPT)
    for option in color_options:
        option.click()
        sleep(5)
        color_name = context.driver.find_element(*COLOR_NAME).text
        actual_colors += [color_name]

        assert actual_colors == expected_colors, f'Error! Expected {expected_colors}, but got {actual_colors}'


