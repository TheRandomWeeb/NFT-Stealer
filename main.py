from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# driver = webdriver.Firefox(executable_path="./geckodriver")

driver = webdriver.Chrome(executable_path="./chromedriver")

def SelectNfts():
    driver.get("https://opensea.io/collection/boredapeyachtclub")
    nft = driver.find_element(By.XPATH, "//div[@role='grid']")
    source = nft.get_attribute("innerHTML")
    
    with open("test.html", "w") as f:
        f.write(source)


def GetImage():
    img = driver.find_element(By.CLASS_NAME, "Image--image")
    print(img.get_attribute("src"))

SelectNfts()
# GetImage()
