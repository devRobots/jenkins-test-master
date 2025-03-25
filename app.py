import sys
from src.math import sum

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(f"The number {a} + {b} equals {sum(a, b)}")
