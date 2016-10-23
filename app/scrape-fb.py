import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from app import scrape_main

# extrair dados com CSS Selectors
firefox = webdriver.Firefox()
firefox.get('https://www.facebook.com/')

usuario = scrape_main.usr
senha = scrape_main.pwd
assert "Facebook" in firefox.title
elem = firefox.find_element_by_id("email")
elem.send_keys(usuario)
elem = firefox.find_element_by_id("pass")
elem.send_keys(senha)
elem.send_keys(Keys.RETURN)
sleep(10)

post_box=firefox.find_element_by_name("xhpc_message").send_keys("Testando Postagem com Seleinum - Automação Cobolman!.")
sleep(2)
post_it=firefox.find_element_by_xpath("//*[text()='Publicar']").click()

print ("Posted...")



