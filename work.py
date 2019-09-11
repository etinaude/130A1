import math
class A1:
    def __init__(self,name):
        self.objects=[]
        data1 = open(name,"r").read().splitlines()
        data2 =[]
        ret =[]
        for i in range(0,len(data1)):
            data2.append(data1[i].split())
        for i in range(0,len(data2)):
            if len(data2[i])>7:
                ret.append((data2[i][2],int(float(data2[i][0])),int(data2[i][7])))
            else:
                ret.append((data2[i][2],int(float(data2[i][0])),int(data2[i][5])))
        data = ret
        dic = {}
        for i in data:
            dic[i[0]] = []
        for i in data:
            dic[i[0]].append((i[1],i[2]))
        maxx = -9
        for key,val in dic.items():
            if maxx< 1+len(dic[key])//10:
                maxx = 1+len(dic[key])//10
        for key,val in dic.items():
            self.objects.append(IP_address(key,val,maxx))
        #total.append(self.objects)
    def __str__(self):
        self.objects= sorted(self.objects)
        sstr="['"
        for i in self.objects:
            sstr +=i.__str__()+"', '" 
        return sstr[:-4]+"']"
    def get_statistics(self):
        self.objects= sorted(self.objects)
        sstr=[]
        for i in self.objects:
            sstr.append(i.get_statistics()) 
        return sstr
    def get_freq_table(self,ip):
        self.objects= sorted(self.objects)
        for i in self.objects:
            if i.get_ip_address() == ip:
                return i.get_freq_list()
    def get_sum_table(self,ip):
        self.objects= sorted(self.objects)
        for i in self.objects:
            if i.get_ip_address() == ip:
                return i.get_sum_list()
    def get_avg_table(self,ip):
        self.objects= sorted(self.objects)
        for i in self.objects:
            if i.get_ip_address() == ip:
                return i.get_avg_list()
                
                
class IP_address:
    key = ""
    data=[]
    size =0
    pack =[]
    freq =[]
    ave =[]
    def __init__(self,key="",data=[],size=1):
        self.key = key
        self.data =data
        self.size = size
        self.freq = [0]
        self.pack =[0]
        self.ave =[0]
        for i in range(1,size,1):
            self.freq.append(0)
            self.pack.append(0)
            self.ave.append(0)
        j = 0
        for i in range(0,len(data),1):
            #print(math.floor(data[i][0]/10), "    ",math.floor(j/10) )
            self.freq[math.floor(j/10)] +=1
            #print(self.freq)
            self.pack[math.floor(j/10)] +=data[i][1]
            j+=1
        for i in range(0,len(self.freq),1):
            if self.freq[i] > 0:
                self.ave[i] = round(self.pack[i]/self.freq[i],1)
            else:
                self.ave[i] = 0
        if self.freq[-1] ==0:
            self.freq = self.freq[::-1]
            self.pack = self.pack[::-1]
            self.ave = self.ave[::-1]
    def get_ip_address(self):
        return self.key
    def get_freq_list(self):
        out = []
        for i in range(0, len(self.freq),1):
            out.append([i,self.freq[i]])
        return out
    def get_sum_list(self):
        out = []
        for i in range(0, len(self.pack),1):
            out.append([i,self.pack[i]])
        return out
    def get_avg_list(self):
        out = []
        for i in range(0, len(self.ave),1):
            out.append([i,self.ave[i]])
        return out
    def get_statistics(self):
        #ip address, total sum of all packet-size, total frequency, average of all packet-size
        pac = 0
        fre = 0
        eve = 0
        for i in range(0,len(self.ave),1):
            fre += self.freq[i]
            pac += self.pack[i]
        eve = pac/fre
        return [self.key,pac,fre,int(eve)] 
    def __str__(self):
        return self.key+":freq="+str(self.freq)+",sum="+str(self.pack)+",avg="+str(self.ave)
    def __eq__(self,other):
        if self.key == other.get_ip_address():
            return True
        return False
    def __lt__(self,other):
        if self.key[-2:] < other.get_ip_address()[-2:]:
            return True
        return False
        
        
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

def get_unique_ip_data_list(data):
    dic = {}
    for i in data:
        dic[i[0]] = []
    for i in data:
        dic[i[0]].append((i[1],i[2]))
    return dic
    
    
def read_file(name):
    f = open(name,"r")
    r = f.read()
    data = r.split()
    ret =[]
    for i in range(1,len(data),7):
        ret.append((data[i+1],int(float(data[i])),int(data[i+4])))
    return ret
