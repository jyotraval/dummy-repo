start=int(input("Start from? ::"))
end=int(input("till?  :"))
for i in range(start,end+1):
    if i == 0 or i == 1:
        continue
    var=0
    for j in range(2,i):
        if i % j == 0:
            var=1
            break
    if var==0:
        print("primw no.",i)

