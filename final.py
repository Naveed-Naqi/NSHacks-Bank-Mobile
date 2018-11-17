
# coding: utf-8

# In[53]:


import numpy as np

import osmnx as ox
import networkx as nx
import folium

import matplotlib.pyplot as plt

from sklearn.neighbors import KDTree

get_ipython().run_line_magic('matplotlib', 'inline')

# creating a graph by using a point in downtown Omaha
old_market = (40.704620, -73.876030)
G = ox.graph_from_point(old_market, distance=5000)

#banks
bank1 = ox.geocode('8000 Cooper Ave, Glendale, NY 11385')
bank2 = ox.geocode('9030 Metropolitan Ave, Rego Park, NY 11374')
bank3 = ox.geocode('7011 Myrtle Ave, Glendale, NY 11385')

fig, ax = ox.plot_graph(G, fig_height=10, fig_width=10, 
                        show=False, close=False, 
                        edge_color='black')
ax.scatter(bank1[1], bank1[0], c='red', s=100)
ax.scatter(bank2[1], bank2[0], c='blue', s=100)
ax.scatter(bank3[1], bank3[0], c ='yellow', s = 100)

plt.savefig('firstnodes.png')


# In[44]:


nodes, _ = ox.graph_to_gdfs(G)
nodes.head()

tree = KDTree(nodes[['y', 'x']], metric='euclidean')
print(bank1)
print(bank2)
print(bank3)
b1_idx = tree.query([bank1], k=1, return_distance=False)[0]
b2_idx = tree.query([bank2], k=1, return_distance=False)[0]
b3_idx = tree.query([bank3], k=1, return_distance=False)[0]
closest_node_to_b1 = nodes.iloc[b1_idx].index.values[0]
closest_node_to_b2 = nodes.iloc[b2_idx].index.values[0]
closest_node_to_b3 = nodes.iloc[b3_idx].index.values[0]


fig, ax = ox.plot_graph(G, fig_height=10, fig_width=10, 
                        show=False, close=False, 
                        edge_color='black')
ax.scatter(bank1[1], bank1[0], c='red', s=100)
ax.scatter(bank2[1], bank2[0], c='blue', s=100)
ax.scatter(bank3[1], bank3[0], c='yellow', s=100)
ax.scatter(G.node[closest_node_to_b1]['x'],
           G.node[closest_node_to_b1]['y'], 
           c='green', s=100)
ax.scatter(G.node[closest_node_to_b2]['x'],   
           G.node[closest_node_to_b2]['y'], 
           c='green', s=100)
ax.scatter(G.node[closest_node_to_b3]['x'],
           G.node[closest_node_to_b3]['y'],
           c='green', s=100)
plt.show()


# In[57]:


route = nx.shortest_path(G, closest_node_to_b3,
                         closest_node_to_b1)

route2 = nx.shortest_path(G, closest_node_to_b1,
                         closest_node_to_b2)
route.pop()
route.extend(route2)

fig, ax = ox.plot_graph_route(G, route, fig_height=10, 
                              fig_width=10, 
                              show=False, close=False, 
                              edge_color='black',
                              orig_dest_node_color='green',
                              route_color='green')
ax.scatter(bank1[1], bank1[0], c='red', s=100)
ax.scatter(bank2[1], bank2[0], c='blue', s=100)
ax.scatter(bank3[1], bank3[0], c='yellow', s=100)

plt.show()
plt.savefig('firstpaths.png')


# In[59]:


m = ox.plot_route_folium(G, route, route_color='green')
folium.Marker(location=bank1, popup = 'BankStop1',
              icon=folium.Icon(color='red')).add_to(m)
folium.Marker(location=bank2, popup = 'BankStop3',
              icon=folium.Icon(color='blue')).add_to(m)
folium.Marker(location=bank3, popup = 'BankStop2',
             icon = folium.Icon(color='purple')).add_to(m)

m.save(outfile = 'finalMap.html')


# In[17]:


nodes, _ = ox.graph_to_gdfs(G)
nodes.head()

tree = KDTree(nodes[['y', 'x']], metric='euclidean')


addresses = ['420 Court Street, Brooklyn, NY 11231', 
             '356 Fulton St, Brooklyn, NY 11201', 
             '516 5th Ave, Brooklyn, NY 11215',
             '37-02 82nd Street, Jackson Heights, NY 11372',
             '1425 Rockaway Pkwy, Brooklyn, NY 11236',
             '1865 2nd Avenue, New York, NY 10029',
             '249 East 86th Street, New York, NY 10028'
            ]

class MapCreation:
    global points, actualPoints
    points = []
    actualPoints = []
    def PointList(a):
        for i in range (0, len(a)):
            points.append(ox.geocode(a[i]))
    
    def PointPlace():
        for i in range (0,len(points)):
            ax.scatter(points[i][1], points[i][0], c='red', s=100)

    def FindNodes(nodes, tree):
        for i in range (0,len(points)):
            b = points[i]
            a = tree.query([b], k=1, return_distance=False)[0]
            actualPoints.append(nodes.iloc[a].index.values[0])
        for i in range (0,len(actualPoints)): #Places New Nodes
            ax.scatter(G.node[actualPoints[i]]['x'],
                       G.node[actualPoints[i]]['y'],
                       c='green', s=100)
            
    def DetermineOrder():
        ORDER = []
        C1 = 0
        C2 = 0
        for i in range (0, len(actualPoints)):
            for j in range(0, len(actualPoints)):
                if i != j:
                    #Ben Shapiro Strikes Again, Libtards
                    sqrt(actualPoints[i][1] + actualPoints
                    
                    
        
            

            

MapCreation.PointList(addresses)

fig, ax = ox.plot_graph(G, fig_height=10, fig_width=10, 
                        show=False, close=False, 
                        edge_color='black')      
#print(points)
#print(len(points))
MapCreation.PointPlace()
MapCreation.FindNodes(nodes, tree)
plt.show()

