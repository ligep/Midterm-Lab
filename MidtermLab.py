import sys
cementnum = int(input())
cementlist = []
for i in range(cementnum):
    currentlist = input()
    currentlist = currentlist.split()
    for j in range(len(currentlist)):
        currentlist[j] = int(currentlist[j])
    cementlist.append(currentlist)

for cements in cementlist:
    high1 = 0
    index1 = -1
    high2 = 0
    index2 = -1
    waterblocks = 0
    while (index2 != 0):
        for i in range(index1+1, len(cements)):
            if high1 <= cements[i]:
                high1 = high2 = cements[i]
                index1 = index2 = i
            else:
                break
        possiblewall = 0
        possiblewallindex = 0
        for i in range(index2+1, len(cements)):
            if high1 > cements[i]:
                if possiblewall < cements[i]:
                    possiblewall = cements[i]
                    possiblewallindex = i
            if high1 <= cements[i]:
                high2 = cements[i]
                index2 = i
                break
        if index1 == index2:
            high2 = possiblewall
            index2 = possiblewallindex
        smallhigh = 0
        if high1 < high2:
            smallhigh = high1
        else:
            smallhigh = high2

        for x in cements[index1+1:index2]:
            waterblocks += smallhigh-x
        high1 = high2
        index1 = index2
    print(waterblocks)
