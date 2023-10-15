from pathlib import Path
import time

# path = Path("asdf")
path = Path("modules")
print(path.exists())

path = Path("test")
path.mkdir()
time.sleep(3)
path.rmdir()

# path = Path()
# print(path.glob("*"))

# for p in path.glob("*"):
#     print(p)

p = Path(".")
for i in p.iterdir():
    print(i)

path = Path("1-helloworld.py")
print(path.read_text())

path = Path("asdf.txt")
path.write_text("asdfasdfasdfasdf")