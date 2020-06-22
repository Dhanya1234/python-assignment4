a=10
b=20
c=30
def maximum(a,b,c):
  	if(a>=b)and(a>=c):
  		maximum=a
  	elif(b>=a)and(b>=c):
  		maximum=b
  	else:
  		maximum=c
  		
  	return maximum 
print(maximum(a,b,c))