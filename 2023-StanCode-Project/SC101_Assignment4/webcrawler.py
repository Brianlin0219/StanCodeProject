"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        datas = soup.tbody.find_all('tr')
        m_number_sum = 0
        fm_number_sum = 0
        for data in datas[:-1]:
            m_number = data.find_all('td')[2].text
            fm_number = data.find_all('td')[4].text
            m_number_adj = int(m_number.replace(',', ''))
            fm_number_adj = int(fm_number.replace(',', ''))
            m_number_sum += int(m_number_adj)
            fm_number_sum += int(fm_number_adj)
        print(f"Male Number:{m_number_sum}")
        print(f"Female Number:{fm_number_sum}")


if __name__ == '__main__':
    main()
