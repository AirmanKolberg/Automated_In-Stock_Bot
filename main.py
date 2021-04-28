from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from secrets import *
from twilio_settings import text_me, call_me


def open_webpage_in_browser(site):
    buyer_browser = webdriver.Firefox()
    buyer_browser.get(site)
    buyer_browser.maximize_window()


def check_if_product_in_stock(product_link):
    # Open a browser-less Selenium driver
    options = Options()
    options.headless = True
    firefox = webdriver.Firefox(options=options)

    firefox.get(product_link)
    source_code = firefox.page_source
    firefox.close()

    for tag in out_of_stock_tags:
        if tag in source_code:
            return False
    return True


if __name__ == '__main__':
    while True:
        # Closes app if all products are in-stock
        if product_sites == list():
            exit()

        for site in product_sites:
            in_stock_message = f"{product_sites[site]} in stock!  Link:\n{site}"
            in_stock = check_if_product_in_stock(site)

            if in_stock:
                text_me(in_stock_message)
                call_me()
                print(in_stock_message)
                open_webpage_in_browser(site)

                # Remove site from list to prevent repeat notifications
                product_sites.pop(site)
            else:
                print(f'{product_sites[site]} not in stock:\n{site}\n')
