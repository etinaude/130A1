import math
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