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
        if not correct:
            ##out of all the keys that are in the update string, find the key inside each of the key's values that occurs the most. That value should go last.  THen find the second most. And the third most. And place them respectively until you're done.
            ## Any values not in the keys list goes in front (ex: 97 isnt a key, so itll be the first in the list)
            keysInUpdateString = {}
            for i in range(len(updates)):
                if updates[i] in keysValues.keys():
                    keysInUpdateString[updates[i]] = 0
            for eachKey in keysInUpdateString.keys():   
                for otherKeys in keysInUpdateString.keys():
                    if eachKey in keysValues[otherKeys]:
                        keysInUpdateString[otherKeys]+=1
            sorted_keys = sorted(keysInUpdateString, key=keysInUpdateString.get)
            for i in range(len(updates)):
                if updates[i] not in sorted_keys:
                    sorted_keys.insert(0, updates[i]) 

            sum+=int(sorted_keys[int(len(sorted_keys)/2)])
    elif "|" in eachLine:
        X, Y = eachLine.split("|")
        X = X.strip()
        Y = Y.strip()
        if Y not in keysValues.keys():
            keysValues[Y] = []
        keysValues[Y].append(X)
    else:
        checkUpdates = True
print(sum)
