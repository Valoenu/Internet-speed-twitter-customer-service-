# Internet-speed-twitter-customer-service-


from selenium import webdriver
from selenium.common.by import By
from selenium.common.Keys import Keys
from selenium.common.exceptions import NoSichElementException, ElementClickInterceptedException
from time import sleep

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_experimental_option("detach", true). / In case / Additional data


# Your twitter data here
TWITTER_EMAIL = 'Twitter Email Here'
TWITTER_PASSWORD = 'Twitter Password Here'

# Internet Service Provider (ISP)'s Example:
# Speed, 150Mbps download
# 10Mbps upload.
DOWNLOAD_PROMISED = 150
UPLOAD_PROMISED = 10

# DRIVER_PATH something like "/Users/Name/.../chromedriver"


# Creating a class / it will be easier later + better organised

class InternetSpeedTwitter:
  def __init__(self, driver_path):
    self.driver = webdriver.Chrome()
    self.upload = 0
    self.download = 0

    
    # Get internet speed data
  def internet_speed(self):
      # Web access link / speed test web
      self. driver.get("https://www.speedtest.net")

      time.sleep(2)

      # Create start/go button (SpeedTest)
      start_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
      start_button.click()


      # Wait 2-3 minutes for Internet speed results / It's depends on your device
      time.sleep(120)

      self.upload = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    
      self.download = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    
    # Tweet post
    def tweet_post(self):
      self.driver.get("https://twitter.com/login")
      time.sleep(5)

        # Data process
      email_field = driver_find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
      email_field.send_Keys(TWITTER_EMAIL)

      password_field = driver_find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
      password_field.send_Keys(TWITTER_PASSWORD)
      password_field.send_Keys(Keys.ENTER)

      time.sleep(5)
      
      tweet_structure = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
      
      message = f"Hey ISP, why is my internet {self.download}down/{self.upload}up when I pay for {DOWNLOAD_PROMISED}down/{UPLOAD_PROMISED}up?"
      tweet.structure.send_Keys(message)
      time.sleep(5)

      # Sending Tweet
      send_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
      send_button.click()
      
      time.sleep(5)
      self.driver.quit()


      

      

# Create our bot (Object)
object = InternetSpeedTwitter()
object.internet_speed()
object.tweet_post()
