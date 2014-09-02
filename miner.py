import urllib
remove = [',','.','@','%','#','$','*','(',')','^']
def mine(a,weed=True,x=4,z=10):
    global remove
    infomore = False
    z = 10
    x=4
    weed =True
    def find_key(symbol_dic, val):
        return [k for k, v in symbol_dic.iteritems() if v == val][0]
    def striplist(l):
        return([x.strip() for x in l])
    def splitlist(l,k=' '):
        return([x.split(k) for x in l])
    def lowerlist(l):
        return([x.lower() for x in l])
    length = lambda x: len(x) < 5 
    lines = lowerlist(striplist(a))
    #remove unwanted char
    def isin(txt):
        global remove
        for i in remove:
            for j in txt:
                if i in j:
                    return True
        return False
    def weed():
        while isin(lines): 
            I = 0
            for i in lines:
                lines[I] = filter(lambda x: x not in remove,i)
                I += 1
        return lines
    lines = weed()
    #words
    words = []
    def wo():
        extend = words.extend
        for i in lines:
            extend(i.split())
        return words
    words = wo()
    print "Words:"+str(len(words)) 
    #word weeder
    if weed:
        def hasweeds(words):
            for i in words:
                if len(i)<=x:
                    return True
            return False
        def w():
            remove = words.remove
            while hasweeds(words):
                for i in words:
                    if len(i)<=x:
                        remove(i)
            return words
        words = w()
    #collect data
    data = {}
    def d():
        for i in words:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
    d()
    if infomore:
        print data
    #get ten highest appering words
    def tenhighest():
        datalist=data.values()
        datalist.sort()
        dat = []
        datappend = dat.append
        for i in range(z+1):
            datappend([datalist[-1] ,find_key(data,datalist[-1])])
            del datalist[-1]
        for i in range(len(data)):
            counted = []
            countedappend = counted.append
            I=0
            for i in dat:
                if i not in counted:counted.append(i)
                else:del dat[I]
                I += 1
        return dat
    dat = tenhighest()
    print dat 
    def out():
        print"The top "+str(z)+" with a minimumm length of "+str(x)+":"
        #output
        for i in range(len(dat)):
            print dat[i][0],dat[i][1]
    out()
def rundefault(urls=None):
    #import parse as parser
    data = []
    if not urls:
        surls = [str(i)+".txt" for i in range(1,38)]
    #urls = ["http://shakespeare.mit.edu/asyoulikeit/full.html","http://shakespeare.mit.edu/allswell/full.html", "http://shakespeare.mit.edu/comedy_errors/full.html", "http://shakespeare.mit.edu/cymbeline/full.html", "http://shakespeare.mit.edu/lll/full.html", "http://shakespeare.mit.edu/measure/full.html", "http://shakespeare.mit.edu/merry_wives/full.html", "http://shakespeare.mit.edu/midsummerr/full.html", "http://shakespeare.mit.edu/much_ado/full.html", "http://shakespeare.mit.edu/pericles/full.html", "http://shakespeare.mit.edu/taming_shrew/full.html", "http://shakespeare.mit.edu/temptest/full.html", "http://shakespeare.mit.edu//full.html", " http://shakespeare.mit.edu/troilus_cressida/full.html", "http://shakespeare.mit.edu/twelfth_night/full.html", "http://shakespeare.mit.edu/two_gentlemen/full.html", "http://shakespeare.mit.edu//full.html", "http://shakespeare.mit.edu/winters_tale/full.html", "http://shakespeare.mit.edu//full.html", "http://shakespeare.mit.edu/1henryiv/full.html", "http://shakespeare.mit.edu/2henryiv /full.html", "http://shakespeare.mit.edu/henryv/full.html", "http://shakespeare.mit.edu/1henryvi /full.html", "http://shakespeare.mit.edu/2henryvi /full.html", "http://shakespeare.mit.edu/3henryvi /full.html", "http://shakespeare.mit.edu/henryvii/full.html", "http://shakespeare.mit.edu/john/full.html", "http://shakespeare.mit.edu/richardii/full.html", "http://shakespeare.mit.edu/richardiii/full.html", "http://shakespeare.mit.edu/cleopatra/full.html", "http://shakespeare.mit.edu/coriolanus/full.html", "http://shakespeare.mit.edu/hamlet/full.html", "http://shakespeare.mit.edu/julius_casear/full.html", "http://shakespeare.mit.edu/lear/full.html", "http://shakespeare.mit.edu/macbeth/full.html", "http://shakespeare.mit.edu/othelo/full.html", "http://shakespeare.mit.edu/romeo_juliet/full.html", "http://shakespeare.mit.edu/timon/full.html", "http://shakespeare.mit.edu/titus/full.html"]
    for i in urls:
        d = open(i).readlines()
        data.extend(d)
##    while True:
##        try:
##            weed = raw_input("Weed?,True or False" )
##            if not weed in ["True","False"]:raise RuntimeError()
##        except RuntimeError:pass
##        else:
##            if weed == "True":
##                weed = True
##            else:weed = False
##            break
##    if weed:
##        while True:
##            try:x = int(raw_input("minimum word length:"))
##            except ValueError:pass
##            else:break
##    while True:
##        try:z = int(raw_input("Top "))
##        except ValueError:pass
##        else:break
    print mine(data)
##run()
def profile():
    import cProfile
    cProfile.run('mine(open("1.txt").readlines())')
if __name__ == "__main__":
    profile()
