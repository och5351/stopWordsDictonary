from bs4 import BeautifulSoup
import urllib.request
import sys

class CrawlerUtil:

    text = ''

    def getText(self, URL):
        print('URL을 분석합니다.')
        source_code_from_URL = urllib.request.urlopen(URL)
        soup = BeautifulSoup(source_code_from_URL, 'html.parser', from_encoding='utf-8')
        print('뉴스를 가져옵니다.')

        for htmlText in soup.select('#articleBodyContents'):
            self.text = htmlText.text
        if self.text != '':
            print('뉴스를 성공적으로 가져왔습니다.')
            print('받아온 뉴스를 보기 쉽게 가공합니다.')
            self.text = self.text.replace('\n','')
            self.text = self.text[61:len(self.text) - 100] # 최대한 내용만 받아 오기
            print('\n다음은 받아 온 뉴스입니다.\n'+self.text+'\n')
            self.make_list()
        else:
            print('-' * 50)
            print('\n뉴스 가져오기를 실패하였습니다.')
            print('URL을 다시 한번 확인하여주세요.\n')
            print('-' * 50)
            print('프로그램을 종료합니다.')
            sys.exit(1)

    def make_list(self):
        print('가공한 뉴스를 단어 단위로 배열화 합니다.')
        temp = self.text.split()
        print('배열화를 성공하였습니다.')
        return temp

