import requests
from bs4 import BeautifulSoup

url = "https://funpay.com/chips/51/" # put a link
file_path = r'Test_project\github\parser_funpay_soup\result.txt' # put a path


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2526 Yowser/2.5 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")

elements = soup.select("a.tc-item")[:5] # Ограничиваем количество элементов до 5


# Открываем файл для записи
with open(file_path, "w", encoding="utf-8") as file:
    for idx, element in enumerate(elements, start=1):
        try:
            # Link
            link = element.get("href")
            print(f"Link: {link}")
            
            # Server
            server_element = element.select_one("div.tc-server")
            server_name = server_element.get_text(strip=True) if server_element else "N/A"
            print(f"Server: {server_name}")

            # User
            user_element = element.select_one("div.media-user-name")
            user_name = user_element.get_text(strip=True) if user_element else "N/A"
            print(f"User: {user_name}")

            # User Reviews
            reviews_element = element.select_one("span.rating-mini-count")
            user_reviews = reviews_element.get_text(strip=True) if reviews_element else "N/A"
            print(f"User Reviews: {user_reviews}")

            # User Info
            user_info_element = element.select_one("div.media-user-info")
            user_info = user_info_element.get_text(strip=True) if user_info_element else "N/A"
            print(f"User Info: {user_info}")

            # Availability
            amount_element = element.select_one("div.tc-amount")
            amount_text = amount_element.get_text(strip=True) if amount_element else "N/A"
            print(f"Availability: {amount_text}")

            # Price
            price_element = element.select_one("div.tc-price")
            price_text = price_element.get_text(strip=True) if price_element else "N/A"
            print(f"Price: {price_text}")

            # Записываем результат в файл
            result_str = (
                f"Link {idx}: {link}\n"
                f"Server: {server_name}\n"
                f"Price: {price_text}\n\n"
                f"Availability: {amount_text}\n"
                f"User Name: {user_name}\n"
                f"User Reviews: {user_reviews}\n"
                f"User Info: {user_info}\n"
            )
            file.write(result_str)

        except Exception as e:
            print(f"Error processing element {idx}: {e}")

print("Парсинг завершен!")
