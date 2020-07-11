from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver

ques = []

r = requests.get('https://simpleprogrammer.com/programming-interview-questions/')
c = r.content
soup = BeautifulSoup(c)
main_content = soup.find('div', attrs = {'class': 'awr'})


for i in main_content.find_all("li"):
    ques.append(i.text)

file = pd.DataFrame(ques, columns = ['question1'])
file.to_csv("dataset.csv")

