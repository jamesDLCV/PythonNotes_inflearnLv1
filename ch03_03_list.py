### ch03-3-1
# 파이썬 리스트
# 자료 구조에서 중요하다.
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)
# 버스에 줄을 선 것과 비슷. 먼저 서 있는 사람이 먼저 들어 간다.
# 중복도 허용한다. 똑같은 값을 여러 개 저장할 수 있다.
# 한 번 삽입을 하면 수정도 가능하다. 5를 넣었는데 7로 바꿀 수 있다.
# 마음에 안 드는, 혹은 필요 없는 데이터는 리스트 안에서 삭제할 수 있다.

# 리스트는 문자열과 마찬가지로 시쿼스 형이다.
# 순서가 존재한다.
# 여러 가지 데이터 타입을 담을 수 있다.
# 알고리즘을 풀기 위해서는 알고리즘 문제를 풀거나 데이터를 담을 때,
# 리스트가 필요하다. 다른 언어에서는 배열이라고 한다.
# 굉장히 중요한 자료 구조 중의 하나이다.
# 리스트를 잘 사용해야, 데이터베이스에서 값을 가져 오거나
# 웹과 인터넷에서 크롤링을 해서 데이터를 가져 올 수 있다.
# 대부분 리스트 형태로 담을 가능성이 크다.
# 데이터 분석에도 필수다. numpy, padas 등에서
# 2차원 3차원 이런 식으로 데이터를 리스트로 담고 있다.
# 그 안의 동작하는 메커니즘은 약간 다르더라도
# 어떤 데이터를 삽입하고 가져 오는 형태는 비슷하다.

### 리스트 사용법
# 1. 리스트 선언
# 2. 리스트 특징
# 3. 리스트 인덱싱 - 문자열의 인덱싱과 동일, string
# 4. 리스트 슬라이싱 - 문자열의 인덱싱과 동일, string
# 5. 리스트 함수
# 6. 리스트 삭제


### 선언
a = []  # 빈 리스트는 이렇게 대괄호로 선언한다.
print(type(a))  # <class 'list'>

b = list()  # 빈 리스트를 이렇게도 선언할 수 있다.

c = [70, 75, 80, 85]    # index 0, 1, 2, 3, 네 개의 원소를 가지고 있는
                        # 리스트를 선언했다.
print(len(c))           # 4
# string하고 별반 차이가 없다.
# string도 시퀀스 형이기 때문에, 문자열에서 사용하던 slicing이나 len을
# 사용할 수 있다.

# 서로 다른 자료형을 하나의 리스트 안에 담을 수가 있다.
d = [1000, 10000.0, 'Ace', 'Base', 'Captain']

# 리스트 안에 또 다른 리스트를 담을 수도 있다.
e = [1000, 10000.0, ['Ace', 'Base', 'Captain']]
# e의 첫 째 열은 int, 둘 째 혈은 double, 셋 째 열은 리스트이다.

#
f = [21.42, 'football', 3, 4, False, 3.141592]

### 인덱싱
# 내가 원하는 데이트를 꺼내오는 과정이라고 생각하면 된다.
d = [1000, 10000.0, 'Ace', 'Base', 'Captain']
e = [1000, 10000.0, ['Ace', 'Base', 'Captain']]

