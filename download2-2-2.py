# wrap line up, go to config and type softWarp: true
  # editor:
  #   fontSize: 23
  #   tabLength: 4
  #   softWrap: true

# 한글 출력 ###########################################################
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
######################################################################

# 웹에서 이미지 다운 로드

import urllib.request as dw     # alias dw

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAyMDRfMzUg%2FMDAxNjEyNDExNzY4ODU3.2llTMPooIVZ6splbaqiLCqu-Dnx0169btlbceB7FDq8g.ocvc7xVALon5Pu6T1pdPcH_AMUq3X0ylVqkK1BREBRkg.JPEG.makeup446%2F2%25A3%25DFjaemyung%25A3%25DF20210203%25A3%25DF164339.jpg&type=sc960_832"

htmlURL = "https://www.google.com"

savePath1 = "D:/temp_/test1.jpg"
savePath2 = "D:/temp_/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

# old style은 다음과 같다. 지금은 아래의 with문을 쓴다.
saveFile1 = open(savePath1, 'wb')   # w: write, r: read, a: add, wb: write binary
saveFile1.write(f)                  # saveFile1.write(f.read)도 된다.
saveFile1.close()                   # 리소스를 반납한다.

# 위 세 줄을 다음과 같이 with문으로 쓸 수 있다.
with open(savePath2, 'wb') as saveFile2:    # <- 이걸 사용하는 것이 좋다.
    saveFile2.write(f2)

print('download completed')

# 차이점 ################################################################
# urlretrieve:
#     다이렉트로 저장한다.
#     저장 > open('r') > 변수에 할당 > 파싱 > 저장
#     파싱이 필요 없는 데이터(엑셀, 공공기관 문서)는 반복문으로 사용하기 편리.
#
# urlopen:
#     메모리 변수에 할당한다.
#     저장하기 전에
#     변수 할당 > 파싱 > 저장(db...)
#     중간 작업(분석, 분류)가 필요할 때 사용.

# 배운 내용 ############################################################
# urlretrieve
# rulopen
# urlretrieve vs. rulopen
# open, write, close
# with
