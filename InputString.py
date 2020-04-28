class InputString:

    text = ''

    def __init__(self):
        self.inputWords()

    def inputWords(self):
        print('-'*50)
        self.text = input("네이버 뉴스의 URL을 입력하여주세요. (ex. https://news.naver.com/main"
                          "/read.nhn?mode=LSD&mid=shm&sid1=102&oid=025&aid=0002996696)\n\n 입력 : ")
        print('-' * 50)
        print('\n')
        self.judgeWordsAtt()

    def judgeWordsAtt(self):
        if self.text[:22] == 'https://news.naver.com':
            print("URL이 입력되었습니다.\n")
            print('-' * 50)
            print('\n')

        else:
            print("Naver 뉴스의 URL이 아닙니다. 다시 입력하여 주세요.\n")
            print('-' * 50)
            print('\n')
            self.text = ''
            self.inputWords()

    def getText(self):
        return self.text

