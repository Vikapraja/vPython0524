#aggregation(len/min/max/sum/etc) in set
s={10,20,5,6,10}
print(s)
print(len(s))
print(min(s))
print(max(s))
print(sum(s))

#sortin in set
print(sorted(s)) #sorted returns always list
print(sorted(s,reverse=True))

#uniun in set
a={10,20,30}
b={30,40,50}
print(a.union(b))
print(b.union(a))

#itersection
print(a.intersection(b))
print(b.intersection(a))

#difference
print(a.difference(b))
print(b.difference(a))














