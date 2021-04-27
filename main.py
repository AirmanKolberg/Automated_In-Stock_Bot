from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from secrets import *
from twilio_settings import text_me, call_me


def check_if_product_in_stock(product_link):
    # Open a browser-less Selenium driver
    options = Options()
    options.headless = True
    firefox = webdriver.Firefox(options=options)

    firefox.get(product_link)
    source_code = firefox.page_source

    for tag in out_of_stock_tags:
        if tag in source_code:
            return False
    return True


if __name__ == '__main__':
    while True:
        for site in product_sites:
            in_stock_message = f"In stock!  Click link:\n{site}"
            in_stock = check_if_product_in_stock(site)
            
            if in_stock:
                text_me(in_stock_message)
                call_me()
                print(f'In stock!\n{site}')

                # Remove site from list to prevent repeat notifications
                product_sites.remove(site)
