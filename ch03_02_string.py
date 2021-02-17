# chapter02-1
# 파이썬 문자형
# 문자형 중요
# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 문자열 출력
print(type(str1), type(str2), type(str3), type(str4))
# 문자열 길이
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str() # str(object)를 호출한다, 빈 문자열 생성됨.
                # 형 변환할 때 int() 이렇게 했다. 이와 비슷.

print(type(str1_t1), len(str1_t1)) # <class 'str'> 0
print(type(str2_t2), len(str2_t2)) # <class 'str'> 0

# escape 문자 사용
# I'm a boy

print("I'm a boy")
print('I\'m a boy')
print('I\\m a boy')     # I\m a boy

print('a \t b')         # tab 간격
print('a \n b')         # 줄 바꿈, 엔터가 쳐진다.

print('a \"\" b')       # a "" b

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)                              # Do you have a "retro games"?
escape_str2 = 'What\'s on TV?'
print(escape_str2)                              # What's on TV?

# 탭, 줄 바꿈
t_s1 = "Click \t Strrt!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String, 이스케이프와 반대
raw_s1 = r'D:\python\test'         # 드라이브 경로를 가지고 올 수 있다.
raw_s2 = r'D:\tpython\test'        # tap \t가 작동하지 않는다.
                                   # 있는 그대로 raw string으로 출력한다.
                                   # 역슬래시를 그대로 출력할 수 있다.
                                   # 소문자 r이 붙어 있으면 raw string이구나.
                                   # 역슬래시를 사용하지 않기 위해 사용했구나.
                                   # 이스케이프 문자를 사용하지 않기 위해
                                   # 변수를 선언했구나라고 이해하라.
print(raw_s1)
print(raw_s2)

#----------------
# chapter02-1
# 멀티라인 입력
### 역슬래시가 나오면, 파이썬은
### 이 다음에 어떤 변수를 바인딩하는구나로 이해한다.
### 역슬래시를 사용하라 use a backslash.

multi_str = \
'''
스트링
멀리 라인
테스트
'''
print(multi_str)

multiLineTest = \
'this is also \
possible'                       # 이렇게 백슬래쉬를 쓴다. 이어진다는 표시

print(multiLineTest)            # this is also possible

multiLineTest2 = \
'this is also ' \
'possible' \

print(multiLineTest2)           # this is also possible

# 문자열 연산
## 곱하기와 더하기를 할 수 있다.
## 다른 문법에서는 보기 힘든 스킬이다.

str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul chuncheon"

print(str_o1 * 3)
print(str_o1 + str_o2)

print('y' in str_o1)            # is there 'y' in str_o1?
                                # True 출력. 1
                                # 파이썬에서는 이렇게 문자가 들어오면 하나 하나를
                                # 리스트라고 보면 된다.

# ch03_01 데이터 자료형 때 시퀀스를 공부했다. 시퀀스닌 in 연산자를 사용할 수 있다.

print('z' in str_o1)            # false 출력. 0

print('P' not in str_o2)        # True 출력. 대문자 P가 없으므로 True 출력.
                                # not in? 없느냐고 물어봤으므로 True 출력.
                                # 파이썬은 대소문자를 구분한다.
print('P' in str_o2)            # not이 없으면, False 출력.
                                # 있느냐고 물으면 False, 없느냐고 물으면 True.
                                # 이렇게 in 연산자를 스트링해서 쓸 수 있다.

# 어플리케이션을 활용한 데이터 분석 때 아주 많이 사용되므로 문자열 연산은 숙지하라.
print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('P' not in str_o2)
print('P' in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))   # 66 <class 'str'>, 숫자처럼 보이지만 str이다.
                                # 문자 66을 의미한다. 숫자가 아니다.
