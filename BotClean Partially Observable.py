# this is more of a simple import test than a real solution

import random
import pickle

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self, endpoint):
        return abs(endpoint.x - self.x) + abs(endpoint.y - self.y)

def next_move(posx, posy, board):
    botPoint = Point(posx, posy)
    visitedPoints.append(botPoint)
    visitedPoints.append(Point(posx - 1, posy - 1))
    visitedPoints.append(Point(posx - 1, posy))
    visitedPoints.append(Point(posx - 1, posy + 1))
    visitedPoints.append(Point(posx, posy - 1))
    visitedPoints.append(Point(posx, posy + 1))
    visitedPoints.append(Point(posx + 1, posy - 1))
    visitedPoints.append(Point(posx + 1, posy))
    visitedPoints.append(Point(posx + 1, posy + 1))
    with open('visitedPoints','wb') as visited:
        pickle.dump(visitedPoints,visited)
    for row in range(len(board)):
        for item in range(len(board[row])):
            if board[row][item] == 'd':
                ds.append(Point(row,item))
    with open('ds','wb') as dirt:
        pickle.dump(ds,dirt)
    nearest_point = None
    for point in ds:
        if nearest_point is None or point.dist(botPoint) < nearest_point.dist(botPoint):
            nearest_point = point
    if nearest_point is not None:
        print_move(nearest_point.x - botPoint.x, nearest_point.y - botPoint.y)
    # solo random non può o va fuori dal grid
    if ds == []:
        notSeen = [x for x in allPoints if x not in visitedPoints]
        nearest_point = random.choice(notSeen)
        print_move(nearest_point.x - botPoint.x, nearest_point.y - botPoint.y)
    if nearest_point.x - botPoint.x == 0 and nearest_point.y - botPoint.y == 0:
        ds.remove(botPoint)


def print_move(remx, remy):
    if remx < 0:
        print('UP')
    elif remx > 0:
        print('DOWN')
    elif remy < 0:
        print('LEFT')
    elif remy > 0:
        print('RIGHT')
    else:
        print('CLEAN')

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    allPoints = []
    for row in range(len(board)):
        for item in range(len(board[row])):
            allPoints.append(Point(row,item))
    ds = []
    visitedPoints = []
    try:
        with open('ds','rb') as dirt:
            pickle.load(dirt)
    except:
        pass
    try:
        with open('visitedPoints','rb') as visited:
            visitedPoints = pickle.load(visited)
    except:
        pass
    next_move(pos[0], pos[1], board)
