class Node:

    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self, header):
        self.header = header
        self.lastNode = header


    def addNode(self, node):
        self.lastNode.next = node
        self.lastNode = node
        self.lastNode.next = None


    def printnodes(self):
        currentNode = self.header
        while currentNode.next!=None:
            print(currentNode.data)
            currentNode = currentNode.next
        print(currentNode.data)
        





if __name__ == "__main__":
    headerNode = Node(1);
    linkedList = LinkedList(headerNode)
    linkedList.addNode(Node(2))
    linkedList.addNode(Node(3))
    linkedList.addNode(Node(4))

    linkedList.printnodes()
