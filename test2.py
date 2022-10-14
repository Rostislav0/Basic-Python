from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://www.bershka.com/by/%D0%BC%D1%83%D0%B6%D1%87%D0%B8%D0%BD%D1%8B/%D0%BE%D0%B1%D1%83%D0%B2%D1%8C-c1010193202.html?discount=1'


def get_sales(structure):
    # with open("123.html", "w", encoding='utf-8') as file:
    #     file.write(driver.page_source)
    soup = BeautifulSoup(structure, 'lxml')
    items = soup.find_all('div', class_='category-product-card')

    sales = []
    for item in items:
        if item.find('img', class_='image-item'):
            sales.append({
            # 'name': item.find('div', class_='product-text product-text__without-label').get_text(),
            # 'price': ''.join(item.find('span', class_='current-price-elem red-price').get_text().split())
            # 'div', class_='product-text product-text__without-label'
                item.find('img', class_='image-item').get('alt'): [
                    'https://www.bershka.com' + item.find('a', class_='grid-card-link').get('href'),
                    ''.join(item.find('span', class_='current-price-elem red-price').get_text().split()[0])
                ]
            })
    return print(sales)


def get_source_html(url):
    driver = webdriver.Chrome()

    driver.get(url=url)
    time.sleep(0.2)
    SCROLL_PAUSE_TIME = 0.2

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(0.2)
    return get_sales(driver.page_source)


def main():
    get_source_html(url)


if __name__ == '__main__':
    main()