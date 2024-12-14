checkUpdates = False
keysValues = {}
file = open("text.txt", "r")
sum=0
for eachLine in file:
    if checkUpdates:
        correct = True
        updates = eachLine.split(",")
        updates[-1] = updates[-1].strip()
        for key in keysValues.keys():
            if key in updates:
                for i in range(updates.index(str(key)), len(updates),1):
                    if str(updates[i]) in keysValues[key]:
                        correct = False
                        break
        if correct:
            sum+=int(updates[int(len(updates)/2)])
    elif "|" in eachLine: ##Line Separator
        X, Y = eachLine.split("|")
        X = X.strip()
        Y = Y.strip()
        if Y not in keysValues.keys():
            keysValues[Y] = []
        keysValues[Y].append(X)
    else:
        checkUpdates = True
print(sum)
