import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class search(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Qualtop\Desktop\Selenium with python\Firefox Driver\geckodriver.exe")
    
    def test_buscar(self):
        driver = self.driver
        driver.get ("http://opencart.abstracta.us/index.php?route=common/home")
        time.sleep(2)
        
        element1=driver.find_element_by_name ("search")
        element1.send_keys("Palm Treo Pro")
        element1.send_keys(Keys.RETURN)
        
        element2__click_buscar=driver.find_element_by_xpath ("//*[@id='search']/span/button")
        element2__click_buscar.click()
        
        Addtowishlist = driver.find_element_by_xpath ("//*[@id='content']/div[3]/div/div/div[2]/div[2]/button[2]")
        Addtowishlist.click()
        
        Addtocar = driver.find_element_by_xpath ("//*[@id='content']/div[3]/div/div/div[2]/div[2]/button[1]")
        Addtocar.click()
            
        time.sleep(5)  
    
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()