words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
print words.replace("day", "month", 1)

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0], y[-1]
str = y[0] + ' ' + y[-1]
print str

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
pos0 = z[:len(z)/2]
pos1 = z[len(z)/2:]
a = [pos0, pos1]
print a