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

coffee_block = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
coffee_title = (By.CSS_SELECTOR, "[data-component-type='s-search-result'] h2")
coffee_pic = (By.CSS_SELECTOR, "[data-component-type='s-product-image'] a")
BEST_SELLER = (By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")


#@given('open {search_word}')
#def open_amazon(context, search_word):
#    context.driver.get("https://www.amazon.com/")


@given('open amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()





@given('open amazon product {product_id}page')
def open_product(context, product_id):
    context.driver.get(f"https://www.amazon.com/gp/product/B07BJKRR25/")




#@when('search for {search_word}')
#def open_customer_service(context, search_word):
#    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")
#    sleep(1)





#@then('search for {search_word}')
#def open_canceled_items(context, search_word):
#    context.driver.find_element(*SEARCH_INPUT).send_keys('cancel order', Keys.ENTER)
#    context.driver.find_element(*BB_SEARCH).send_keys('basketball', Keys.ENTER)
#    sleep(1)


@then('search for {search_word}')
def open_canceled_items(context, search_word):
    context.app.header.Search_amazon(search_word)




#@then('verify the {search_word} page comes')
#def verify_canceled_page(context, search_word):
#    expected_result = context.driver.get("https://www.amazon.com/gp/help/customer/display.html?help_keywords=canceled+order&search")
#    actual_result = context.driver.get("https://www.amazon.com/gp/help/customer/display.html?help_keywords=canceled+order&search")

#    assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected{expected_result}'





#@then('verify that evey product has name and image')
#def verify_name_image(context):
#    all_product = context.driver.find_elements(*coffee_block)
#    for product in all_product:
#        title = product.find_element(*coffee_title).text
#        assert title != '', 'Error! title should not be empty'
#        print(title)

#        product.find_element(*coffee_pic)



