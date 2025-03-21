import gym
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import hashlib
import time

class AmazonTestingEnv(gym.Env):
    def __init__(self):
        # Set up Selenium WebDriver
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=chrome_options)
        
        # Track visited pages
        self.visited_pages = set()
        self.current_step = 0
        self.max_steps = 20
        
        # Define action and observation spaces
        self.action_space = gym.spaces.Discrete(4)  # 4 actions
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(100,))
        
        # Initialize TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(max_features=100)

    def _get_state(self):
        # Extract page content and convert to TF-IDF vector
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        text = soup.get_text()
        return self.vectorizer.fit_transform([text]).toarray()[0]

    def _calculate_reward(self):
        # Reward for unique pages and penalize repeats
        page_hash = hashlib.sha256(self.driver.page_source.encode()).hexdigest()
        if page_hash in self.visited_pages:
            return -1
        else:
            self.visited_pages.add(page_hash)
            return 2

    def step(self, action):
        reward = 0
        done = False
        
        try:
            if action == 0:  # Search for a product
                search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
                search_box.send_keys("laptop")
                self.driver.find_element(By.ID, "nav-search-submit-button").click()
                reward += 1
                
            elif action == 1:  # Click on a product
                products = self.driver.find_elements(By.CSS_SELECTOR, ".s-result-item [data-asin]")
                if products:
                    products[0].click()
                    reward += 1.5
                    
            elif action == 2:  # Add to cart
                addtocarts = self.driver.find_elements(By.XPATH, "//input[@id='add-to-cart-button']")
                if addtocarts:
                    addtocarts[1].click()
                    reward += 3
                
            elif action == 3:  # Navigate to deals
                self.driver.find_element(By.LINK_TEXT, "Today's Deals").click()
                reward += 1
                
            time.sleep(2)  # Allow page load
            reward += self._calculate_reward()
            
        except Exception as e:
            reward -= 2  # Penalize failed actions
            print(f"Action failed: {str(e)}")

        self.current_step += 1
        if self.current_step >= self.max_steps:
            done = True

        return self._get_state(), reward, done, {}

    def reset(self):
        self.driver.get("https://www.amazon.in")
        self.current_step = 0
        self.visited_pages.clear()
        time.sleep(2)
        return self._get_state()

    def close(self):
        self.driver.quit()