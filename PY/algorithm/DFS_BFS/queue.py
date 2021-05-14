#먼저 들어오는 데이터가 먼저 나가는 선입 선출의 구조
#입구가 출구가 모두 뚫려있는 터널과 같은 형태
#차례대로 나감(대기열)
from collections import deque #list가 아닌 deque를 쓰는게 훨씬 빠르다
queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() #왼쪽의 것이 나감
queue.append(1)
queue.append(4)
queue.popleft() #왼쪽의 것이 나감

print(queue)
queue.reverse()
print(queue)