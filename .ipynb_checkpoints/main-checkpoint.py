# Person(Korea) 이게 다 가져오는겁니다. 초기값, 생성자 모두 다
# 상속을 받아야 super.__init__ 이것도 쓸수 있는겁니다.

print('-------------------------------------------------------------------------------------------')

# 1번
# super().__init__에 'aaaa'를 넣었기 때문에 introduce에서 self.nationName하면 'aaaa' 나오지만 
# super().nationName하면 대한민국이 나오게된다.

#상속
class Korean:
    city = '서울특별시'
    nationName = '대한민국'
    population = 51740000
    name='홍길동'
    #+1000개 데이터..

    def __init__(self,nationName):
        self.nationName=nationName


#클래스 선언
class Person(Korean):

   
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        super().__init__('aaaa')


        
    def introduce(self):
        print('안녕하세요, 저는 '+self.name+'이고, '+str(self.age)+'살입니다.'+super().nationName)

    def getKoreanName(self):
        return super().name

person1 = Person('철수',20,'서울')
person2 = Person('영희',25,'부산')

name = person1.getKoreanName()
print(name)


person1.introduce()
person2.introduce()

print('-------------------------------------------------------------------------------------------')

# 2번
# 두가지 이유
# 클래스 Korean 초기값 nationName에 '대한민국'을 넣었기 때문에 self.nationName하면 '대한민국'이 나온다.
# super().__init__에 '대한민국'이 들어가있기 때문에 self.nationName에 '대한민국'이 나온다.
# 둘중에 하나만 해도 된다. 
# 지금 상황은 원래 내용이 대한민국인데 다시 지우고 대한민국으로 적은것과 동일하다.

# 부모 클래스 (Korean)
class Korean:
    city = '서울특별시'
    nationName = '대한민국'
    population = 51740000
    name = '홍길동'
    # +1000개 데이터..

    def __init__(self, nationName):
        self.nationName = nationName

# 자식 클래스 (Person)
class Person(Korean):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        super().__init__('대한민국')  # 부모 클래스의 생성자 호출

    def introduce(self):
        print(f'안녕하세요, 저는 {self.name}이고, {self.age}살입니다. {self.nationName}')  # self.nationName 사용

    def getKoreanName(self):
        return Korean.name  # 부모 클래스의 클래스 변수 직접 접근

# 객체 생성
person1 = Person('철수', 20, '서울')
person2 = Person('영희', 25, '부산')

# 부모 클래스의 기본 이름 가져오기
name = person1.getKoreanName()
print(name)  # 홍길동

# 소개 출력
person1.introduce()  # 안녕하세요, 저는 철수이고, 20살입니다. 대한민국
person2.introduce()  # 안녕하세요, 저는 영희이고, 25살입니다. 대한민국

print('-------------------------------------------------------------------------------------------')

# 3번 
# class Korea에서 data1 초기값으로 'a'를 줬기 때문에 Person class에서 self.data1에 'a'가 나온다.
# class Person에서 super().__init__에 'new data2'를 넣었고 그렇게되면 부모 생성자를 불러오는데 부모 생성자에 data2를 설정해뒀기 때문에 'new data2'가 나온다.

class Korea:
    data1='a'

    def __init__(self,data2):
        self.data2=data2

    

class Person(Korea):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__('new data2')

    def info(self):
        print(f'data1 :  {self.data1}, data2:   {self.data2}입니다.')



man = Person('홍길동',20)
man.info()

print('-------------------------------------------------------------------------------------------')

# 4번
# class Person에서 super().__init__에 'new data1', 'new data2'를 넣었고 
# super기 때문에 부모생성자를 불러오는데 data1, data2로 설정이 되어있으므로
# 생성자로 내용을 다시 적었기 때문에
# 초기값인 'a'가 아니라 self.data1에 'new data1'이 나오게된다.

class Korea:
    data1='a'

    def __init__(self,data1,data2):
        self.data1=data1
        self.data2=data2

    

class Person(Korea):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__('new data1','new data2')

    def info(self):
        print(f'data1 :  {self.data1}, data2:   {self.data2}입니다.')



man = Person('홍길동',20)
man.info()

print('-------------------------------------------------------------------------------------------')

