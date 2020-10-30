from WordCloudHelper import WordCloudHelper

if __name__ == "__main__":
    news_word_cloud = WordCloudHelper(query='Russia', lang='en', country='US')
    news_word_cloud.generate_WordCloud('RussiaNewsCloud')
