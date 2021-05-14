cabinet  = {
    3:'a',
    100:'b',
}#key:value형식

print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3)) # get으로 받을 수도 있다.
print(cabinet.get(5,"사용가능")) # None // 계속 이어 나갈 수 있음

#None을 없애고 사용가능을 채워넣음
print('hi') 

#확인법 in 을 사용하여 확인 가능
print(3 in cabinet) # True
print(5 in cabinet) # False
#String도 가능
cabinet = {
    "a-a" : 'b',
    "b-b" : 'a',
}
print(cabinet["a-a"])
cabinet["a-a"] = "c-c" # 값을 업데이트 가능
print(cabinet["a-a"])

#삭제 가능
del cabinet["a-a"]
print(cabinet.get("a-a"))

#key,value,item 확인가능
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

#clear
cabinet.clear()
print(cabinet)