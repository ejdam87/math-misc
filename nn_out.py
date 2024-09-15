import matplotlib.pyplot as plt

vals = []
with open("vgg16_outputs.txt", "r") as f:
    content = f.read().split("\n")
    content.pop()
    vals = [float(x) for x in content]

plt.hist(vals)
plt.show()
