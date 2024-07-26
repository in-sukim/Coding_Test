

def dfs(x, dictionary, alpha):
    dictionary.append(x)
    for i in alpha : 
        if len(x) != len(alpha) :
            dfs(x+i, dictionary, alpha)
        else :
            x[:-1]
            

def solution(word):
    alpha = ['A','E','I','O','U']
    dictionary = []
    for i in range(len(alpha)) :
        dfs(alpha[i], dictionary, alpha)
    
    return dictionary.index(word) + 1