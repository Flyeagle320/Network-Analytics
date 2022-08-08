# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:14:15 2022

@author: Rakesh
"""

######################Problem########################################
import pandas as pd

##loading dataset##
routes =  pd.read_csv('D:/DATA SCIENCE ASSIGNMENT/Datasets_Network Analytics/connecting_routes.csv')
routes.drop(routes.columns[6] ,axis=1 , inplace= True)
routes.columns= ["flights", "ID", "main Airport", "main Airport ID", "Destination","Destination  ID","haults","machinary"]

hault = pd.read_csv('D:/DATA SCIENCE ASSIGNMENT/Datasets_Network Analytics/flight_hault.csv')
hault.columns =["ID","Name","City","Country","IATA_FAA","ICAO","Latitude","Longitude","Altitude","Time","DST","Tz database time"]

import networkx as nx
graph =nx.from_pandas_edgelist(routes,source='main Airport' , target = 'Destination')

pos = nx.spring_layout(graph, k= 0.15)
nx.draw_networkx(graph, pos , node_size=15 , node_color = 'red')

##degree centrality##
degree = nx.degree_centrality(graph)
print(degree)

##finding most central aiport #
max_degree = max(degree)

max_degree_index = hault.index[hault['IATA_FAA']== max_degree]
hault.iloc[max_degree_index]

#closeness centrality#
closeness = nx.closeness_centrality(graph)
print(closeness)
#airport close to most airports#term of no of flights#
max_closeness = max(closeness)
max_closeness_index = hault.index[hault['IATA_FAA']== max_closeness]
hault.iloc[max_closeness_index]

#betweeness centrality##
betweeness = nx.betweenness_centrality(graph)
print(betweeness)

##which airport comesbetween most of the routes and it will be intl hub#
max_betweeness = max(betweeness)
max_betweeness_index = hault.index[hault['IATA_FAA'] == max_betweeness]
hault.iloc[max_betweeness_index]

##eigen vector centrality#
eigen_centrality =nx.eigenvector_centrality(graph)
print(eigen_centrality)

##airport with more potential with most dep and arrival#
max_eigen_centrality = max(eigen_centrality)
max_eigen_centrality_index=hault.index[hault['IATA_FAA'] == max_eigen_centrality]
hault.iloc[max_eigen_centrality_index]




