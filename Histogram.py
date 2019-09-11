class Histogram:
    x = 5
    y = 10
    data = []
    def __init__(self,data,x_width =5,y_width =10):
        self.x = x_width
        self.y = y_width
        self.data = data
    def __str__(self):
            return "x_width="+str(self.x)+" y_width="+str(self.y)+", data="+str(self.data)
    def draw_vertical_histogram(self,x_index=0,y_index=1,unit=10):
        width= "{0:<" + str(self.x) + "}"
        for i in range(20,0,-1):
            line = ""
            prt = False
            for j in range(0,len(self.data),1):
                if i*unit <= self.data[j][y_index]:
                    line = line + width.format("*")
                    prt = True
                    width= "{0:<" + str(self.x) + "}"
                else:
                    line = line +("{0:<" + str(self.x) + "}").format("")
            if prt == True:
                print(line)
        line = ""
        pre=""
        for k in range(0,len(self.data),1):
            width= "{0:<" + str(self.x) + "}"
            line = line+width.format(self.data[k][0])
            for i in range(0,self.x,1):
                pre = pre+"-"
        print(pre)
        print(line)
    def draw_horizontal_histogram(self,x_index=0,y_index=1,unit=10):
        for i in range(0,len(self.data),1):
            width= "{0:<" + str(self.x) + "}"
            line= width.format(self.data[i][x_index])+"|"
            for j in range(0,int(self.data[i][y_index])//unit,1):
                line = line+"*"
            print(line)
