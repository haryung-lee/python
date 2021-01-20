# 14891 - 톱니바퀴

# 원형 큐 크기 지정
MAX_QSIZE = 9

class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def enqueue(self, item):
        self.rear = (self.rear + 1) % MAX_QSIZE
        self.items[self.rear] = item

    def dequeue(self):
        self.front = (self.front+1) % MAX_QSIZE
        return self.items[self.front]

    def peek(self):
        return self.items[(self.front + 1) % MAX_QSIZE]


class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def addRear(self, item):
        self.enqueue(item)

    def addFront(self, item):
        self.items[self.front] = item
        self.front = (self.front - 1 + MAX_QSIZE) % MAX_QSIZE

    def deleteRear(self):
        item = self.items[self.rear]
        self.rear = (self.rear - 1 + MAX_QSIZE) % MAX_QSIZE
        return item

    def deleteFront(self):
        return self.dequeue()

    def getSmt(self, idx):
        return self.items[idx]

    def printDeque(self):
        for i in range(1, MAX_QSIZE):
            print(self.items[i], end = ' ')


    # 뒤를 지워서 앞에 넣기
    def clkDir(self):
        self.addFront(self.deleteRear())

    # 앞을 지워서 뒤에 넣기
    def cntClkDir(self):
        self.addRear(self.deleteFront())

arr = [CircularDeque() for i in range(4)]

for i in range(4):
    a = list(input())
    for j in range(8):
        arr[i].addRear(int(a[j]))
    # arr[i].printDeque()

n = int(input())
check = []
rotate = [False] * 4

for i in range(n):
    check = [arr[0].getSmt(3), arr[1].getSmt(7), arr[1].getSmt(3),
             arr[2].getSmt(7), arr[2].getSmt(3), arr[3].getSmt(7)]
    k, dir = map(int, input().split())
    rotate[k - 1] = True

    if k == 1:
       while

    if dir == 1:
        for i in range(4):
            if i == k: continue

        # arr.clkDir()
