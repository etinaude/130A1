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
    def draw_horizontal_histogram(self,x_index=0,y_index=1):
        line =""
        for i in range(0,len(data),1):
            for j in range(0,data[i],1):
                


h2 = Histogram([['May', 37], ['Bob', 74], ['Mike', 23]])
print(h2)