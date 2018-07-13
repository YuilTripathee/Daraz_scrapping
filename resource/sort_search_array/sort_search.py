from operator import attrgetter, itemgetter
class sort_search:
    def __init__(self, seq):
        seq = seq
        self.seq = seq
    
    def __repr__(self):
        return "%s" % self.seq

    def quick_sort(self, seq):
        if len(seq) < 2: return seq
        ipivot = len(seq)//2        # dividing the array
        pivot = seq[ipivot]         # partitioning the array
        if type(seq[0]) is int:
            before = [x for i,x in enumerate(seq) if x <= pivot and i != ipivot] # sorting out values before pivot
            after = [x for i,x in enumerate(seq) if x > pivot and i != ipivot]   # sorting out values after pivot
            return self.quick_sort(before) + [pivot] + self.quick_sort(after)    # merging the sorted arrays
        elif type(seq[0]) is dict:
            before = [x for i,x in enumerate(seq) if x['id'] <= pivot['id'] and i != ipivot] # sorting out values before pivot
            after = [x for i,x in enumerate(seq) if x['id'] > pivot['id'] and i != ipivot]   # sorting out values after pivot
            return self.quick_sort(before) + [pivot] + self.quick_sort(after)    # merging the sorted arrays

    def binary_search(self, item):
        seq = self.seq
        lo, hi = 0, len(seq)        # initializing high and low range
        while lo <= hi:
            mid = (hi + lo)//2      # initializing mid value
            if seq[mid] == item:
                return mid          # return mid if its the desired value
            elif seq[mid] > item:
                hi = mid - 1    # if larger, set mid as high
            else:
                lo = mid + 1        # if low increment the mid by 1 and assign to low
        return  None

if __name__ == '__main__': 
    
    list = [2, 3, 5, 6, 8]
    lista = ["CA818EL0HKWQ0NAFAMZ", "CG185EL043NL4NAFAMZ", "CG185EL0A1ZMWNAFAMZ", "CH190EL0SVI2GNAFAMZ", "CH190EL0YTU48NAFAMZ", "HI453EL0J8378NAFAMZ"]
    lstask = sort_search(lista)
    print(lstask)
    if lstask.binary_search("CA818EL0HKWQ0NAFAMZ") != None:
        print('Present')
        print(lstask.binary_search("CA818EL0HKWQ0NAFAMZ"))
    else:
        print("Absent")
