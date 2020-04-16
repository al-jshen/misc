import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.datasets import make_moons

# create a distance matrix given a list of points
def create_distance_matrix(points):
    distance_matrix = np.zeros((len(points), len(points))) # initialize matrix
    for i in range(len(points)):
        for j in range(len(points)):
            dist = np.sqrt(np.square(points[i]-points[j]).sum()) # calculate distance between two points 
            distance_matrix[i, j] = dist # set value of i,j'th point on matrix to distance between point i and point j
    return distance_matrix

# calculate number of neighbours of each point given a distance matrix
def calculate_neighbours(distance_matrix):
    num_neighbours = np.zeros(len(distance_matrix)) # initialize array
    for i in range(len(num_neighbours)):
        num_neighbours[i] = (distance_matrix[i] <= eps).sum() - 1 # calculate number of points within epsilon radius, -1 because don't want to include itself
    return num_neighbours

# calculate whether a point is a core point given number of neighbours
def calculate_core(num_neighbours):
    core = np.zeros(len(num_neighbours)) # initialize array
    for i in range(len(num_neighbours)):
        core[i] = 1 if num_neighbours[i] >= minPoints else 0 # assign 1 if a point has more than minPoints neighbours
    return core

# return indices of all neighbours
def get_neighbours(pt_idx, distance_matrix):
    neighbours = np.where(distance_matrix[pt_idx] <= eps)[0]
    return neighbours

def calculate_border_noise(distance_matrix, core):
    for i in range(len(core)):
        if core[i] == 1: # if index contains a core point
            #core_neighbours = get_neighbours(i, distance_matrix)
            core_neighbours = np.where(distance_matrix[i] <= eps)[0] # find neighbours of a core point
            #core[core_neighbours] = np.array([2 if x==0 else x for x in core[core_neighbours]]) # if the neighbour is not already assigned (is another core) then set it to a border point
            core[core_neighbours] = np.array([1 if x==0 else x for x in core[core_neighbours]]) # same as above line but change colour of border points to same as core points
    core[core==0] = 3 # points that are neither core nor border are noise
    return core

"""
for an unassociated core
get its neighbours
for its neighbours which are core
repeat the above
once you have all those linked cores
assign them all to one cluster
increment cluster
repeat the above until all cores are associated
all_cores = np.where(cores == 1)[0]
start_seed = np.random.choice(all_cores)
def recurse(neighbours, ):
    neighbours = get_neighbours(start_seed, dtmat)
    core_neighbours = np.array([pt for pt in neighbours if pt in all_cores])
    return(neighbours, core_neighbours)
"""

def gen_line(pts=250, max_x=40, mrange=100, brange=100, noise_factor=1):
    m, b = np.random.randint(0, mrange), np.random.randint(0, brange)
    noise = (noise_factor * m) * np.random.randn(pts, 1)

    x = max_x * np.random.rand(pts, 1)
    y = m * x + b + noise
    return np.concatenate((x, y), axis=1)

dat = make_blobs(n_samples=250)[0]
#dat = make_moons(n_samples=250, noise=0.1)[0]
#dat = gen_line(noise_factor=5)
#dat = make_circles(n_samples=250)[0]
eps = 1 # maximum distance to be considered a neighbour
minPoints = 4 # minimum neighbours to be considered a cluster

dtmat = create_distance_matrix(dat)
neighbours = calculate_neighbours(dtmat)
cores = calculate_core(neighbours)
types = calculate_border_noise(dtmat, cores)

from sklearn.cluster import DBSCAN
cluster = DBSCAN(eps=eps, min_samples=minPoints).fit(dat)

f, (ax0, ax1, ax2) = plt.subplots(1, 3, sharey=True, figsize=(12, 4))
ax0.scatter(dat[:,0], dat[:,1])
ax0.title.set_text('Initial')
ax1.scatter(dat[:,0], dat[:,1], c=types)
ax1.title.set_text('Outliers Detected')
ax2.scatter(dat[:,0], dat[:,1], c=cluster.labels_)
ax2.title.set_text('Clusters Classified')
plt.show()

