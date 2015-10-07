# Charles Harris Trustpilot backend challenge solution
# -*- coding: utf-8 -*-
# md5 of our target: 4624d200580677270a54ccff86b9610e
# This code ran in 48.6 seconds on a 2.5Ghz i7 Macbook Pro OSX 10.10.5


def prepareList(mySet):
    """function to load words and do initial processing"""
    # strip out words from mySet that have the wrong letters
    newset = set()
    for word in mySet:
        for letter in word: 
            if letter not in goodLetters:
                newset.add(word)
                break
    mySet.difference_update(newset)

    # strip out words from mySet that have too many of the right letters
    newset.clear()
    for word in mySet:
        count = defaultdict(int)
        for letter in word:
            count[letter] += 1
        for letter in goodLetters:
            if count[letter] > check[letter]:
                newset.add(word)
                break
    mySet.difference_update(newset)

    # define list to iterate over, sort, and reorder to make search most efficient
    newList = list(mySet)
    newList.sort(lambda x,y: cmp(len(x), len(y)))
    newList.reverse()

    # put the likely words containing between 4 and 7 letters up front 
    # so we check combos of them first
    countLow = 0
    countHigh = 0
    for word in newList:
        if len(word) > 3:
            countLow += 1
        if len(word) > 7:
            countHigh += 1
    newList = newList[countHigh:countLow] + newList[:countHigh] + newList[countLow:]
    return newList


def recurseHash(combo, counts, depth, newList, check, goodLetters):
    """recursive function to check combos for correct letter count and hash if right"""
    import sys
    import hashlib
    for elem in newList:
        if elem in combo:
            continue
        else:
            # update counts
            for letter in elem:
                counts[letter] += 1

            # set flags to tell if our combo has not enough, or too many, of any letter
            lessFlag = 0
            greaterFlag = 0
            for letter in check:
                if counts[letter] < check[letter]:
                    lessFlag = 1
                elif counts[letter] > check[letter]:
                    greaterFlag = 1

            # check flags and either hash combo, call recurseHash again, or do nothing
            if greaterFlag == 0:
                combo.append(elem)
                if lessFlag == 0:
                    if hashlib.md5(" ".join(combo)).hexdigest() == '4624d200580677270a54ccff86b9610e':
                        print "Success: ", " ".join(combo)
                        sys.exit(0)
                elif len(combo) < depth:
                    recurseHash(combo, counts, depth, newList, check, goodLetters)
                combo.remove(elem)

            # remove letters from counts
            for letter in elem:
                counts[letter] -= 1


# let's do it
if __name__ == '__main__':

    import itertools
    from collections import defaultdict, deque
    check = defaultdict(int)
    letterString = 'poouulttttrywissan'
    for letter in letterString:
        check[letter] += 1
    goodLetters = str('poultrywisan')
    mySet = set(open('wordlist.txt'))
    mySet = set(map(lambda s: s.strip(), mySet))
    newList = prepareList(mySet)
    recurseHash(deque(), defaultdict(int), 3, newList, check, goodLetters)