print(str(10.1))                # 당연히 문자 10.1이다.
print(str(True), type(str(True))) # True <class 'str'>, 문자열이다.
# 눈에 보이는 건 True지만 파이썬이 이해하고 있는 True, False는 boolean 형이 아니라
# True 문자로 인식하고 있다.
print(str(complex(12)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha, .....)
## 너무 많아서 외워도 헤깔리게 된다.
## 필요할 때 구글링을 해서 찾아서 사용하게 된다.

str_o5 = "banana"
print("capitalize: ", str_o5.capitalize())  # capitalize() 이렇게 해서 호출한다.
                                            # capitalize:  Banana
                                            # 첫 번째 글자가 대문자로 바뀐다.
# 따라서 capitalize() 함수는 첫 번째 시작 글자를 대문자로 바꿔준다.

print("endswith?: ", str_o5.endswith("s"))  # endswith?:  False
                                            # 끝글자가 s로 끝나는가?
print("endswith?: ", str_o5.endswith("a"))  # endswith?:  True
# 마지막 문자가 무엇인지 체클할 때 사용하는 함수이다.
# 모든 문단의 끝에는 뭔가를 붙어야 하는데 그게 돼 있는지 확인할 수 있다.

print("replace: ", str_o5.replace("nana", "Good"))  # replace:  baGood
print("replace: ", str_o5.replace("py", "Good"))    # replace:  banana
print("replace: ", str_o5.replace("nana", " Good")) # replace:  ba Good
# 띄어쓰기도 포함한다. 이 부분을 찾아서 이걸로 바꿔줘. 많이 쓰는 함수이다.

print("sorted: ", sorted(str_o5))   # sorted:  ['a', 'a', 'a', 'b', 'n', 'n']
# 리스트 형태로 반환한다. 순서가 정렬이 돼서 나왔다.
# 문자열을 받아서 어떤 기준에 맞게 정렬해서 리스트 형태로 반환한다는 것을 기억하라.
# 왜 이렇게 나오는지는 공부를 좀 더 해야 할 수 있다. 나중에 배우게 된다.

# 공백으로 돼 있는 것에, 쓰기 좋은 함수가 있다.
## split이다. split도 많이 쓴다.
## 특정 단어를 분리할 때, 단어 단위나, 문장 단위로 분리할  많이 쓴다.
str_o9 = "You are my sunshine."
print("split: ", str_o9.split(' '))     # split의 기준은 공백이다.
                                        # 각각의 단어를 리스트로 만들어준다.
str_o10 = "You!are!my!sunshine."
print("split: ", str_o10.split('!'))     # split의 기준은 !이다.

# 문자열 함수 정리 ####################################

str_o6 = "pineapple"
str_o7 = "strawberry"
str_o8 = "I am a boy"
print("Capitalize: ", str_o6.capitalize())
print("endswith?: ", str_o6.endswith("s"))
print("join str: ", str_o6.join(["I'm ", "!"]))
print("replace1: ", str_o7.replace('berry', ' Good'))
print("replace2: ", str_o7.replace("are", "was"))
print("split: ", str_o8.split(' '))                     # Type 확인
print("split type: ", type(str_o8.split(' ')))
print("sorted: ", sorted(str_o8))
print("reversed1: ", reversed(str_o6))                  # reverse=True

print("reversed2: ", list(reversed(str_o7)))            #list 형 변환

# Capitalize:  Pineapple        # 맨앞 글자를 대문자로 바꿔라.
# endswith?:  False             # s로 끝나는가? False.
# join str:  I'm pineapple!     # 앞에 I'm을 뒤에는 !를 붙인다.
# replace1:  straw Good
# replace2:  strawberry         # replace할 글자가 존재하지 않으면 안 한다.
# split:  ['I', 'am', 'a', 'boy']
# split type:  <class 'list'>
# sorted:  [' ', ' ', ' ', 'I', 'a', 'a', 'b', 'm', 'o', 'y']
    # 공백도 문자로 처리한다.
# reversed1:  <reversed object at 0x00000134B04DA5C8>
# reversed2:  ['y', 'r', 'r', 'e', 'b', 'w', 'a', 'r', 't', 's']

# 반복(시퀀스)

im_str = "Good Boy!"

print(dir(im_str))      # dir로 im_str에서 가능한 것들을 찾아보자.
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# 위 출력 결과는 초보에서는 몰라도 된다. class를 배워야 이해할 수 있다.
# im_str 변수에서 사용할 수 있는 모든 것들을 나열한다.
# '__iter__' 만 보자. im_str에 이것이 있다는 것을 반복을 사용할 수 있다는 의미다.

# 출력
for i in im_str:
    print(i)
# 한 글자씩 가져와서 출력이 된다.
# 이런 문자열은 시퀀스 형이기 때문에, 슬라이싱 처리를 할 수 있다.
# slice 자르는 처리를 할 수 있다는 것이다.

# 기초 문법은 쉽지만 다뤄 봐야 한다.
# 많은 양을 쉬운 예제로 공부하는 것이 좋다.
# 문자열이라는 자료형에도 위에서와 같이 아주 많은 내용이 있다.
# 이렇게 많은 내용을 다 숙지해야 타인의 코드도 이해할 수 있고 잘 짤 수도 있다.

# 슬라이싱, 아주 중요하다.
str_sl = "Nice Python"

print(len(str_sl))          # 11개.

# 슬라이싱 연습
print(str_sl[0:3])          # Nic
                            # 개수가 아니다. index를 의미한다. 0, 1, 2 index
# str_sl에서 Python만 출력하고 싶다면 어떻게 하는가?
print(str_sl[5:])           # [5: 11]과 동일
print(str_sl[5:10])         # 맨 마지막 index 전까지만 출력.
print(str_sl[:])            # Nice Python
print(str_sl[:len(str_sl)]) # Nice Python, (str[:11])과 동일, 처음부터 10번까지
# 마직막 부분의 index를 모를 때는 생략을 하거나 len() 함수를 사용한다.
# 첫 부분도 생략할 수 있다.
print(str_sl[:len(str_sl) - 1]) # Nice Pytho, 맨 마지막 n이 빠졌다.
                                # [:10]과 동일
print(str_sl[1:4:2])            # 1부터 4-1까지 가지고 오는데 2칸씩 건너뛰어라.
                                # ie
print(str_sl[1:9:2])            # iePt, index1~index8까지 2칸씩 건너뛰면서 출력.
print(str_sl[1:10:2])           # idPto

# 마이너스도 쓸 수 있다.
str_sl1 = "good Python"
print(str_sl1[-5:])              # ython
print(str_sl1[-5:-2])            # yth, index-5, -4, -3까지 출력
                                 # index -2는 출력되지 않는다.
print(str_sl1[-5:-1])            # ytho, index -1은 출력되지 않는다.
print(str_sl1[-5:0])             # 아무 것도 출력되지 않는다.

print(str_sl1[1:-2])             # ood Pyth, index1부터 index-3까지 출력

print(str_sl1[::2])              # 두 칸씩 뛰면서 가져와라, 처음부터 끝까지
                                 # go yhn, index0 즉 첫 칸은 출력한다.
print(str_sl1[:-1])              # good Pytho
print(str_sl1[-1:])              # n
print(str_sl1[::-1])             # nohtyP doog, index-1부터 역순으로 출력한다.
# 음수는 오른쪽에서 왼쪽으로, -1부터 왼쪽으로.
# 양수는 왼쪽에서 오른쪽으로, 0부터 오른쪽으로.
# 긴 문자열을 가지고 오고, 원하는 단어만 슬라이싱해보다 보면 익힐 수가 있다.

# 아스키 코드 (또는 유니코드)
## 파이썬에서는 z를 표시하기 위해서는 아스키 코드표의 z에 해당하는 번호를 찾아서
## 갖고 와서 문자로 처리해서 우리한테 보여주는 것이다.
## 컴퓨터는 z과 같은 문자를 인식하는 게 아니다.
## 모든 프로그램 언어에서 유니코드나 아스키코드표를 보고 컴퓨터가 내부적으로 처리한다.

a = 'z'
print(ord(a))               # 아스키 코드로.
                            # 122, z에 해당하는 아스키 코드는 122다.
# 파이썬 인터프리터가 122를 보고 알파벳 z를 우리에게 표시해 주는 것이다.
print(chr(122))             # 문자로.
                            # z, 아스키코드를 알파벳으로 보여는 함수는 chr이다.
# 코드 값을 알기 위해서 ord나 char 같은 함수를 찾을 수도 있다.

# 문자형은 복습을 해 주기를 바란다.
# 인덱싱은 0부터 시작한다.
# 거꾸로 갈 때는 -1부터 시작한다.
# 리스트를 알아야 알고리즘 문제를 풀 수 있고 자료 구조까지 볼 수 있다.
