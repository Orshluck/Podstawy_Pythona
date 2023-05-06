import random

class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail
        self.size = 0
        self.element = None

    def __str__(self):
        result = []
        currentElement = self.head
        while currentElement: ## None works as empty
            result.append(str(currentElement.data))
            currentElement = currentElement.nextE
        return result

    def get(self, e=None):
        if not e:
            return self.head
        currentElement = self.head
        while currentElement:
            if currentElement.data == e:
                return currentElement
            currentElement = currentElement.nextE
        return None


    def delete(self, e):
        currentElement = self.head
        while currentElement:

            if currentElement.nextE.data == e: # if next element is the one to delete
                # here delete element
                currentElement.nextE = currentElement.nextE.nextE # set this element next as the one next next
                currentElement.nextE
            currentElement = currentElement.nextE
        return None

    def append(self, e, func=None):

        currentElement = self.head

        if not func:
            func = lambda x, y: x >= y # return x >= y
        if not currentElement:
            # if list is empty crate head
            self.head = e
            return
        if func(currentElement.data, e.data):
            # check if current
            e.nextE = currentElement
            self.head = e
            return
        while currentElement.nextE:
            if  func(currentElement.nextE.data,e.data):
                e.nextE = currentElement.nextE
                currentElement.nextE = e
                return
            currentElement = currentElement.nextE

        currentElement.nextE = e

    def printSelf(self):
        currentElement = self.head
        while currentElement:
            print(currentElement.data)
            currentElement = currentElement.nextE


#
# ## Testy do zadania 1
# linked_list = MyLinkedList(Element(5))
# for i in range(1,20):
#     x = random.randint(1, 100)
#     print(x)
#     elem = Element(x)
#
#     linked_list.append(elem,lambda x, y: x <= y)
#
# print(linked_list.__str__())