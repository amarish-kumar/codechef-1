wit, bal = map(float, raw_input().split())
withd = int(wit)
if withd % 5 != 0:
    print ("%.2f" % bal)
elif wit + 0.50 > bal:
    print ("%.2f" % bal)
else:
    bal -= wit + 0.5
    print ("%.2f" % bal)
 
