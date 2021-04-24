import fnmatch
import Levenshtein
import asyncio

def RemoveFromList(thelist, val):
    """
    Removing Dictionary from list
    """
    return [value for value in thelist if value != val]

def GetDic():
    """
    Gets current Dictionary
    """
    try:
        dicopen = open("DL.txt", "r")
        dicraw = dicopen.read()
        dicopen.close()
        diclist = dicraw.split("\n")
        diclist = RemoveFromList(diclist, '')
        return diclist
    except FileNotFoundError:
        print("No Dictionary!")
        return 
    
def Word2Vect(word):
    """
    Converting Text/Word to Vector
    """
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    w = word.lower()
    wl = list(w)
    for i in range(0, len(wl)):
        if wl[i] in l:
            ind = l.index(wl[i])
            v[ind] += 1
    return v

def Vect2Int(vect):
    """
    Converting vector to Integer/Number
    """
    pv = 0
    f = 0
    for i in range(0, len(vect)):
        wip = (vect[i]*(2**pv))
        f += wip
        pv += 4
    return f
    
def Ints2Dic(dic):
    """
    Gets Dictionary from an Integer/Number
    taken from Vec2Int results
    """
    d = {}
    for i in range(0, len(dic)):
        v = Word2Vect(dic[i])
        Int = Vect2Int(v)
        if Int in d:
            tat = d.get(Int)
            tat.append(dic[i])
            d[Int] = tat
        elif Int not in d:
            d[Int] = [dic[i]]
    return d
        
d = GetDic()
ind = Ints2Dic(d)

async def Unscramble(word):
    """
    Unscramble the Word/Text
    and returns 'Nothing was found'
    if the results is not avaiable on
    current Dictionary.
    """
    v = Vect2Int(Word2Vect(word))
    ret = ind.get(v, 'Nothing was found.')
    
    return ret


async def Guess(word):
    """
    Guessing the word with regex and returns 
    string closests to the original word

    (I'd say about 80% accuracy)
    """
    closests_dist = 0x7FFFFFFF
    dist = 1
    result = "Nothing was found"

    if '_' in word:
        word = word.replace('_', '?')

    filtered = fnmatch.filter(d, word)

    for guess in filtered:
        dist = Levenshtein.distance(word, guess)
        if dist < closests_dist:
            closests_dist = dist
            result = guess

    return result
