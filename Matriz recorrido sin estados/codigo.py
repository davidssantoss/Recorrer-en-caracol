def main(args):
    print("Lista: {}".format(getM()))
    """print("Sublista" + list(getM()))"""
    
    """[x.split(" " , 1) for x in open ("./matriz.txt", "r").readlines()]"""
    
    

def getM():
    return [x.split() for x in open ("./matriz.txt").readlines()]
	   
"""
def suma_fila(x):
    
	if x == []:
            return 0;
    return x [0] + suma_fila(x[1:])
"""

def listar():
    return 


if __name__ == '__main__':
    import sys
   
    sys.exit(main(sys.argv)) 
