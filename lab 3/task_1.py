import random
import math

def main():
    n = random.randint(1, 15)
    fact = math.factorial(n)
    print(f"Random number: {n}")
    print(f"Factorial: {fact}")

if __name__ == "__main__":
    main()
