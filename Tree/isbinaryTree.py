# Validate_Binary_Tree_Nodes

leftchild = [-1, -1, 0, 1]
rightchild = [-1, -1, -1, 2]
# leftchild = [1, -1, 3, -1]
# rightchild = [2, 3, -1, -1]

from collections import deque

#se ognuno può essere root allora li provo tutti
def isbinaryTree(left, right, n, root):
    visited = set([root])
    q = deque()
    q.append(root)
    while q:
        i = q.popleft()
        if leftchild[i] in visited: return False
        if rightchild[i] in visited: return False
        if leftchild[i] != -1:
            q.append(leftchild[i])
            visited.add(leftchild[i])
        if rightchild[i] != -1:
            q.append(rightchild[i])
            visited.add(rightchild[i])

    return len(visited) == n

def solution(left, right, n):
    for i in range(n):
        if isbinaryTree(left, right, n, i):
            print(i)
            return True
    return False


solution(leftchild, rightchild, 4)