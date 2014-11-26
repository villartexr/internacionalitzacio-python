class Node: 
	id = 0
	def __init__(self, state, parent, action, pathcost, defth):
		#print state, parent, action, pathcost		
		self.state=state
		self.parent=parent
		self.action=action
		self.pathcost=pathcost
		self.id=Node.id	
		self.defth=defth
		Node.id=Node.id+1	
		pass
	def path(self):
	#return(s,w,s)
		pass

	def __str__(self):
		if self.parent == None:
			id.None
		else:
			id=self.parent.id
		return str(self.state)+" "+str(self.parent.id)+ "  "+str(self.action)+ " "+str(self.pathcost)

def path (self):
	stack = []
	node = self
	while node.parent != None:
		stack.append(node.action)
		node=node.parent
	stack.reverse()
	return stack
		
if __name__=="__main__":
	n=Node((5,5),None,None, 0)
	n1=Node((5,4), n,'south', 1)
	n2= Node((4,4), n1,'west', 2)
	n3=Node((4,5), n2, 'north', 3)
	print n3
