from selenium import webdriver

browser = webdriver.Firefox(executable_path = 'C:\\Program Files\\Mozilla Firefox\\geckodriver.exe')
browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('cover-thumb')
    #elem = browser.find_element_by_class_name('tabcap')
    print('Found <%s> element with that class name!' %(elem.tag_name))
except:
    print('Was not able to find an element with that name')
