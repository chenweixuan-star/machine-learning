import random

class BatchDataLoader:
    def __init__(self, data, batch_size, shuffle=False):
        
        self.data = data
        self.batch_size = batch_size
        self.shuffle = shuffle
        self._index = 0  
        self._shuffled_data = None 

    def __iter__(self):
        self._index = 0
        self._shuffled_data = self.data.copy()
        if self.shuffle:
            random.shuffle(self._shuffled_data)
        return self

    def __next__(self):
        if self._index >= len(self._shuffled_data):
            raise StopIteration
        
        start = self._index
        end = min(self._index + self.batch_size, len(self._shuffled_data))
        batch = self._shuffled_data[start:end]
        
        self._index = end
        
        return batch


# 使用示例 
if __name__ == "__main__":
    data = list(range(1, 21))
    print("原始数据:", data)
    
    loader = BatchDataLoader(data, batch_size=6, shuffle=False)
    
    print("\n按批次输出(每批最多6个):")
    for batch in loader:
        print(batch)