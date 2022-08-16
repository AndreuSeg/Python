# No funciona este archivo pk han parcheado las paginas de Coolmod y de PCComponentes
from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def check_stock():
    url = "https://www.pccomponentes.com/asus-geforce-gtx-1050-tis-4gb-gddr5"
    url_sfera = "https://www.sfera.com/es/rebajas-hombre/pantalones/bermuda-lino-21319b4/05556/"
    session = HTMLSession()
    product_page = session.get(url_sfera)
    found = product_page.html.find("#product_button_add1")
    if len(found) > 0:
        driver = webdriver.Firefox()
        driver.get(url_sfera)
        driver.find_element_by_class_name("confirm").click()
        driver.find_element_by_class_name("accept").click()
        driver.find_element_by_class_name("button-buy").click()
        sleep(1)
        driver.find_element_by_class_name("confirm").click()
        # Esto es por si vuelve a salir la silla razer
        try:
            driver.find_element_by_class_name("confirm").click()
        except NoSuchElementException:
            print("No habia silla razer")
        driver.find_element_by_class_name("button-buy").click()
        is_form_loaded = False
        form = None
        while not is_form_loaded:
            try:
                form = driver.find_element_by_class_name("login100-form")
                is_form_loaded = True
            except NoSuchElementException:
                print("Puessss no esta el formulario...")

        email = form.find_element_by_name("jform[email]")
        password = form.find_element_by_name("jform[password]")
        email.send_keys("nate@nate.com")
        password.send_keys("megustarazer")
        driver.find_element_by_class_name("login100-form-btn").click()



def main():
    check_stock()


if __name__ == "__main__":
    main()
