class GrandParent:
    def __init__(self, **kwargs):
        print("GrandParent 被调用了")

class Parent1(GrandParent):
    def __init__(self, name, **kwargs):
        print(f"Parent1: name={name}")
        super().__init__(**kwargs)  # 注释掉，不调用
        self.name = name

class Parent2(GrandParent):
    def __init__(self, age, **kwargs):
        print(f"Parent2: age={age}")
        # super().__init__(**kwargs)  # 这个会执行
        self.age = age

class Child(Parent1, Parent2):
    def __init__(self, name, age):
        super().__init__(name=name, age=age)

c = Child("Tom", 18)
print(Child.mro())

# 注意这个 super().__init__(**kwargs)  parent1  parent2 都要传 因为不传  mro 就会中断了