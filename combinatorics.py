
with open("main.c", "r") as f:

    res = f.read().replace("unsigned long", "unsigned long long")

with open("new.txt", "w") as f:

    f.write(res)