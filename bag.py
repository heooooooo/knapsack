class tui:
    def __init__(self,khoi_luong,gia,don_gia,phuong_an):
        self.gia=gia
        self.khoi_luong=khoi_luong
        self.don_gia=don_gia
        self.phuong_an=phuong_an

f=open('túi lớn/bag.inp')
g=open('túi lớn/bag.out','w')
n,M=map(int,f.readline().split())
a=[0]*n
for i in range(n):
    khoi_luong,gia=map(int,f.readline().split())
    don_gia=gia/khoi_luong
    phuong_an=0
    a[i]=tui(khoi_luong,gia,don_gia,phuong_an)

for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i].don_gia<a[j].don_gia:
            a[i],a[j]=a[j],a[i]

for i in range(len(a)):
    a[i].phuong_an=M//a[i].khoi_luong
    M-= a[i].phuong_an*a[i].khoi_luong
    if M<a[i].khoi_luong:
        pass
result=0
for i in range(len(a)):
    print(a[i].__dict__)
    result+=a[i].gia*a[i].phuong_an
print(result,file=g)
f.close()
g.close()