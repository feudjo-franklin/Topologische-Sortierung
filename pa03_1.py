def top_order(G):
    n = len(G) #Anzahl der Knoten
    if n == 0:
        return []
    else:
        R = []
        Q = []
        for i in range(n):
            if G[i].name not in R:
                R.append(G[i].name)
                Q.append(G[i])
                while not Q == []:
                    v = Q[-1]
                    i = 0
                    while len(v.successors) > i and v.successors[i].name in R:
                        #umstellen(R)
                        #j = R.index(v.successors[i].name)
                        #R.insert(j,v.name)
                        #R.pop(j-1)
                        #R.pop()
                        if v.successors[i] in Q:
                            return [-1]
                        i += 1
                        umstellen(R)
                        
                    if len(v.successors) > i:
                        w = v.successors[i]
                        R.append(w.name)
                        umstellen(R)
                        Q.append(w)
                    else:
                        Q.pop()

        return R
""" Falls das letzte Element von S ein Kind an der Stelle i in S besitzt,
setze ich das letzte Element von S an der Stelle i-1 und ösche das letzte Element aus S """            
def umstellen(S): 
    s = S[-1]
    n = len(s.successors)
    suc_indexes = []
    for i in range(n):
        if s.successors[i] in S:
            j = S.index(s.successors[i])
            suc_indexes.append(j)
    if suc_indexes != []:
        S.insert(min(suc_indexes), s)
	S.pop()
        
            
class Node:
    def __init__(self):
        self.color = "white"
    
"""
def dfs(r):
    R = [r.name]
    Q = [r]
    K = []
    while not Q == []:
        v = Q[-1]
        i = 0
        while len(v.successors) > i and v.successors[i].name in R:
            j = R.index(v.successors[i].name)
            R.insert(j,v.successors[i].name)
            R.pop()
            if v.successors[i] in Q:
                K.append("k")
            i += 1
            
        if len(v.successors) > i:
            w = v.successors[i]
            R.append(w.name)
            Q.append(w)
        else:
            Q.pop()
    return (R,K)
"""            
n = Node()
m = Node()
n.name = "Quelle"
m.name = "Senke"
n.color = m.color = "white"
n.successors = [m]
m.successors = []
G = [m, n]
print(top_order(G))
"""
n = Node()
m = Node()
n.name = "links"
m.name = "rechts"
n.color = m.color = "white"
n.successors = [m]
m.successors = [n]
G = [m.n]
print(top_order(G))
"""        
