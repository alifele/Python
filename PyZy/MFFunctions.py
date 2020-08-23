import numpy as np


class MFFunction:
    def __init__(self):
        pass

    def triMF(x,a,b,c,H=1,B=0):
        if type(x)!='list':
            if x<=a:
                return B
            elif x>a and x<=b:
                return (H/(b-a))*(x-a) + B
            elif x<=c and x>b:
                return (H/(b-c))*(x-c) + B
            else:
                return B

        else:
            result = []
            for elem in x:
                if elem<=a:
                    result.append(B)
                elif elem>a and elem<=b:
                    result.append(((H-B)/(b-a))*(elem-a) + B)
                elif elem<=c and elem>b:
                    result.append(((H-B)/(b-c))*(elem-c) + B)
                else:
                    result.append(B)
            return result

    def trapMF(x,a,b,b1,c,H=1,B=0):
        if type(x)!='list':
            if x<=a:
                return B
            elif x>a and x<=b:
                return (H/(b-a))*(x-a) + B
            elif x>b and x<=b1:
                return H
            elif x<=c and x>b1:
                return (H/(b1-c))*(x-c) + B
            else:
                return B

        else:
            result = []
            for elem in x:
                if elem<=a:
                    result.append(B)
                elif elem>a and elem<=b:
                    result.append(((H-B)/(b-a))*(elem-a) + B)
                elif elem>b and elem<=b1:
                    result.append(H)
                elif elem<=c and elem>b1:
                    result.append(((H-B)/(b1-c))*(elem-c) + B)
                else:
                    result.append(B)
            return result

    def GuassMF(x, mu, sigma):
        return np.exp((-(x-mu)**2)/(2*sigma**2) )

    def GuassBellMF(x,b,c, sigma):
        if type(x)!='list':
            if x<=b:
                return np.exp(-((x-b)**2)/(2*sigma**2))
            elif x>b and x<=c:
                return 1
            else:
                return np.exp(-((x-c)**2)/(2*sigma**2))
        else:
            result = []
            for elem in x:
                if elem<=b:
                    result.append(np.exp(-((elem-b)**2)/(2*sigma**2)))
                elif elem>b and elem<=c:
                    result.append(1)
                else:
                    result.append(np.exp(-((elem-c)**2)/(2*sigma**2)))
            return result


    def bellShapeMF(x,mu,width,slope):
        return 1/(1+(np.abs((x-mu)/width))**(2*slope))
