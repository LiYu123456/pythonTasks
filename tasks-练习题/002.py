# coding:UTF-8
print("Start......")
i=int(input("净利润:"))
arr=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
r=0
for id in range(1,len(arr)):
	if(i>=arr[id]):
		r+=(i-arr[id])*rat[id]
		print(r)
		i=arr[id]
print("最终结果:"+str(r))
print("End........")