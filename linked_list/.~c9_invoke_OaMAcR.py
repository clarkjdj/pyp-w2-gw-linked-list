class AbstractLinkedList(object):
    """
    Abstract class representing the LinkedList inteface you must respect.
    
    You must not implement any of the method in this class, and this class
    must never be instantiated. It's just a "guide" of which methods
    the LinkedList class should respect.
    """

    def __str__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __add__(self, other):
        raise NotImplementedError()

    def __iadd__(self, other):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def append(self, element):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

    def pop(self, index=None):
        raise NotImplementedError()


class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        return str(self.elem)

    def __eq__(self, other):
        if isinstance(other, LinkedList):
            return self.elem == other.elem #compare node.elem to value passed to it
        else:
            return self.elem == other

    def __repr__(self):
        return "<Node {}>".format(self.elem)


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        # start at none
        self.start = None
        self.end = None
        #[1,2], self.start (Node(1)) >> Node1.next now pts to Node(2) 
        # set elements to empty list
        elements = [] if not elements else elements
        for val in elements:
            self.append(val)
            

    def __str__(self):
        return str([element.elem for element in self])
    
    def __len__(self):
        return self.count()

    def __iter__(self):
        n = self.start
        while n:
            yield n
            n = n.next

    def __getitem__(self, index):
       for n, node in enumerate(self): 
           if n == index:
               return node

    def __add__(self, other):
       l1 = [ n.elem for n in self]
       l2 = [ n.elem for n in other]
       l3 = l1+l2
       return LinkedList(l3)

    def __iadd__(self, other):
        return self.__add__(other) #  x += 1  == x = x+1

    def __eq__(self, other):
        return [element.elem for element in self] == [element.elem for element in other]

    def append(self, elem):
        #new node
        if self.start == None:  #is it the first node
            self.start = Node(elem)
            self.end = Node(elem)
        elif self.start == self.end:
            self.start.next = Node(elem) #fix first node when adding 2nd
            self.end.next = self.start.next #prior node now  points to new node
            self.end = self.end.next #new node is now end
        else:
            self.end.next = Node(elem) #prior node now  points to new node
            self.end = self.end.next #new node is now end
                
        
    def count(self):
        c = 0
        for e in self:
            c +=1
        return c
        
    def pop(self, index=None):
        prior = self.start
        if len(self)== 0: #If the list is empty, raise an error
            raise IndexError()
            
        elif index == None: #If we're not passing an index
            if len(self) == 1: #And the list only has an item, remove start and end
                temp = self.end
                self.start, self.end = None, None
                return temp
            for element in self: #If the list has several items, remove the last one
                if element.next == None:
                    prior.next = None
                    self.end = prior.next
                    return element
                else:
                    prior = element
        else: #If we did pass an index
            if index >= len(self): raise IndexError() #But the index is greater than the existing number of nodes, raise error
            if len(self) == 1: #If the list contains a single element, remove start and end
                temp = self.end
                self.start, self.end = None, None
                return temp
            if self[index].next == None: #If we're trying to remove the last item
                temp = self[index]
                if self[index-1]:
                    self[index-1].next = None
                    self.end = self[index-1]
            if self[index].next == None: #If we
                else:
                    self.start = self[index].next
                    return temp
            else: #If we're trying to remove anything but the last item    
                temp2 = self[index]
                if self[index-1]:
                    self[index-1].next = self[index+1]
                    return temp2
                else: 
                    self.start = self[index].next
                    return temp2





