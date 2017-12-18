n = input('give me something\n')
par = 1
for i in range(1,n+1):
	 par = par*i
if n ==1:
	print '1 =1'
elif n == 2:
	print '1 * 2 = 2'
elif n == 3:
	print '1 * 2 *3= 6'
else:
	print ('1*2*...*%s =%s'%(n,par))




		
