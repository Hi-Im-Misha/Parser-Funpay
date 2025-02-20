import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://funpay.com/chips/51/" # put a link


file_path = r"Git_project\parser-funpay\result.txt"
driver_path = r"Git_project\parser-funpay\chromedriver.exe"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2526 Yowser/2.5 Safari/537.36")
# chrome_options.add_argument("--headless") # interface visibility
chrome_options.add_argument("--disable-blink-features=AutomationControlled")


service = webdriver.chrome.service.Service(driver_path)
service.start()
driver = webdriver.Remote(service.service_url, options=chrome_options)


driver.get(url)
with open(file_path, "w", encoding="utf-8") as file:
    while True:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            button = driver.find_element(By.CSS_SELECTOR, "button.lazyload-more")

            if button.is_displayed():
                button.click()
                time.sleep(1)

            else:
                break 

        except Exception as e:
            print("Error:", e)
            break


    elements = driver.find_elements(By.CSS_SELECTOR, "a.tc-item")
    for idx, element in enumerate(elements, start=1):
        # Link
        link = element.get_attribute("href")

        # Server
        server_element = element.find_element(By.CSS_SELECTOR, "div.tc-server")
        server_name = server_element.text

        # Availability
        amount_element = element.find_element(By.CSS_SELECTOR, "div.tc-amount")
        amount_text = amount_element.text

        # Price
        price_element = element.find_element(By.CSS_SELECTOR, "div.tc-price")
        price_text = price_element.text.strip()


        result_str = f"Ссылка {idx}: {link}, Сервер: {server_name}, Наличие: {amount_text}, Цена: {price_text}"
        file.write(result_str + "\n")


driver.quit()
