sal = [33911, 50422, 58840, 83933]

increase = [((sal[idx] - sal[idx - 1])/sal[idx - 1])*100 for idx in range(1, len(sal))]

print(increase)

print(((sal[-1] - sal[0])/sal[0])*100)
