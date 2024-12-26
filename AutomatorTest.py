from Automator import BrowserTypes, Automator

#samples of xpath
#//*[@name='????' and @title='?????']
#//*[(@id='?????') and not(@class='??????')]

#simple login page sample
try :
    automator = Automator(BrowserTypes.EDGE, "https://testpages.eviltester.com/styled/cookies/adminlogin.html")
    automator.set_speed(1)
    automator.send_keys_to_xpath_element("//*[@id='username' and @name='username']", 10, "Admin")
    automator.send_keys_to_xpath_element("//*[@name='password' and @name='password']", 10, "AdminPass")
    automator.send_click_to_xpath_element("//*[@id='login']", 10)
    automator.fixed_delay(5)
    automator.close_browser()
except ValueError as e:  
    print(e)
    pass #do nothing


