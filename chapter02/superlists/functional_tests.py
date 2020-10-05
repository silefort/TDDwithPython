from selenium import webdriver

# Starting a Selenium "webdriver" to pop up a real Firefox browser Window
browser = webdriver.Firefox()
# Using it to open up a web page which we're expecting to be served from our local computer
browser.get('http://localhost:8000')

# Checking that the page has the word "Django" in its title
assert 'Django' in browser.title
