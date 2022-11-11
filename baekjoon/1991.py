import sys
input = sys.stdin.readline
from collections import defaultdict

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BTree:
    def __init__(self, graph):
        self.graph = graph
        self.root = Node('A')
        self.mk_tree(self.root)
        
    def mk_tree(self, node):
        left_data, right_data = self.graph[node.data]
        if left_data != '.':
            node.left = Node(left_data)
            self.mk_tree(node.left)
        if right_data != '.':
            node.right = Node(right_data)
            self.mk_tree(node.right)
        return node

    def preorder_traversal(self, node=None):
        node = self.root if not node else node
        res = node.data
        if node.left:
            res += self.preorder_traversal(node.left)
        if node.right:
            res += self.preorder_traversal(node.right)
        return res

    def inorder_traversal(self, node=None):
        node = self.root if not node else node
        res = ''
        if node.left:
            res += self.inorder_traversal(node.left)
        res += node.data
        if node.right:
            res += self.inorder_traversal(node.right)
        return res
        
    def postorder_traversal(self, node=None):
        node = self.root if not node else node
        res = ''
        if node.left:
            res += self.postorder_traversal(node.left)
        if node.right:
            res += self.postorder_traversal(node.right)
        res += node.data
        return res

def solution(n, graph):
    btree = BTree(graph)
    print(btree.preorder_traversal())
    print(btree.inorder_traversal())
    print(btree.postorder_traversal())

n = int(input().strip())
graph = defaultdict(list)
for _ in range(n):
    parent, left, right = input().strip().split()
    graph[parent] = [left, right]
solution(n, graph)
