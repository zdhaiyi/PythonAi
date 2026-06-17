__all__ = [ "log_separator2", "log_separator3", "PI"]
PI = 3.1415926
NAME = "Python"

def log_separator1():
    print("- " * 30)

def log_separator2():
    print("* " * 30)

def log_separator3():
    print("+ " * 30)

def log_separator4():
    print("# " * 30)

# 测试
if __name__ == "__main__":
    log_separator1()


