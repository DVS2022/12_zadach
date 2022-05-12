class smart_key(object):
    def __init__(self, obj):
        self.obj = obj
    def __lt__(self, other):
        return (other.obj + self.obj) < (self.obj + other.obj)

biggest = lambda x: ''.join(sorted(
    map(str, x),
    key = smart_key
))

print(biggest([12, 9, 31, 97, 98, 96, 555]))




