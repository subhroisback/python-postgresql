class sset(set):
    def __str__(self):
        return ', '.join([str(i) for i in self])

print(set([1,2,3]))
print(sset([1,2,3]))