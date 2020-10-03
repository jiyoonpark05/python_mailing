# #openpyxl 사용 방법
#
# from openpyxl import Workbook
#
# wb = Workbook()
# ws1 = wb.active
# ws1.title = "articles"
# ws1.append(["제목", "링크", "신문사"])
#
# wb.save(filename='articles.xlsx')

import matplotlib.font_manager as fm

# 이용 가능한 폰트 중 '고딕'만 선별
for font in fm.fontManager.ttflist:
    if 'Gothic' in font.name:
        print(font.name, font.fname)