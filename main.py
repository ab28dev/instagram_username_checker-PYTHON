import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

class InstagramBot:

    def __init__(self):

        # Launching chrome using chrome web driver
        self.driver = webdriver.Chrome('./chromedriver.exe')
        
        # Opening instagram website signup page
        self.driver.get('https://www.instagram.com/accounts/emailsignup/?hl=en')

        # Remove Existing Output file (if any)
        if os.path.exists("Output.txt"):
            os.remove("Output.txt")
        else:
            print("The file does not exist")

        # Enter a line in the outout file- Valid Usernames
        output = open("Output.txt", "w")    
        output.write("Valid Usernames-->\n\n")

        # Close the output file
        output.close()

        # Open input file containing 1 username in a line
        input = open("Input.txt")

        # Call signup function for each line(username)
        for each_username in input:
            
            # Call signup method
            self.signup(each_username)
        
        # Close the input file
        input.close()

        # Close chrome using chromedriver
        self.driver.quit()


    
    def signup(self, username):
        
        #____________________________________________ For other purpose _____________________________________
        # Finding the email box and entering email
        # enter_email = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'emailOrPhone')))
        # enter_email.send_keys('someuniqueemailaddress@gmail.com')

        # finding the username box and inserting the username in it
        # alternate-> self.driver.find_element_by_name('username').send_keys(self.username)
        #_____________________________________________________________________________________________________

        # Find username box
        # Click on it
        # Select text present in it
        # Delete the text
        # Enter the username
        enter_username = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.click()
        enter_username.send_keys(Keys.CONTROL, "a+")
        enter_username.send_keys(Keys.DELETE)
        enter_username.send_keys(username)

        # Find Email box and click on it
        clk_pass = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'emailOrPhone')))
        clk_pass.click()
 
        # Open output file in append mode
        output = open("Output.txt", "a")    

        # Wait for the icon to appear
        time.sleep(3)

        # Find the tick icon (if username available)
        try:
            self.driver.find_element_by_class_name('coreSpriteInputAccepted')
            # Save the available username in the output file
            output.write(username)
            print('pass')
        except NoSuchElementException:
            print('failed')

        # Close output file
        output.close()


# Driver    
if __name__ == '__main__':

    # Made by Abhishek Bharti
    # Follow me on github - https://github.com/ab28dev

    # Creating Object of the class
    ig_bot = InstagramBot()

#________________________________________________ Program Ends Here __________________________________________
#_____________________________________________________________________________________________________________