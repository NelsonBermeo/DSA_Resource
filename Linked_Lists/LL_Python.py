#Credit to Dhaval Patel from codebasics youtube channel

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        #The beginning of the ls would take whatever is currently in the
        #   head and would make it the NEXT for the insert you are putting
        #   at the beginning 
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node

    def insert_values(self, data_list):
        #This method will take in a list of values as data_list to insert 
        #   and create a fresh linked list
        self.head = None
        for i in data_list:
            self.insert_at_end(i)
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return 
        itr = self.head
        llstr = ''
        while itr: 
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            #Python cleans up the garbage head so we are good here
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while(itr.next):
            if count == index-1:
                break
            itr = itr.next
            count += 1
        itr.next = itr.next.next

    def insert_at(self, index, data):
        if index<0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while(itr.next):
            if count == index-1:
                break
            itr = itr.next
            count += 1
        saved = itr.next
        itr.next = Node(data)
        itr.next.next = saved

        #or 

        # while itr:
        #     if count == index - 1:
        #         node = Node(data,itr.next)
        #         itr.next=node
        #         break
        #     itr = itr.next
        #     count+=1


if __name__ == '__main__':
    values = [0, 1, 2, 3, 4]
    ll = LinkedList()
    ll.insert_values(values)
    ll.insert_at(6, 8)
    ll.print()