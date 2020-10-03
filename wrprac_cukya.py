from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ""
with open ("KakaoTalk_cukya.csv", "r", encoding ="utf-8") as f:
    lines = f.readlines()
    for line in lines[4:]:
        if',' in line :
            text += line
print(text)

wc = WordCloud(font_path="/System/Library/Fonts/Supplemental/AppleGothic.ttf", background_color="white", width=600, height=400)
wc.generate(text)
# wc.to_file("result.png")

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path="/System/Library/Fonts/Supplemental/AppleGothic.ttf", background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked2.png")