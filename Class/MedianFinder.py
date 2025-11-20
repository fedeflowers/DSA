# MedianFinder

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -1 * num)
        #all in order, max heap have less and min heap has more
        if self.maxheap and self.minheap and self.maxheap[0]*-1 > self.minheap[0]:
            m = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -1*m)
        
        if len(self.maxheap) > len(self.minheap) +1:
            m = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, m *-1)
        if len(self.minheap) > len(self.maxheap) +1:
            m = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, m*-1)

    def findMedian(self) -> float:
        if (len(self.minheap) + len(self.maxheap)) % 2 == 0 :
            return (self.minheap[0] +( self.maxheap[0] * -1))/2
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return self.maxheap[0]*-1

        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

from abc import ABC, abstractmethod

class ModelClassifier(ABC):
    @abstractmethod
    def train(self, x_train, y_train, x_test, y_test):
        pass

    @abstractmethod
    def predict(self, x):
        pass

class DocumentClassifier(ModelClassifier):
    def __init__(self, model_instance):
        self.model = model_instance  # This could be a sklearn, PyTorch, etc. model

    def train(self, x_train, y_train, x_test=None, y_test=None):
        # Example with scikit-learn
        self.model.fit(x_train, y_train)
        # Optionally, you can evaluate on test data
        if x_test is not None and y_test is not None:
            score = self.model.score(x_test, y_test)
            print("Test score:", score)
        return self.model

    def predict(self, x):
        return self.model.predict(x)

#possible use with scikit learn
from sklearn.linear_model import LogisticRegression

sklearn_model = LogisticRegression()
classifier = DocumentClassifier(sklearn_model)
classifier.train(x_train, y_train, x_test, y_test)
prediction = classifier.predict(x_new)

