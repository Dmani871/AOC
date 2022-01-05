def no_of_tree_on_route(incx,incy,filename):
    with open(filename) as file:
        x=0
        y=0
        no_of_tree=0
        for num, line in enumerate(file, 0):
            if num % incy==0:
                line=line.rstrip()
                while x>=len(line):
                    line=line+line
                if line[x]=="#":
                    no_of_tree+=1
                x=x+incx
            y+=incy
        return no_of_tree
r1=no_of_tree_on_route(1,1,'map.txt')
r2=no_of_tree_on_route(3,1,'map.txt')
r3=no_of_tree_on_route(5,1,'map.txt')
r4=no_of_tree_on_route(7,1,'map.txt')
r5=no_of_tree_on_route(1,2,'map.txt')

print(r1*r2*r3*r4*r5)