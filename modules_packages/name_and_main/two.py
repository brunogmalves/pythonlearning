import one

print("TOP LEVEL IN TWE.PY")

one.func()

if __name__ == "__main__":
    print("Two.py is being run directly!")
else:
    print("Two.py was imported.")