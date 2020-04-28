class WordsProcessor:
    def __init__(self):
        print("불용어 처리가 준비되었습니다.")

    def delete_stopWords(self, contentsArr, stopWordsArr):
        print("불용어를 제거합니다.")

        for contentsNum in range(len(contentsArr)):
            for stopW in stopWordsArr:
                if stopW in contentsArr[contentsNum]:
                    contentsArr[contentsNum] = contentsArr[contentsNum].replace(stopW, '')
        print('불용어를 제거하였습니다.')
        print('\n 불용어가 처리된 내용입니다.')
        print(contentsArr)
        return contentsArr

    def index_frequency(self, contentsArr):
        print('색인어들의 빈도수를 조사합니다.')
        resultDic = {}
        for word in contentsArr:
            resultDic[word] = resultDic.get(word, 0) + 1
        print('\n다음은 색인어들의 빈도수 입니다.\n')
        print('색인어\t\t\t\t\t\t\t\t빈도수')
        print('-' * 50)
        for key in resultDic.keys():
            print(key + '\t\t\t\t\t\t\t\t' + str(resultDic[key]))

