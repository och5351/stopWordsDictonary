class StopWords:
    def __init__(self):
        print("불용어 처리를 준비 합니다.")

    # 불용어 사전 업로드
    def load_stopWordsDic(self):
        print("불용어 사전을 로드합니다.")
        f = open('stopwordsKorean.txt',
                 'r', -1, "utf-8")
        data = f.readlines()
        f.close()
        data = [x.replace("\n", "") for x in data]
        print("불용어 사전 로드를 성공하였습니다.")
        print("\n불용어 사전은 다음과 같습니다.\n")
        print(data)
        print('\n')
        return data

