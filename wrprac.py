from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ""
with open ("KakaoTalk_CHEESYGANG.csv", "r", encoding ="utf-8") as f:
    lines = f.readlines()
    for line in lines[4:]:
        if',' in line :
            text += line.replace("지윤","").replace("고라니상","").replace("고잉섹시호","").replace("이세상힙스터","")\
                .replace("ㅋ","").replace("이모티콘","").replace("사진","").replace("동영상","").replace("그래서","").replace("나도","")\
                .replace("언니","").replace("내가","").replace("지금","").replace("오늘","").replace("했는데","").replace("나는","").replace("요즘","")\
                .replace("샵검색","").replace("내일","").replace("어제","").replace("시발","").replace("다희"," ").replace("근데","")\
                .replace("ㅅㅂ","").replace("이거","").replace("많이","").replace("이게","").replace("그냥","").replace("유진이","").replace("토미는","")\
                .replace("그냥","").replace("하는","").replace("그거","").replace("그런","").replace("하고","").replace("그래도","").replace("있고","")\
                .replace("같아","").replace("http","").replace("twitter","").replace("아직","").replace("같은","").replace("그래","").replace("하면","")\
                .replace("그러게","").replace("있는","").replace("저는","").replace("이렇게","").replace("그니까","").replace("그러면","").replace("여기","")\
                .replace("그럼","").replace("다들","").replace("저거","").replace("있어","").replace("원래","").replace("토미가","").replace("갑자기","")\
                .replace("너무","").replace("이런거","").replace("이제","").replace("때마다","").replace("사람이","").replace("거기","")\
                .replace("사람이","").replace("그건","").replace("하지만","").replace("어차피","").replace("아니","").replace("이미","").replace("계속","")\
                .replace("사람","").replace("status","").replace("벌써","").replace("것","").replace("그렇게","").replace("ㅇ","").replace("봤는데","")\
                .replace("있으면","").replace("전에","").replace("이도","").replace("있으면","").replace("얼마나","").replace("토미한테","").replace("해도","")\
                .replace("영상","").replace("그게","").replace("시팔","").replace("진짜","").replace("존나","").replace("다시","").replace("조금","").replace("사실","")\
                .replace("보고","").replace("일단","").replace("어디","").replace("무슨","").replace("2장","").replace("미친","")


print(text)

wc = WordCloud(font_path="/System/Library/Fonts/Supplemental/AppleGothic.ttf", background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path="/System/Library/Fonts/Supplemental/AppleGothic.ttf", background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")