# **Use classmethod & staticmethod** in a program.
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    @classmethod
    def subtract(self, a, b):
        return a - b
    def disp(self):
        print("Hello World")
        
m1 = MathUtils.add(5, 3)
print(m1)
m2 = MathUtils.subtract(5, 3)
print(m2)
m3 = MathUtils()
print(m3.disp())