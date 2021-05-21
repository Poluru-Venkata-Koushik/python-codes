import ctypes

class dynamicarray:
    def _make_array(self,k):
        return (k*ctypes.py_object)()
    def __init__(self):
        self.n=0;
        self.capacity=1
        self._A_=self._make_array(self.capacity)
    def __len__(self):
        return self.n
    def __getitem__(self, index):
        if not 0<=index<=self.n:
            raise IndexError("Index out of range")
        return self._A[index]
    def __resize__(self):
        B=self._make_array_
