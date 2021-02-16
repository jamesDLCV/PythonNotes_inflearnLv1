# chapter03-2
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
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Strrt!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String, 이스케이프와 반대
raw_s1 = r'D:\python\test'         # 드라이브 경로를 가지고 온다.
raw_s2 = r'D:\tpython\test'        # tap \t가 작동하지 않는다.
                                   # 있는 그대로 raw string으로 출력한다.
                                   # 역슬러시를 그대로 출력할 수 있다.
                                   # 소문자 r이 붙어 있으면 raw string이구나.
                                   # 역슬러시를 사용하지 않기 위해 사용했구나.
                                   # 이스케이프 문자를 사용하지 않기 위해
                                   # 변수를 선언했구나라고 이해하라.
print(raw_s1)
print(raw_s2)
