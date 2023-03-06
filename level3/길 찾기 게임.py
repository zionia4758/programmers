import sys
sys.setrecursionlimit(10001)
class Tree:
    def __init__(self,val,idx):
        self.val = val
        self.idx = idx
        self.left = None
        self.right = None
    def insert(self, val,idx):
        if val < self.val:
            if self.left == None:
                self.left = Tree(val,idx)
            else:
                self.left.insert(val,idx)
        elif val > self.val:
            if self.right == None:
                self.right = Tree(val,idx)
            else:
                self.right.insert(val,idx)

def solution(nodeinfo):
    answer = [[]]
    idx = 0
    for n in nodeinfo:
        n.append(idx)
        idx+=1
    nodeinfo.sort(key = lambda x:x[1],reverse = True)
    head = nodeinfo.pop(0)
    tree = Tree(head[0],head[2])
    for n in nodeinfo:
        tree.insert(n[0],n[2])
    preorder = []
    postorder = []
    queue = [tree]
    while queue:
        q = queue.pop()
        preorder.append(q.idx+1)
        if q.right != None:
            queue.append(q.right)
        if q.left!=None:
            queue.append(q.left)

    head = tree
    route = []
    while True:
        if head.left != None:
            temp = head.left
            head.left = None
            route.append(head)
            head = temp
            continue
        if head.right != None:
            temp = head.right
            head.right = None
            route.append(head)
            head = temp
            continue
        if head.left==None and head.right == None:
            postorder.append(head.idx+1)
            if len(route)>0:
                head = route.pop()
            else:
                break
    
    answer = [preorder,postorder]
    return answer
