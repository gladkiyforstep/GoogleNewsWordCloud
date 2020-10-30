import wordcloud
from businessHelper import BusinessHelper

class WordCloudHelper(BusinessHelper):


    def generate_WordCloud(self,file_name = 'WordCloud'):
        txt = self.get_last_month_news()
        w = wordcloud.WordCloud(width=1000, font_path="msyh.ttc", height=700)
        w.max_words = 50
        w.generate(txt)
        w.to_file(f'{file_name}.png')



