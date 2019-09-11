class Table:
    def __init__(self,a,headers = "None",width = 5):
        #print(a)
        self.data = a
        self.width = width
        self.header = headers
    def __str__(self):
        return "headers="+str(self.header)+", width="+str(self.width)+", data="+str(self.data)
    def draw_table(self):
        out = ''
        line = ''
        b= "{0:<" + str(self.width) + "}"
        for j in range(0,len(self.header),1):
                out = out + b.format(str(self.header[j]))
        for i in range(0,self.width*len(self.header),1):
            line = line + "-"
        print ("|"+out+"|")
        print ("|"+line+"|")
        for i in range(0,len(self.data),1):
            out = ''
            for j in range(0,len(self.data[i]),1):
                out = out + b.format(self.data[i][j])
            print ("|"+out+"|")