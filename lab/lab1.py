class MyClass(object): 
  z=2 
  def __init__(self,a,b): 
      self.x=a              #>>> self.x=a,self.y=b will cause error 'not iterable'
      self.y=b 
      
  def add(self): 
      return self.x+self.y+self.z
 
myinstance=MyClass(3,4)
print myinstance.add()

file=open('myfile.txt','w')
file.write('hello world!!')
#file.flush()

file=open('myfile.txt', 'r')
file.seek(6)
print file.read()
