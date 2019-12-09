from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser  = webdriver.Firefox()

browser.get('https://www.quora.com/topic/Fashion-and-Style-Advice/all_questions')


post = browser.find_element_by_tag_name('body')

no_of_page = 20

while no_of_page:
    post.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    no_of_page -= 1
    
post_data = browser.find_elements_by_class_name('ui_qtext_rendered_qtext')

file = open('text.txt','w')
c = 1
for var in post_data:
    file.write(str(str(c)+var.text))
    file.write('\n')
    c += 1
file.close()
