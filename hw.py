# 1번
class Device:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand
    
    def info(self):
        print(f'{self.brand}의 {self.name} 기기입니다')
 
d = Device('스마트폰','삼성')
d.info()

print('----------------------------------------------------------')

# 2번
class DeviceCounter:
    def __init__(self):
        self.count = 0

    def add_device(self):
        self.count += 1
        print(f'현재 카운터는 {self.count}입니다.')
        return self.count

    def reset(self):
        self.count = 0
        print(f'카운터를 초기화했습니다.')
        return self.count
    
devicecounter = DeviceCounter()
devicecounter.add_device()
devicecounter.add_device()
devicecounter.reset()
devicecounter.add_device()

print('------------------------------------------------------------')

# 3-1번
class Device:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand
    
    def info(self):
        print(f'{self.brand}의 {self.name} 기기입니다')

class Laptop(Device):
    def info(self):
        print(f'{self.brand}의 {self.name} 노트북입니다')
    
d = Device("태블릿", "애플")
d.info()

l = Laptop("맥북", "애플")
l.info()

print('------------------------------------------------------------')

# 3-2번
class Device:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    
    def info(self, is_laptop=False):  # is_laptop 파라미터 추가
        if is_laptop:
            print(f'{self.brand}의 {self.name} 노트북입니다.')
        else:
            print(f'{self.brand}의 {self.name} 기기입니다.')

class Laptop(Device):
    def info(self):
        super().info(is_laptop=True)  # 부모 클래스의 info()를 활용하면서 노트북 표시

d = Device("태블릿", "애플")
d.info()

l = Laptop("맥북", "애플")
l.info()

print('-------------------------------------------------------------')

