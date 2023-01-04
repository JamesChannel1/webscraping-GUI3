import tkinter
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path='C:\Program Files (x86)\chromedriver.exe')
driver = webdriver.Chrome(service=service)

main = tkinter.Tk()
main.geometry("300x300")
main.title("webscraping tool")

l = tkinter.Label(main, text="webscrape:")
l.pack()
entry = tkinter.Entry(width=50)
entry.pack()


def fun1a():
    url = entry.get()
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    driver.get(url)
    time.sleep(5)
    text_variable = soup.get_text()
    time.sleep(0.5)
    root = tkinter.Tk()
    root.title("text window")
    root.geometry("1600x768")
    text1 = tkinter.Text(root, height=100, width=400)
    text1.insert(tkinter.INSERT, text_variable)
    text1.pack()


def fun3a():
    fun1a()

b2 = tkinter.Button(main, text="click", command=fun3a)
b2.pack()

main.mainloop()