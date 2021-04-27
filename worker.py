
import fnmatch
import string
import difflib
import Levenshtein

def permutation(s):
    """
    Convert string to permutation/anagram

    Params:

    s - your text to be converted
    """
    if s == "":
        return [s]
    else:
        ans = []
        for an in permutation(s[1:]):
            for pos in range(len(an)+1):
                ans.append(an[:pos]+s[0]+an[pos:])
        return ans
    
def dictionary(fileList):
    """
    Get the contents of dictionary file 

    Params:

    fileList - Your File List
    """
    dict = {}
    infile = open(fileList, "r")
    for line in infile:
        word = line.split("\n")[0]
        word = word.lower()
        dict[word] = 1
    infile.close()
    return dict

dic = dictionary('Dictionary/words.txt')

def Unscramble(anagram):
    """
    Find simillar scrambled word into unscrambled one

    Params:

    anagram - your text to be unscramble
    """
    wordList = anagram.split(None)
    result = 'Nothing was Found.'
    solutionList = []

    for word in wordList:
        anaList = permutation(word)
        for ana in anaList:
            if ana in dic:
                dic[ana] = word

    for k, v in dic.items():
        if v != 1:
            solutionList.append(k)

    best_match = difflib.get_close_matches(anagram, solutionList, n=1, cutoff=0.2)
    ret = ''.join(best_match)
    return ret

def Guess(word, dic_file = ''):
    """
    Guessing the word with regex and returns 
    string closests to the original word
    
    Params:

    Word - Your guessed text

    dic_file - Your dictionary file (make sure you have dictionary related to your guess!)
    """
    result = 'Nothing was found.'
    tmp = 'null'

    tmp = word.replace('_', '?')
    tmp = tmp.replace(' ', '')

    if dic_file != '':
        jobDic = dictionary(dic_file)
        filtered = fnmatch.filter(jobDic, tmp)
        print('[!] Using dic_file as filter')
    else:
        filtered = fnmatch.filter(dic, tmp)
        print('[!] Using default dictionary as filter')
    
    closests_dist = 0x7FFFFFFF
    dist = 0

    for guess in filtered:
        dist = Levenshtein.ratio(tmp, guess)
        if dist < closests_dist:
            closests_dist = dist
            result = guess

    return result

def Reverse(word):
    """
    Reverse the word and then returns it

    Params:

    word - Your text to be reversed
    """
    return word[::-1]
