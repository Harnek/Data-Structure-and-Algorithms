class BinaryTree(object):

	def __init__(self, rootObj):

		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self,newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)

		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self,newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)

		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getLeftChild(self):
		return self.leftChild

	def getRightChild(self):
		return self.rightChild

	def setRootVal(self, obj):
		self.key = obj

	def getRootVal(self):
		return self.key

#Traverse tree
	def preorder(self):
		print(self.key)
		if self.leftChild:
			self.leftChild.preorder()
		if self.rightChild:
			self.rightChild.preorder()

	def postorder(self):
		if self.leftChild:
			self.leftChild.postorder()
		if self.rightChild:
			self.rightChild.postorder()
		print(self.key)

	def inorder(self):
		if self.leftChild:
			self.leftChild.inorder()
		print(self.key)
		if self.rightChild:
			self.rightChild.inorder()


r = BinaryTree(4)
r.insertLeft(42)
r.insertLeft(41)
r.insertRight(23)
r.insertRight(21)
r.leftChild.insertRight(43)
r.rightChild.insertLeft(22)

#	    4
#	41     21
# 42  43 22  23

r.preorder()
print("\n"*2)
r.postorder()
print("\n"*2)
r.inorder()

#print(r.getLeftChild().getLeftChild().getRootVal())
#print(r.getRightChild().getRightChild().getRootVal())