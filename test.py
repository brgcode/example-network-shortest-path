from compas.geometry import Pointcloud, KDTree
from compas.datastructures import Network

cloud = Pointcloud.from_bounds(10, 5, 3, 200)
tree = KDTree(cloud)

network = Network()

for point in cloud:
    network.add_node(x=point[0], y=point[1], z=point[2])

for node in network.nodes():
    point = network.node_coordinates(node)
    for nbr in tree.nearest_neighbors(point, 4, distance_sort=True):
        if nbr[2] < 1e-6:
            continue
        if not network.has_edge(node, nbr[1], directed=False):
            network.add_edge(node, nbr[1])

start = network.get_any_node()
goal = network.get_any_node()
path = network.shortest_path(start, goal)
