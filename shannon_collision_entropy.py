import sys
import csv
import matplotlib.pyplot as plt
import csv
import numpy as np
import copy
import operator
import math
git
a=02
idea 1 is here
fowjo
community={}
mster change_1oko
number_of_detection=0

nametag={}
f=open('/Users/heetae/Dropbox/basin/data/for_reduced_t/node_number.csv','rU')
for line in csv.reader(f):
	c1=line[0] # number
	c2=line[1] # name
	nametag[c2]=c1
f.close()
coordinate_y={}
f=open('/Users/heetae/Dropbox/basin/data/for_reduced_t/reduced_nodes.csv','rU')
for line in csv.reader(f):
	c1=line[0]
	c6=line[5]
	c7=line[6]
	coordinate_y[nametag[c1]]=c7
f.close()

ordered_community_class={}
for g in range(1,101):
	f=open('/Users/heetae/Dropbox/basin/comminuty/MatLabData/LouvainResultsIdentified/ChileanPowerGrid_adj_matrix_comm_g0.0323_%s.txt' % g,'rU')
	community_class={}
	commu_={}
	first_line=f.readline().split()[5]
	f.seek(0)
	# print g
# comment

	
	if int(first_line) == 3:
# indent
		number_of_detection+=1
		for line in f.readlines():
			if not line.startswith('#'):
				node=line.split()[0]
				community_id=line.split()[1]
				community_class[node]=community_id


		degree_for_color_={}
		for co in range(int(first_line)):
			degree_for_color_[str(co+1)]=[] # degree-for_color[1]=[node,node,node....]

		for x1 in community_class:
			degree_for_color_[community_class[x1]].append(coordinate_y[x1]) # degree_for_color_[1]=[123,234,25...y coordinate]

		max_degree_of_commu={}
		for co in range(int(first_line)):
			max_degree_of_commu[str(co+1)]=max(degree_for_color_[str(co+1)])
		sorted_commu=sorted(max_degree_of_commu.items(),key=operator.itemgetter(1),reverse=True)

		order_of_={}
		for co in range(int(first_line)):
			order_of_[sorted_commu[co][0]]=co+1
		
		for x in community_class: #{('0':('1':1,'2':30,'3':40))}
			if not x in ordered_community_class.keys():
				ordered_community_class[x]={}
			if not order_of_[community_class[x]] in ordered_community_class[x].keys():
				ordered_community_class[x][order_of_[community_class[x]]]=0
			ordered_community_class[x][order_of_[community_class[x]]]+=1

	
	f.flush()
	f.close()
shannon={}
for x in ordered_community_class.keys():
	shannon[x]=0
	for k,v in ordered_community_class[x].items():
		shannon[x]+=-(float(v)/number_of_detection)*((math.log(float(v)/number_of_detection))/math.log(2))

collision={}
for x in ordered_community_class.keys():
	collision[x]=0
	for k,v in ordered_community_class[x].items():
		collision[x]+=-(math.log(((float(v)*float(v))/(number_of_detection*number_of_detection)))/math.log(2))

node_number={}
f=open('/Users/heetae/Dropbox/basin/data/for_reduced_t/node_number.csv','rU')
for line in csv.reader(f):
	c1=line[0]
	c2=line[1]
	node_number[c1]=c2
f.close()

f=open('community_result_323_entropy.csv','w')
f.write('Id,node_number,shannon,collision\n')
for n in community_class:
	f.write(str(node_number[n])+','+str(n)+','+str(shannon[n])+','+str(collision[n])+'\n')
f.flush()
f.close()