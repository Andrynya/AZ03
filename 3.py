import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import matplotlib.pyplot as plt

# Открываем браузер
driver = webdriver.Chrome()

# Переходим на сайт
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)
time.sleep(5)

# Находим все элементы с ценами
divany = driver.find_elements(By.CLASS_NAME, 'lsooF')

parsed_data = []

for divan in divany:
    try:
        price = divan.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
    except:
        print(f"Произошла ошибка")
        continue

    parsed_data.append([price])

# Закрываем браузер
driver.quit()

# Создаем csv файл для записи
with open("prices.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Price"])
    writer.writerows(parsed_data)

# Определяем среднюю цену
prices = [float(item[0]) for item in parsed_data]
average_price = sum(prices) / len(prices)
print(f"Средняя цена на диваны: {average_price}")

# Строим гистограмму цен
plt.hist(prices, bins=20)
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.title('Гистограмма цен на диваны')
plt.show()