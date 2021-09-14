
class Nodes:

    def __init__(self, value):
        self.data = value
        self.next = None



def PrintNodes(header):
    currentnode = header
    while currentnode.next != None:
        print(currentnode.data)
        currentnode = currentnode.next

    print(currentnode.data)



if __name__ == "__main__":
    print("hello there how are you")

    node1 = Nodes(1)
    node2 = Nodes(2)
    node3 = Nodes(3)

    node1.next = node2
    node2.next = node3
    node3.next = None

    #print(node1.next.next.next)

    PrintNodes(node1)
