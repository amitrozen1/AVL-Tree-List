#username1 - argov
#id1       - 308447382
#name1     - Yael Argov
#username2 - amitrosen
#id2       - 208279489
#name2     - Amit Rosen

"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor. Constructs a virtual node which can be made real later.
    @type value: str
    @param value: data of your node
    runtime complexity: O(1)
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0  # the size of this node's subtree

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    runtime complexity: O(1)
    """
    def getLeft(self):
        if self.height != -1:
            return self.left
        return None

    """returns the right child
    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    runtime complexity: O(1)
    """
    def getRight(self):
        if self.height != -1:
            return self.right
        return None

    """returns the parent 
    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    runtime complexity: O(1)
    """
    def getParent(self):
        return self.parent

    """return the value
    @rtype: str
    @returns: the value of self, None if the node is virtual
    runtime complexity: O(1)
    """
    def getValue(self):
        if self.height != -1:
            return self.value
        return None

    """returns the height
    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    runtime complexity: O(1)
    """
    def getHeight(self):
        return self.height

    """returns the size
    @rtype: int
    @returns: the size of self, 0 if the node is virtual
    runtime complexity: O(1)
    """
    def getSize(self):
        return self.size

    """sets left child
    @type node: AVLNode
    @param node: a node
    runtime complexity: O(1)
    """
    def setLeft(self, node):
        self.left = node

    """sets right child
    @type node: AVLNode
    @param node: a node
    runtime complexity: O(1)
    """
    def setRight(self, node):
        self.right = node

    """sets parent
    @type node: AVLNode
    @param node: a node
    runtime complexity: O(1)
    """
    def setParent(self, node):
        self.parent = node

    """sets value
    @type value: str
    @param value: data
    runtime complexity: O(1)
    """
    def setValue(self, value):
        self.value = value

    """sets the height of the node
    @type h: int
    @param h: the height
    runtime complexity: O(1)
    """
    def setHeight(self, h):
        self.height = h

    """sets the size of the node
    @type s: int
    @param s: the size
    runtime complexity: O(1)
    """

    def setSize(self, s):
        self.size = s

    """returns whether self is not a virtual node 
    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    runtime complexity: O(1)
    """
    def isRealNode(self):
        return self.height != -1

    """returns whether self is a virtual node 
    @rtype: bool
    @returns: True if self is a virtual node, False otherwise.
    runtime complexity: O(1)
    """
    def isVirtual(self):
        return self.height == -1

    """turns a virtual node real
    @pre: self is virtual
    runtime complexity: O(1)
    """
    def makeReal(self):
        self.height += 1
        self.size = 1
        self.right = AVLNode(None)
        self.right.setParent(self)
        self.left = AVLNode(None)
        self.left.setParent(self)

    """turns a real node virtual
    @pre: self is virtual
    runtime complexity: O(1)
    """
    def makeVirtual(self):
        self.height = -1
        self.size = 0
        self.value = None
        self.right.setParent(None)
        self.left.setParent(None)
        self.right = None
        self.left = None

    """updates the height of the (non-virtual) node
    runtime complexity: O(1)
    """
    def updateHeight(self):
        if self.height != -1:
            self.height = max(self.right.getHeight(), self.left.getHeight()) + 1

    """updates the size of the (non-virtual) node
    runtime complexity: O(1)
    """
    def updateSize(self):
        if self.height != -1:
            self.size = self.right.getSize() + self.left.getSize() + 1


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):

    """
    Constructor.
    runtime complexity: O(1)
    """
    def __init__(self):
        self.root = AVLNode(None)  # constructs a virtual node as the root

    """returns whether the list is empty
    @rtype: bool
    @returns: True if the list is empty, False otherwise
    runtime complexity: O(1)
    """
    def empty(self):
        return self.root.isVirtual()

    """retrieves the i'th item in the list
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: AVLNode
    @returns: the i'th item in the list
    runtime complexity: O(logn) where n is the size of the tree
    """
    def retrieveNode(self, i):
        index = i + 1
        current = self.root
        while current.isRealNode():  # current will never be virtual so current.child will never be None
            currentRank = current.getLeft().getSize() + 1
            if currentRank == index:
                return current
            if currentRank > index:
                current = current.getLeft()
            else:
                index = index - currentRank
                current = current.getRight()

    """retrieves the value of the i'th item in the list
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the value of the i'th item in the list
    runtime complexity: O(logn) where n is the size of the tree
    """
    def retrieve(self, i):
        return self.retrieveNode(i).getValue()

    """returns the rightmost node in the given node's subtree
    @type node: AVLNode
    @pre: node.isRealNode == True
    @param node: The given node
    @rtype: AVLNode
    @returns: the rightmost node in the given node's subtree
    runtime complexity: O(logn) where n is the size of the (sub)tree
    """
    def getMax(self, node):
        current = node
        while current.getRight().isRealNode():
            current = current.getRight()
        return current

    """returns the leftmost node in the given node's subtree
    @type node: AVLNode
    @pre: node.isRealNode == True
    @param node: The given node
    @rtype: AVLNode
    @returns: the leftmost node in the given node's subtree
    runtime complexity: O(logn) where n is the size of the (sub)tree
    """
    def getMin(self, node):
        current = node
        while current.getLeft().isRealNode():
            current = current.getLeft()
        return current

    """returns the predecessor of the given node, None if the given node is the min-ranked node in the tree
    @type node: AVLNode
    @pre: node.isRealNode == True
    @param node: The given node
    @rtype: AVLNode
    @returns: the predecessor of the given node, None if the given node is the min-ranked node in the tree
    runtime complexity: O(logn) where n is the size of the tree
    """
    def getPredecessor(self, node):
        if node.getLeft().isRealNode():
            return self.getMax(node.getLeft())
        current = node
        parent = current.getParent()
        while (parent is not None) and (current is parent.getLeft()):
            current = parent
            parent = parent.getParent()
        return parent

    """returns the successor of the given node, None if the given node is the max-ranked node in the tree
    @type node: AVLNode
    @pre: node.isRealNode == True
    @param node: The given node
    @rtype: AVLNode
    @returns: the successor of the given node, None if the given node is the max-ranked node in the tree
    runtime complexity: O(logn) where n is the size of the tree
    """
    def getSuccessor(self, node):
        if node.getRight().isRealNode():
            return self.getMin(node.getRight())
        current = node
        parent = current.getParent()
        while (parent is not None) and (current is parent.getRight()):
            current = parent
            parent = parent.getParent()
        return parent

    """inserts val at position i in the list
    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we insert
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    runtime complexity: O(logn) where n is the size of the tree
    """
    def insert(self, i, val):
        if i == self.root.getSize():
            if i == 0:
                newNode = self.root
            else:
                newNode = self.getMax(self.root).getRight()
        else:  # i < self.root.getSize()
            current = self.retrieveNode(i)
            if current.getLeft().isVirtual():
                newNode = current.getLeft()
            else:
                current = self.getPredecessor(current)
                newNode = current.getRight()
        newNode.setValue(val)
        newNode.makeReal()
        return self.FixTree(newNode.getParent())

    """rotates the given node left
    @type node: AVLNode
    @pre: node and node.left are real nodes
    @param i: The given node
    runtime complexity: O(1)
    """
    def rotateRight(self, node):
        pivot = node.getLeft()
        node.setLeft(pivot.getRight())
        node.getLeft().setParent(node)
        pivot.setRight(node)
        pivot.setParent(node.getParent())
        if pivot.getParent() is None:
            self.root = pivot
        elif pivot.getParent().getRight() is node:
            pivot.getParent().setRight(pivot)
        else:
            pivot.getParent().setLeft(pivot)
        node.setParent(pivot)
        node.updateHeight()
        node.updateSize()
        pivot.updateHeight()
        pivot.updateSize()

    """rotates the given node right
    @type node: AVLNode
    @pre: node and node.right are real nodes
    @param i: The given node
    runtime complexity: O(1)
    """
    def rotateLeft(self, node):
        pivot = node.getRight()
        node.setRight(pivot.getLeft())
        node.getRight().setParent(node)
        pivot.setLeft(node)
        pivot.setParent(node.getParent())
        if pivot.getParent() is None:
            self.root = pivot
        elif pivot.getParent().getLeft() is node:
            pivot.getParent().setLeft(pivot)
        else:
            pivot.getParent().setRight(pivot)
        node.setParent(pivot)
        node.updateHeight()
        node.updateSize()
        pivot.updateHeight()
        pivot.updateSize()

    """receives two nodes, the first of which is the second's ancestor and makes the first node the parent of 
    the second. The function does not change toBypass's pointers to other nodes
    @type parent: AVLNode
    @pre: parent is the ancestor of child, or None
    @param parent: The given ancestor
    @type child: AVLNode
    @pre: child.isReal() == True
    @param child: The given descendant
    @type toBypass: AVLNode
    @pre: toBypass.isReal() == True
    @param toBypass: The parent's original child (left or right) which is to be replaced
    runtime complexity: O(1)
    """
    def bypassHelper(self, parent, child, toBypass):
        if parent is None:
            self.root = child
        elif parent.getLeft() is toBypass:
            parent.setLeft(child)
        else:
            parent.setRight(child)
        child.setParent(parent)

    """deletes the given node
    @type toDelete: the given node
    @pre: toDelete.isRealNode() == True
    @param toDelete: The given node
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    runtime complexity: O(logn)
    """
    def deleteNode(self, toDelete):
        parent = toDelete.getParent()
        if toDelete.getLeft().isVirtual() and toDelete.getRight().isVirtual():  # no children
            toDelete.makeVirtual()
        elif toDelete.getLeft().isVirtual() or toDelete.getRight().isVirtual():  # one child
            child = toDelete.getLeft() if toDelete.getLeft().isRealNode() else toDelete.getRight()
            toDelete.setParent(None)
            toDelete.makeVirtual()
            self.bypassHelper(parent, child, toDelete)
            toDelete = child  # ensures that fixTree begins at the right spot
        else:  # two children
            # the next 4 lines save successor's information
            successor = self.getSuccessor(toDelete)
            sParent = successor.getParent()
            sHeight = successor.getHeight()
            sSize = successor.getSize()
            # the next 2 lines save successor's new children
            tdLeft = toDelete.getLeft()
            tdRight = toDelete if toDelete.getRight() is successor else toDelete.getRight()

            # the next 4 lines set successor's new parent(including root handling), and toDelete's if it is not\
            # successor's new right child
            self.bypassHelper(parent, successor, toDelete)
            if toDelete.getRight() is not successor:
                sParent.setLeft(toDelete)  # toDelete's new parent is successor's parent
                toDelete.setParent(sParent)
            # the next 8 lines set toDelete's and successor's new children
            toDelete.setLeft(successor.getLeft())
            toDelete.getLeft().setParent(toDelete)
            toDelete.setRight(successor.getRight())
            toDelete.getRight().setParent(toDelete)
            successor.setLeft(tdLeft)
            successor.getLeft().setParent(successor)
            successor.setRight(tdRight)
            successor.getRight().setParent(successor)
            # the next 4 lines update toDelete's and successor's new heights and sizes
            successor.setHeight(toDelete.getHeight())
            successor.setSize(toDelete.getSize())
            toDelete.setHeight(sHeight)
            toDelete.setSize(sSize)

            return self.deleteNode(toDelete)  # recursive call - deletes according to "no children" or "one child"
        return self.FixTree(toDelete.getParent())

    """deletes the i'th item in the list
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    runtime complexity: O(logn)
    """
    def delete(self, i):
        toDelete = self.retrieveNode(i)
        return self.deleteNode(toDelete)

    """Fixes the tree's balance, heights and sizes of node after insertion or deletion
    @type node: AVLNode
    @pre: node is not virtual (can be real or None)
    @param node: the first node to be fixed
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    runtime complexity: O(logn)
    """
    def FixTree(self, node):
        current = node
        counter = 0
        while current is not None:
            BF = current.getLeft().getHeight() - current.getRight().getHeight()  # checks balance
            if BF == -2:
                pivot = current.getRight()
                pivotBF = pivot.getLeft().getHeight() - pivot.getRight().getHeight()
                if pivotBF == 1:
                    self.rotateRight(pivot)
                    counter += 1
                self.rotateLeft(current)
                counter += 1
            elif BF == 2:
                pivot = current.getLeft()
                pivotBF = pivot.getLeft().getHeight() - pivot.getRight().getHeight()
                if pivotBF == -1:
                    self.rotateLeft(pivot)
                    counter += 1
                self.rotateRight(current)
                counter += 1
            else:  # new balance ops required - checks height
                newHeight = max(current.getLeft().getHeight(), current.getRight().getHeight()) + 1
                if newHeight is not current.getHeight():
                    current.setHeight(newHeight)
                    counter += 1
            current.updateSize()
            current = current.getParent()
        return counter

    """returns the value of the first item in the list
    @rtype: str
    @returns: the value of the first item, None if the list is empty
    runtime complexity: O(logn)
    """
    def first(self):
        if self.root.isVirtual():
            return None
        return self.retrieveNode(0).getValue()

    """returns the value of the last item in the list
    @rtype: str
    @returns: the value of the last item, None if the list is empty
    runtime complexity: O(logn)
    """
    def last(self):
        if self.root.isVirtual():
            return None
        return self.retrieveNode(self.root.getSize() - 1).getValue()

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    runtime complexity: O(n)
    """
    def listToArray(self):
        list = []
        if self.root.isVirtual():
            return list
        current = self.getMin(self.root)
        while current is not None:
            list.append(current.getValue())
            current = self.getSuccessor(current)
        return list

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    runtime complexity: O(1)
    """
    def length(self):
        return self.root.getSize()

    """splits the list at the i'th index
    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list according to which we split the tree
    @rtype: list
    @returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
    right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
    runtime complexity: O(log^2(n))
    """
    def split(self, i):
        left = AVLTreeList()
        right = AVLTreeList()
        x = self.retrieveNode(i)
        val = x.getValue()
        left.root = x.getLeft()
        right.root = x.getRight()
        x.makeVirtual()
        current = x
        while current.getParent() is not None:
            parent = current.getParent()
            tempVal = parent.getValue()
            subtree = AVLTreeList()
            subtree.root = parent.getLeft() if parent.getRight() is current else parent.getRight()
            dir = 0 if parent.getRight() is current else 1  # remembers the order in which the trees should be joined \
                                                            # once parent is made virtual
            parent.makeVirtual()
            if dir == 0:
                subtree.insert(subtree.length(), tempVal)
                subtree.concat(left)
                left.root = subtree.root  # since concat always updates self and destroys the given list
            else:
                right.insert(right.length(), tempVal)
                right.concat(subtree)
            current = parent
        return [left, val, right]

    """concatenates lst to self
    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    runtime complexity: O(logn)
    """
    def concat(self, lst):
        diff = abs(self.root.getHeight() - lst.root.getHeight())
        smallTree = self if self.root.getHeight() <= lst.root.getHeight() else lst
        bigTree = lst if self.root.getHeight() <= lst.root.getHeight() else self
        if smallTree.root.getSize() != 0:  # neither of the trees are empty
            # the next 3 lines create a copy of the last node in self and delete the original node
            x = AVLNode(self.last())
            x.makeReal()
            self.delete(self.root.getSize() - 1)
            current = bigTree.root

            while current.getHeight() > smallTree.root.getHeight():
                current = current.getLeft() if smallTree is self else current.getRight()
            # the next 5 lines "plant" the copied node in big tree and set its children
            bigTree.bypassHelper(current.getParent(), x, current)
            x.setLeft(self.root) if smallTree is self else x.setLeft(current)
            x.getLeft().setParent(x)
            x.setRight(current) if smallTree is self else x.setRight(lst.root)
            x.getRight().setParent(x)

            bigTree.FixTree(x)
        self.root = bigTree.root
        lst.root = AVLNode(None)
        return diff

    """searches for a *value* in the list
    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    runtime complexity: O(n)
    """
    def search(self, val):
        counter = 0
        if self.root.isVirtual():
            return -1
        current = self.getMin(self.root)
        while current is not None:
            if current.getValue() is val:
                return counter
            current = self.getSuccessor(current)
            counter += 1
        return -1

    """returns the root of the tree representing the list
    @rtype: AVLNode
    @returns: the root, None if the list is empty
    runtime complexity: O(1)
    """
    def getRoot(self):
        if self.root.isVirtual():
            return None
        return self.root
