#syntax to import a module from package
    #import package.module as alias
    #from package import module as alias

import mypack.area as ar
print(ar.circle(4))
print(ar.rectangle(4,5))

from mypack import calculator as cl
print(cl.add(4,5))
print(cl.mul(4,5))


