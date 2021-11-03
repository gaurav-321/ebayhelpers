import os
import re
import threading
import time
from bs4 import BeautifulSoup
from tabulate import tabulate
from datetime import timedelta
import undetected_chromedriver as uc
from colorama import init, Fore

init()
red, green, blue = Fore.RED, Fore.GREEN, Fore.BLUE
main_url = "https://www.ebay.de/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=hello&_sacat=0"
MAX_PRICE = 200
MIN_PRICE = 100


class Query:
    def __init__(self):
        self.searches = []
        self.running = False

    def add(self, q):
        self.searches.append([q, []])

    def remove(self, q):
        if q in self.searches:
            self.searches.remove(q)

    def find_products(self):
        if len(self.searches) > 0:
            options = uc.ChromeOptions()
            options.headless = True
            browser = uc.Chrome(options=options)
            browser.minimize_window()

            for index, query in enumerate(self.searches):
                total_data = []
                for i in range(1, 10):
                    url = re.sub("(?<=&_nkw=)[a-zA-Z+]*(?=&)", query[0].replace(" ", "+"),
                                 main_url) + "&_pgn=" + str(i)
                    browser.get(url)
                    products_list = get_all_product(browser)
                    for products in products_list:
                        if products[0] not in [x[0] for x in total_data]:
                            total_data.append(products)
                total_data.sort(key=sorting_func_time)
                self.searches[index][1] = total_data
            for x in self.searches:
                print(x)

            browser.quit()


def clear():
    os.system('cls') if os.name == 'nt' else os.system("clear")


def change_time(string):
    date = re.findall("(?<=Noch )[0-9 ]*(?=T)", string)[:1]
    hour = re.findall("(?<= )[0-9]*(?=[ ]*Std)", string)[:1]
    minute = re.findall("(?<= )[0-9]*(?=[ ]*Min)", string)[:1]
    if not date:
        date = [0]
    if not hour:
        hour = [0]
    if not minute:
        minute = [0]

    time_c = timedelta(days=int(date[0]), hours=int(hour[0]), minutes=int(minute[0]))
    return time_c


def get_all_product(browser):
    soup = BeautifulSoup(browser.page_source, "html.parser")
    products = soup.find_all("div", {'class': 's-item__wrapper clearfix'})
    final_data = []
    for product in products:
        title = product.find("h3", {'class': 's-item__title'})
        sub_title = product.find("div", {'class': 's-item__subtitle'})
        reviews = product.find("div", {'class': 's-item__reviews'})
        current_price = product.find("span", {'class': 's-item__price'})
        time_remaining = product.find("span", {'class': 's-item__time-left'})
        img = product.find("img", {'class': 's-item__image-img'}, src=True)
        data = [img['src']] if img else [""]
        data.append(product.find("a", {'class': 's-item__link'})['href'])
        for x in [title, sub_title, current_price, time_remaining]:
            if x:
                dat = x.text.replace("EUR ", "").replace(",", ".")
                data.append(dat)
            else:
                data.append("")

        if time_remaining:
            final_data.append(data)
    return final_data


def search(queries, page=10):
    total_data = []
    for query in queries:
        for i in range(1, page):
            url = re.sub("(?<=&_nkw=)[a-zA-Z+]*(?=&)", query.replace(" ", "+"), main_url) + "&_pgn=" + str(i)
            browser.get(url)
            products_list = get_all_product()
            for products in products_list:
                if products[0] not in [x[0] for x in total_data]:
                    total_data.append(products)
    total_data.sort(key=sorting_func_time)
    print(blue + tabulate(total_data))


def sorting_func_price(element):
    return float(element[-2])


def sorting_func_time(element):
    return change_time(element[-1])


def main():
    query = Query()
    query.add("oculus quest")
    query.add("oculus quest 2")
    query.find_products()


query_obj = Query()
