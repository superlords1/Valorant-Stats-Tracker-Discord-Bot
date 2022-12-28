from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import discord
from discord import app_commands
from discord.ext import commands
import time
from utils import get_url
import os

def getCompData(url, username_tag):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url)
        
    try:
        rank = driver.find_element(By.CLASS_NAME, "stat__value")
        stats = driver.find_elements(By.CLASS_NAME, "numbers")
        embedvar = discord.Embed(title = f"Stats for: {username_tag[0]}#{username_tag[1]}")
        embedvar.add_field(name = "Rank", value = str(rank.text))
        list = ["Damage/Round","K/D Ratio", "Headshot%", "Win %"]
        for stat in stats:
            name = stat.find_element(By.CLASS_NAME, "name")
            title = name.get_attribute("title")
            if title in list:
                value = stat.find_element(By.CLASS_NAME, "value")
                embedvar.add_field(name = title, value = str(value.text), inline = False)
        return embedvar
    except Exception as e:
        print(e)
        return discord.Embed(title = "User not found")
    #driver.close()