print('>>>>>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])     # 10000.0을 가지고 와라. index 1번을 가지고 와라.
                        # 인덱스 번호만 알면 된다.
sum = (d[0] + d[1] + d[1])
print('sum of int and float - ', sum, type(sum))

print('d - ', d[-1])        # Captain
print(type(e[1]))           # <class 'float'>
print('e - ', e[-1][1])     # Base, e[-1]은 리스트다.
                            # 그 리스트 안의 index 1은 Base다.
print(type(e[-1][1]))       # <class 'str'>
# 두 개 이상 중첩 된 리스트에 접근할 때는 첫 번째 리스트 안에서 그 리스트에 접근해서
# 그 리스트의 인덱스 번호를 입력해 줘야 값이 정확하게 출력된다.

print('e - ', list(e[-1][1]))   # 이것을 리스트로 만들 수 있다. 형 변환을 하면 된다.
                                # e -  ['B', 'a', 's', 'e']
# 문자열은 시퀀스라고 했다. 'Base' 4개의 문자를 index 0, index 1, index 2, index 3
# 이렇게 자기가 알아서 리스트 형태로 분해를 해서, 네 개의 데이터로 이루어진
# 리스트 형태로 변환을 했다. 많이 쓰이므로 잘 알아 둬라.
# b = list(), 이렇게 빈 리스트 선언할 때와 동일한 형태이다.
# 그 괄호 안에 값을 넣으니까 파이썬이 알아서 값을 출력해 줬다.

### 슬라이싱
d = [1000, 10000.0, 'Ace', 'Base', 'Captain']
e = [1000, 10000.0, ['Ace', 'Base', 'Captain']]

print('>>>>>>>>>>')
print('d - ', d[0:3])   # index 0, 1, 2까지 출력, d -  [1000, 10000.0, 'Ace']
print('d - ', d[2:])    # index 2부터 끝까지 출력, d -  ['Ace', 'Base', 'Captain']
print('e - ', e[2:])    # [['Ace', 'Base', 'Captain']]
print('e - ', e[-1][1:3])   # e의 index -1에서 index 1에서부터 2까지 출력
                            # (3-1)이니까 2까지 출력.
                            # ['Base', 'Captain']
                            # 리스트 자체를 슬라이싱해서 리스트를 가지고 왔다.
                            # 리스트를 슬라이싱하니까 리스트가 나온다.
print('e - ', type(e[-1][1:3]))     # e -  <class 'list'>,
                                    # type을 찍어 보면, 리스트가 나온다.

### 리스트 연산
# list + list = list, set + set = set
c = [70, 75, 80, 85]
d = [1000, 10000.0, 'Ace', 'Base', 'Captain']

print('>>>>>>>>>>')
print('c + d', c + d)    # 앞의 것 먼저 다 들어가고 뒤의 것이 삽입되는 방식.
# c + d [70, 75, 80, 85, 1000, 10000.0, 'Ace', 'Base', 'Captain']
# 총 9개의 elements가 된다.

print('c * 3', c * 3)   # c의 원소는 4개인데 곱하기 3을 했으므로 총 12개가 된다.
# c * 3 [70, 75, 80, 85, 70, 75, 80, 85, 70, 75, 80, 85]
# 순서는 유지하고 있다. c의 원소 순서로 3번 중첩된다.
# list * 3 = list
# 쉽게 이해하면 된다, 리스트로 연산하면 리스트가 결과로 나온다.

## print("'Test' + c[0]", 'Test' + c[0])
# TypeError: can only concatenate str (not "int") to str
# 문자 + 숫자 --> error
# 이런 문자 + 숫자는 어떻게 하는가?
print("'Test' + c[0]", 'Test' + str(c[0]))  # 'Test' + c[0] Test70
                        # 뒤에 있는 c[0]를 str로 형 변환을 해 주면 된다.
# 이러한 원리를 잘 파악해 둬라. 파이썬뿐 아니라 모든 언어를 배울 때도 똑같다.

###---------------------------
### ch03-3-2
### 값 비교
print('>>>>>>>>>>')
c = [70, 75, 80, 85]

print(c == c[:3] + c[3:])   # index 0 ~ 2까지에 index 3부터 끝까지를 삽입
                            # True
# 하나의 원소도 빠짐 없이 내부 원소와 개수까지 같기 때문에 True가 나왔다.
# 다음을 통해 이를 확인할 수 있다.
print(c[:3])                # [70, 75, 80]
print(c[3:])                # [85]
print(c[:3] + c[3:])        # [70, 75, 80, 85]

### identity(id)
# 리스트도 마찬가지로 효율성을 따지기 위해 어떻게 하는지 보자.
print('>>>>>>>>>>')
c = [70, 75, 80, 85]
temp = c
print(temp, c)               # [70, 75, 80, 85] [70, 75, 80, 85]
print(id(temp))              # 1940641513992
print(id(c))                 # 1940641513992
# object의 indentity를 확안해 보면, temp와 c가 동일한 주소를 가지고 있다.
# 둘 다 같은 id 값을 가지고 있는 것으로 봐서는, 리스트도 문자열과 마찬가지로
# 또는 숫자와 마찬가지로 변수 할당 시에 파이썬의 빠른 속도나 실행
# 쾌적한 환경을 보장하기 위해서 이 객체를,
# 이게 또 깊은 복사 얇은 복사, 나중에 중급이나 심화에서 배울 내용이 나온다.
# 참조형과 불변형 등의 것들이 있는데 이건 기초에서는 다루지 않아도 된다.
# 중요한 것은 위 temp와 c의 id가 똑같이 나왔다는 것이다.
# 이 둘 다 같은 집 주소를 보고 있고 어느 한 쪽이 변경되면 같은 집 주소를
# 보고 있기 때문에 그 집 안에 있는 사람이 빠지면
# 똑같은 결괏값을 확인할 수 있다는 것이다.
# 예를 들어 한 쪽에서 85를 지우면, 다른 쪽에서도 85가 지워진다.
# 이 둘은 같은 곳을 보고 있기 때문이다. (같은 주소에 저장돼 있기 때문이다)
# 파이썬의 효율성 때무에 리스트 역시도 이렇게 하나의 주소 값을 공유한다고 이해하라.

temp.pop(3)         # temp의 index 3을 삭제하라, 즉 85를 삭제하라.
# The pop() method returns the item present at the given index.
# This item is also removed from the list.
print(temp, c)      # [70, 75, 80] [70, 75, 80]
# temp의 index 3을 삭제했는데, c의 index 3도 같이 삭제되었다.

### 리스트 수정, 삭제
# 이것이 우리가 바로 사용할 만한 스킬이다.
print('>>>>>>>>>>')
c = [70, 75, 80, 85]

c[0] = 4
print('c - ', c)            # c -  [4, 75, 80, 85],
                            # index 0이 4로 바뀌어 있다.
# 이렇게 수정을 바로 index 번호로 접근해서 할 수 있다.
## c의 80을 100으로 바꾸려면 어떻게 하면 되는가?
c[2] = 100
print('c - ', c)            # c -  [4, 75, 100, 85]

c = [70, 75, 80, 85]
c[1:2] = ['a', 'b', 'c']
print('c - ', c)            # c -  [70, 'a', 'b', 'c', 80, 85]
                            # c의 index 1, 즉 75에 ['a', 'b', 'c']가 들어갔다.
                            # 75 대신에 'a', 'b', 'c'가 들어갔다.
                            # 단 list 형으로 들어간 게 아니고 각 원소가 들어간다.
c = [70, 75, 80, 85]
c[1:3] = ['a', 'b', 'c']    # index 1, index 2 대신에 ['a', 'b', 'c']이 삽입된다.
print('c - ', c)            # c -  [70, 'a', 'b', 'c', 85]

c = [70, 75, 80, 85]
c[1:2] = [['a', 'b', 'c']]  # 이렇게 대괄호를 하나 또 쓴다면 어떻게 될까?
print('c - ', c)            # c -  [70, ['a', 'b', 'c'], 80, 85]
                            # index 1에 리스트 형태로 들어간다.
                            # index 0은 int, index 1은 list, index 2는 int이다.

c = [70, 75, 80, 85]
c[1:3] = [['a', 'b', 'c']]  # 이렇게 대괄호를 하나 또 쓴다면 어떻게 될까?
print('c - ', c)            # c -  [70, ['a', 'b', 'c'], 85]
                            # index 1, index 2 대신에 ['a', 'b', 'c']이 삽입된다.

c = [70, 75, 80, 85]
c[1] = ['a', 'b', 'c']      # c[1:2] = [['a', 'b', 'c']]와 결괏값이 동일하다.
                            # index 1에 list를 넣으라고 했으므로 list가 들어간다.
print('c - ', c)            # c -  [70, ['a', 'b', 'c'], 80, 85]
                            # list 안에 또 list가 들어간 중첩의 형태로 삽입된다.
print('')

## 정리
c[1:2] = ['a', 'b', 'c']    # 각 원소가 삽입된다.
c[1] = ['a', 'b', 'c']      # list가 삽입된다.

c = [70, 75, 80, 85]
c[1:3] = []                 # index 1, index 2를 삭제하라는 것과 동일
print('c - ', c)            # c -  [70, 85]
                            # 하지만, 삭제할 때 이렇게 하지는 않는다.

## 삭제
c = [70, 75, 80, 85]

del c[2]                    # index 2를 삭제하라.
print('c - ', c)            # c -  [70, 75, 85]

## 리스트 함수
print('>>>>>>>>>>')
a = [5, 2, 3, 1, 4]

print('a - ', a)            # 기본 값 출력을 해 준다.
                            # 정확하게 리스트를 선언했는지 확인한다.

## array a 뒤에 무엇을 추가하고 싶다. 어떻게 하는가?
# a[5] = 10                 # 이렇게 index 5에 10을 넣어주면 들어갈까?
                            # No, 안 들어간다.
                            # IndexError: list assignment index out of range

a[3] = 10                   # 이렇게 하면 되는가? 이건 수정이 된다. 추가가 아니다.
print('a - ', a)            # a -  [5, 2, 3, 10, 4], index 3의 1이 10으로 바뀜.
# 그럼 어떻게 하는가? append를 쓴다.
a = [5, 2, 3, 1, 4]
a.append(10)
print('a - ', a)            # a -  [5, 2, 3, 1, 4, 10], 제대로 추가가 되었다.

## 신기한 함수가 있다. sort, 오름차순 정렬
#The sort() method sorts the list ascending by default.
a.sort()                    # 이런 형태로 써 준다.
print('a - ', a)            # a -  [1, 2, 3, 4, 5, 10], 오름차순 정렬이 됐다.
## index를 거꾸로 정렬을 해 보자. 뒤집어 버려 보자.
# The reverse() method reverses the sorting order of the elements.
a.reverse()
print('a - ', a)            # a -  [10, 5, 4, 3, 2, 1]

# 만약 list에 data가 1억 개 있다면, 위 sort, reverse는 처리에 시간이 많이 걸릴 것임.
# 정렬에 사용되는 알고리즘은 퀵정렬, 병합정렬, 선택정렬, 삽입정렬, 버블정렬 등이 있음.
# 이런 내부적으로 알고리즘을 통해서 정렬이 돼서 우리는 편하게 결괏값을 확인할 수 있음.
# 나중에는 이런 것 또한 고려해서 프로그래밍을 하게 된다.

## value 3이 첫 번째로 등장하는 index를 알려달라.
# The index() method returns the position
# at the first occurrence of the specified value.
a = [5, 2, 3, 1, 4]
a.index(3)                  # 이렇게 하면 된다.
print(a.index(3))           # 2, value 3은 index 2에서 첫 번째로 등장한다.
print(a.index(1))           # 3, value 1은 index 3에서 첫 번째로 등장한다.
print(a.index(5))           # 0, value 5은 index 0에서 첫 번째로 등장한다.

print(a[3])                 # 1, 이건 index 3의 value를 불러온다.
print(a[1])                 # 2, index 1의 value를 불러온다.

# list의 맨 마지막에 원소를 삽입할 때는 append로 하면 됐다.
## 그러면 특정 위치에 원소를 삽입하고 싶으면 어떻게 하면 되는가?
a = [5, 2, 3, 1, 4]

a.insert(2, 7)              # a의 index 2번에 7을 넣어라.
                            # insert(위치, 추가할 값)
print(a)                    # [5, 2, 7, 3, 1, 4], index 2번에 7이 들어가고,
                            # index 2에 있던 원소부터는 뒷 줄로 밀렸다.
a.reverse()                 # index를 뒤집어서 보관하라.
print('a - ', a)            # a -  [4, 1, 3, 7, 2, 5], insert(2, 7)을 한 list의
                            # 순서를 앞뒤를 뒤집어서 보관했다.

## 제거 할 때 위에서 다음 a에서 10을 지우고 싶다면 어떻게 하면 되는가?
print()
a = [1, 2, 3, 4, 7, 5, 10]
print('a - ', a)

del a[6]                    # 이렇게 하면 index 6번은 삭제된다.
                            # del은 함수가 아니라 예약어다.
                            # keyword이다.
print('a - ', a)            # a -  [1, 2, 3, 4, 7, 5]
# 하지만, list의 data가 10만 개가 있으면 지우고 싶은 숫자를 눈으로 찾기 힘들다.

## 그래서 del을 사용하지 않고, remove() 함수를 사용한다.
# The remove() method removes the first matching element
# (which is passed as an argument) from the list.
a = [1, 2, 3, 4, 7, 5, 10, 10]
a.remove(10)                # 첫 번째로 등장하는 10만 삭제했다.
print('a - ', a)            # a -  [1, 2, 3, 4, 7, 5, 10]
# index로 값을 제거하는 것은 data의 size가 크면 사용할 수 없으므로 remove를 쓴다.

## pop을 해 보자
# The pop() method removes the item at the given index from the list
# and returns the removed item. <----- index의 값을 제거한 후 제거한 값을 반환한다.
# The pop() method takes a single argument (index).
# The argument passed to the method is optional.
# If not passed, the default index -1 is passed <----- default index는 -1이다.
# as an argument (index of the last item).      <----- 맨 마지막 원소다.
# If the index passed to the method is not in range,
# it throws IndexError: pop index out of range exception.
a = [1, 2, 3, 4, 7, 5, 10]
print('a - ', a.pop())     # 10, 이렇게 index 값을 안 넣어주면 -1로 처리돼서
                           # 맨 뒤에 있는 원소가 삭제되는데
                           # 출력되는 건 맨 뒤에 있는 원소 10이다.
print('a - ', a)           # 이렇게 a를 출력해 보면 10이 삭제된 것을 확인할 수 있다.
                           # a -  [1, 2, 3, 4, 7, 5]
# 나중에 알고리즘 공부할 때 참조하라.
# stack이라는 것이 있다. stack, queue 이런 것.
# 마직막에 들어온 애가 가장 먼저 나간다. Last in, first out. LIFO
# 접시를 쌓아 놓았을 때도 제일 위에 있는 접시부터 사용하는 게 일반적이다.
# 주로 웹 브라우저의 바로 가기, 뒤로 가기, 브라우저에서 뒤로 가기 버튼을 누르면
# 지금 바로 전에 있었던 페이지로 뒤로 가기가 된다.
# 마지막에 있던 애가 먼저 나온다.
# 자료 구조에서 문제를 풀 때, 정말 많이 사용하는 메소드가 이 pop이다.
print()
a = [1, 2, 3, 4, 5]
a.pop(2)                    # index 2의 value를 삭제하라.
print('a - ', a)            # a -  [1, 2, 4, 5], value 3이 삭제되었다.

## count(element), list 안에 이 element가 몇 개가 들어 있느냐?
a = [1, 2, 3, 4, 4, 4, 5]
print('a - ', a.count(4))   # 3, a에 4가 3개 들어 있다.
print('a - ', a.count(20))  # a -  0, value 20은 list 안에 없다.
# 백 만 개나 되는 list에 특정 element가 몇 개 있는지 알고자 할 때 사용한다.
# 또 특정 element가 있는지 없는지 확인할 때도 쓴다.

# list 추가하는 방법이 두 개 있었다.
# c[1:2] = ['a', 'b', 'c']  # 이렇게 슬라이싱 범위를 사용해서 추가할 수 있다.
# 원하는 원소, 리스트를 추가할 수 있다.

## extend
# 함수로 되어 있다.
# The extend() method adds all the elements of an iterable
# (list, tuple, string etc.) to the end of the list.
# syntax: list1.extend(iterable)
a = [1, 2, 3]
ex = [4, 5]
a.extend(ex)                # 이렇게 함수 식으로 사용할 수 있다.
                            # 이걸 보면 코드를 바로 이해할 수 있다.
                            # 이런 것이 가독성이다.
print('a - ', a)            # a -  [1, 2, 3, 4, 5], 4와 5가 추가되었다.

### 삭제
# remove, pop, del
# 세 개 중 remove를 제일 많이 사용하고, 알고리즘에서는 pop도 많이 사용한다.
# 데이터가 작고 index 번호를 알고 있다면 del을 임시방편으로 사용해서 삭제할 수 있다.
a = [1, 2, 3, 4, 5]
while a:
    data = a.pop()
    print(data)             # 뒤에서부터 값이 반환되면서 삭제된다.

print(a)                    # []
# list a의 원소를 뒤에서부터 거꾸로 값을 반환하면서 삭제한다.
# 원소 모두가 삭제되면 while 반복문은 실행이 멈춘다.
# while문의 실행이 끝나면 list a 안에는 아무 것도 없게 된다.

### 리스트 사용법
# 1. 리스트 선언
# 2. 리스트 특징
# 3. 리스트 인덱싱 - 0부터 시작, 오른쪽에서 왼쪽은 마이너스를 사용.
# 4. 리스트 슬라이싱 - 반복해서 학습해서 익숙해져라.
# 5. 리스트 함수 - append, extend, pop, remove, count
# 6. 리스트 삭제 - remove, pop, del
