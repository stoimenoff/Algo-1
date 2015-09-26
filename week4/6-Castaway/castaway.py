# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:49:00 2015

@author: stoimenoff
"""
from queue import Queue

class Castaway:
    def min_num_days(self, graph, starting_point, target_point):
        verts = Queue()
        verts.push(starting_point)
        verts.push(-1)
        visited = [0] * len(graph)
        days = 0
        while verts.size > 1:
            vert = verts.pop()
            if vert == -1:
                days += 1
                verts.push(-1)
                continue
            visited[vert] = 1
            if vert == target_point:
                return days
            for i in range(len(graph)):
                    if graph[vert][i] == 1 and visited[i] == 0:
                        verts.push(i)
            
        return "NNnoooo"
    
def main():
    row = input()
    n = int(row.split(" ")[0])
    m = int(row.split(" ")[1])
    row = input()
    sx = int(row.split(" ")[0])
    sy = int(row.split(" ")[1])
    fx = int(row.split(" ")[2])
    fy = int(row.split(" ")[3])
    num_of_islands = 0
    harbours = []
    num_of_harbours = 0
    imap = []
    exploration_queue = Queue()
    for i in range(n):
        row = list(input())
        imap.append(row) 
    for i in range(n):
        for j in range(m):
            if imap[i][j] == "#" or imap[i][j].isalpha():
                if imap[i][j].isalpha():
                    harbours.append([ imap[i][j] ])
                    num_of_harbours += 1
                exploration_queue.push(m*i + j)
                imap[i][j] = str(num_of_islands)
                while exploration_queue.size > 0:
                    explore = exploration_queue.pop()
                    explore_i = int(explore/m)
                    explore_j = explore % m
                    for adj_i in range(explore_i - 1, explore_i + 2):
                        for adj_j in range(explore_j - 1, explore_j + 2):
                            if adj_i >= 0 and adj_i < n and adj_j >= 0 and adj_j < m:
                                if imap[adj_i][adj_j] == "#" or imap[adj_i][adj_j].isalpha():
                                    exploration_queue.push(m*adj_i + adj_j)
                                    if imap[adj_i][adj_j].isalpha():
                                        if num_of_islands < len(harbours):
                                            harbours[num_of_islands].append(imap[adj_i][adj_j])
                                        else:
                                            harbours.append([imap[adj_i][adj_j]])
                                        num_of_harbours += 1
                                    imap[adj_i][adj_j] = str(num_of_islands)
                                    
                num_of_islands += 1
                
    index_harbours = []
    for i in range(len(harbours)):
        for j in range(len(harbours[i])):
            index_harbours.append(harbours[i][j])
            harbours[i][j] = len(index_harbours) - 1
#    print(index_harbours)
#    for row in harbours:
#        for h in row:
#            print(h, end=" ")
#        print("")
    graph = [[0 for c in range(num_of_harbours)] for r in range(num_of_harbours)]
    for island in harbours:
        for i in range(len(island)):
            for j in range(i + 1, len(island)):
                graph[island[i]][island[j]] = 1
                graph[island[j]][island[i]] = 1

    starting_point = int(imap[sx][sy])
    target_point = int(imap[fx][fy])
    
    h = int(input())
    for r in range(h):
        row = input().split()
        h1 = row[0]
        h2 = row[1]
        for h in range(len(index_harbours)):
            if index_harbours[h] == h1:
                h1 = h
            if index_harbours[h] == h2:
                h2 = h
        graph[h1][h2] = 1
        graph[h2][h1] = 1
        
    #for row in graph:
    #    for item in row:
    #        print(item, end = " ")
    min_distance = None
    for start_harbour in harbours[starting_point]:
        for end_harbour in harbours[target_point]:
            distance = Castaway().min_num_days(graph, start_harbour, end_harbour)
            if min_distance == None:
                min_distance = distance
            elif min_distance > distance:
                min_distance = distance
    print(min_distance + 2)
main()