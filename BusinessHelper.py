import calendar
import datetime
import nltk
import re
from bs4 import BeautifulSoup
from WebHelper import GoogleNews


def plus_month(date):
    days_in_month = calendar.monthrange(date.year, date.month)[1]
    date += datetime.timedelta(days=days_in_month)
    return date


class BusinessHelper(GoogleNews):

    def get_public_time(self):
        time_list = self.soup.findAll('time', class_='WW6dff uQIVzc Sksgp')
        date_format = "%Y-%m-%dT%H:%M:%SZ"
        result_list = []
        for s in time_list:
            date = s['datetime']
            formated_date = datetime.datetime.strptime(date, date_format)
            result_list.append(formated_date)

        return result_list

    def get_text_of_news(self):
        name_list = self.soup.findAll('a', class_='DY5T1d')
        text_name_list = []
        for n in name_list:
            text_name_list.append(n.text)
        return text_name_list

    def get_last_month_news(self):
        news = self.get_text_of_news()
        dates = self.get_public_time()
        result = ''
        for i in range(0, len(news)):
            post_date_plus_month = plus_month(dates[i])
            if post_date_plus_month > datetime.datetime.now():
                result += news[i]

        return result

    def str_To_OnlyCoolWordsList(self, txt="Russia policy, after. the US election ways"):
        txt1 = re.sub(r'[^\w\s\']', '', txt)
        txt1 = txt1.split()
        tagged = nltk.pos_tag(txt1)
        result = [word for word, tag in tagged if tag.find('N') == 0]
        return result

    def most_popular50(self):
        txt = self.get_last_month_news()
        txt1 = self.str_To_OnlyCoolWordsList(txt)

        lst = [[0, 'word']]

        for word in txt1:
            exist = False
            for p in lst:
                if word == p[1]:
                    p[0] += 1
                    exist = True
            if not exist:
                lst.append([1, word])

        lst.sort(reverse=True)
        most_popular = lst[0:50]
        return most_popular
