from PreProcess.WordsProcessor import WordsProcessor
from PreProcess.StopWords import StopWords
from InputString import InputString
from Crawler.CrawlerUtil import CrawlerUtil

if __name__ == "__main__":

    text = InputString() # 데이터 입력
    cr = CrawlerUtil()
    cr.getText(text.getText())
    contentsArr = cr.make_list()
    st = StopWords()
    stopWordsArr = st.load_stopWordsDic()
    wp = WordsProcessor()
    result1 = wp.delete_stopWords(contentsArr, stopWordsArr)
    wp.index_frequency(result1)
    print('프로그램을 종료합니다.')

