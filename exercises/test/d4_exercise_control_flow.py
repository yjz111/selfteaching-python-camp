# 使用 for...in 循环打印九九乘法表，输出：

# for  i  in range(1,10):
# 	for j in range(1,i+1):
# 		print('%d*%d=%d'%(i,j,i*j),end=' ')
# 	print()


# 使用 while 循环打印九九乘法表并用条件判断把偶数行去除掉，输出：
i = 1
while i <= 9:
	j = 1
	while j <= i:
		if i%2==0:
			break
		print('%d*%d=%d'%(i,j,i*j),end='\t')
		j += 1
	print()
	i += 1
		




