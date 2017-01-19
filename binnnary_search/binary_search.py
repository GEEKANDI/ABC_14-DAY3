class BinarySearch(list):
    def __init__(self, a, b, *args):
        list.__init__(self, *args)
        self.length_of_list = a
        self.step = b
        end_of_list = self.length_of_list * self.step
        for i in range(self.step, end_of_list + 1, self.step):
            self.append(i)


    def length(self):
        return len(self)


    def search(self, x_in_list, start_val=0, end_val=None, val_interval=0):
        if not end_val:
            # return self[end_val]
            end_val = self.length - 1
        if x_in_list == self[start_val]:
            return {'index': start_val, 'count': val_interval}
        elif x_in_list == self[end_val]:
            return {'index': end_val, 'count': val_interval}
        center_val = (start_val + end_val) // 2
        if x_in_list == self[center_val]:
            return {'index': center_val, 'count': val_interval}
        elif x_in_list > self[center_val]:
            start_val = center_val + 1
        elif x_in_list < self[center_val]:
            end_val = center_val - 1
        if start_val >= end_val:
            return {'index': -1, 'count': val_interval}
        val_interval += 1
        return self.search(x_in_list, start_val, end_val, val_interval)
