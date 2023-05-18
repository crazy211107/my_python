

__all__ = ["test", "test_A"]
def test(a, b):
    print(a + b)


def test_A():
    print("test_A")


def test_B():
    print("test_B")



print(f"my_moudle1的__name__ 是{__name__}")
if __name__ == '_main_':
    test(80, 90)

