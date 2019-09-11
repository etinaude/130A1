from IP_address import IP_address
from Table import Table
from Histogram import Histogram
import math

class A1:
	def __init__(self, name):
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
	def __str__(self): #modify this
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
	def get_freq(self,ip):
	    self.objects= sorted(self.objects)
	    for i in self.objects:
	        if i.get_ip_address() == ip:
	            return i.get_freq_list()
	def get_sum(self,ip):
	    self.objects= sorted(self.objects)
	    for i in self.objects:
	        if i.get_ip_address() == ip:
	            return i.get_sum_list()
	def get_avg(self,ip):
		self.objects= sorted(self.objects)
		for i in self.objects:
			if i.get_ip_address() == ip:
				return i.get_avg_list()
#Note: helper functions (not in A1)
def get_unique_ip_data_list(data):
    dic = {}
    for i in data:
        dic[i[0]] = []
    for i in data:
        dic[i[0]].append((i[1],i[2]))
    return dic #complete this


def read_file(name):
    f = open(name,"r")
    r = f.read()
    data = r.split()
    ret =[]
    for i in range(1,len(data),7):
        ret.append((data[i+1],int(float(data[i])),int(data[i+4])))
    return ret
	

def main():
	my_ip_list = A1('trace33.txt') #return a list of ip address object
	my_result = my_ip_list.get_statistics()
	t1 = Table(my_result, headers=['IP address', 'Sum', 'Freq', 'Avg'], width=13)
	t1.draw_table()
	print()
	my_result = my_ip_list.get_freq('192.168.0.24')
	t1 = Table(my_result, headers=['Time', 'Freq'])
	t1.draw_table()
	h1 = Histogram(my_result, x_width=3)
	h1.draw_horizontal_histogram(unit=1)
	h1.draw_vertical_histogram(unit=1)
	print()		
	my_result = my_ip_list.get_sum('192.168.0.24')
	t1 = Table(my_result, headers=['Time', 'Sum'])
	t1.draw_table()
	h1 = Histogram(my_result, x_width=3)
	h1.draw_horizontal_histogram(unit=100)
	h1.draw_vertical_histogram(unit=100)
	print()
	my_result = my_ip_list.get_avg('192.168.0.24')
	t1 = Table(my_result, headers=['Time', 'Avg'])
	t1.draw_table()
	h1 = Histogram(my_result, x_width=3)
	h1.draw_horizontal_histogram(unit=10)
	h1.draw_vertical_histogram(unit=10)
	print()
main()
