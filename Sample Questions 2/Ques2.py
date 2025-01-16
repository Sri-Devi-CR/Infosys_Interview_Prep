'''
You are given a tree consisting of N nodes.
You are also given two arrays A and P of size N each, where the
value A[i] denotes the value written on the ith node and the
value P[i] denotes that there is an edge between the
node i and P[i].

We say that an edge is considered good, if after deleting this
edge (this will result in formation of 2 trees), the values in each of
the nodes of the trees are distinct.

Find the total number of good edges present in tree.

Input Format
    1. The first line contains an integer, N, denoting the number of
    elements in A.
    2. Each line i of the N subsequent lines (where 0 ≤ i < N)
    contains an integer describing A[i].
    3. Each line i of the N subsequent lines (where 0 ≤ i < N)
    contains an integer describing P[i].

----------------THIS QUESTION HAS AMBIGUITY----------------
----------------REFRAMED QUESTION----------------

Problem Statement: Good Edges in a Tree
You are given a tree with N nodes, where each node has a value associated with it. 
The tree is represented by two arrays: A and P. 

The array A contains the values of the nodes, 
and the array P describes the parent relationships between the nodes.

An edge in the tree is considered "good" if,
after removing that edge, the resulting two subtrees
each contain unique values (i.e., no value is repeated within each subtree).

Your task is to determine the total number of good edges in the tree.

Input Format
    The first line contains an integer N, the number of nodes in the tree.
    The next N lines contain integers, where the i-th line represents the value A[i] of node i.
    The following N-1 lines contain integers, where each line describes the parent of a node in the format P[i]. For node i, P[i] is the parent of node i. The parent array is 0-indexed, and node indices start from 0.
Constraints
    2 ≤ N ≤ 10^5
    0 ≤ A[i] ≤ 10^6
    0 ≤ P[i] < N for all i from 1 to N-1
Output Format
    Output a single integer representing the total number of good edges in the tree.
'''

input_li = [int(x) for x in input().split()]
n = input_li[0]
A = input_li[1:n+1]
P = input_li[n+1:]


