class TimeMap:

    def __init__(self):
        self.store = {}  # {key: [[value, time],[value, time]...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append([value, timestamp]) #no matter list created or not, have to append

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        value = self.store.get(key, []) #[important] if that key exists, return the [[value, time],[value, time]...] with all appended brackets, else return an empty []

        l, r = 0, len(value) - 1  # calculate the amount of [[value, time],[value, time]...]
        result = ""
        
        while l <= r: #Hard: to return nearest time value
            m = (l+r)//2
            if value[m][1] <= timestamp: #如果符合就先記下來，往右找有沒有更接近而符合的
                result = value[m][0]
                l = m + 1
            else: #如果超過要找的timestamp，R指標往左收斂回去
                r = m - 1
        
        return result


        
