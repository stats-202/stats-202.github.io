import collections
import os
from typing import Any, Dict, List, Text, Tuple

from absl import logging
import matplotlib.pyplot as plt
import pandas as pd
from scipy import cluster
from sklearn import preprocessing


class USArrests(object):
  """Chapter 10, Exercise 9."""

  def __init__(self, data_path: Text="../data/USArrests.csv",
               figsize: Tuple[int, int]=(10, 10)):
    """Constructor"""
    self.data_path = data_path
    assert os.path.exists(self.data_path), "USArrests dataset not found."
    logging.info("\tLoading %s", self.data_path)
    self.us_arrests = pd.read_csv(self.data_path, index_col='Unnamed: 0')
    self.figsize = figsize

  def part_a(self) -> Dict[Text, Any]:
    """
    Using the cluster.hierarchy.linkage() and cluster.hierarchy.dendrogram()
    functions, return a figure of the states clustered using hierarchical
    clustering with complete linkage and Euclidean distance.

    n.b. To reuse the cluster results in subsequent questions, please save
    the cluster fit as an attribute, i.e. self.clusters = ...

    Returns:
      A dict of the dendogram values required for the plot.
    """
    self.clusters = cluster.hierarchy.linkage(self.us_arrests, method='complete')
    _, ax = plt.subplots(figsize=self.figsize)
    dendo = cluster.hierarchy.dendrogram(self.clusters,
                                         orientation='top',
                                         labels=self.us_arrests.index,
                                         distance_sort='descending',
                                         show_leaf_counts=True,
                                         ax=ax)
    return dendo

  def part_b(self) -> Dict[int, List[Text]]:
    """
    Using the cluster.hierarchy.cut_tree() function, cut the previously fit
    dendogram into three distinct clusters.

    Returns:
      A dict containing lists of states for each cluster, keyed to integers
      representing the cluster number.
    """
    if not hasattr(self, 'clusters'):
      raise ValueError("clusters not found")
    clusts = cluster.hierarchy.cut_tree(self.clusters, n_clusters=[3])
    groups = collections.defaultdict(list)
    for state, group in zip(self.us_arrests.index, clusts[:,0]):
      groups[group].append(state)

    return groups

  def part_c(self):
    """
    Using the cluster.hierarchy.linkage() and cluster.hierarchy.dendrogram()
    functions, return a figure of the states clustered using hierarchical
    clustering with complete linkage and Euclidean distance after after
    scaling the variables.

    n.b. You can use the preprocessing function from sklearn to do the scaling.

    Returns:
      A dict of the dendogram values required for the plot.
    """
    us_arrests_std = pd.DataFrame(preprocessing.scale(self.us_arrests, axis=0),
                                  columns=self.us_arrests.columns)
    clusters = cluster.hierarchy.linkage(us_arrests_std, method='complete')
    _, ax = plt.subplots(figsize=self.figsize)
    dendo = cluster.hierarchy.dendrogram(clusters,
                                         orientation='top',
                                         labels=self.us_arrests.index,
                                         distance_sort='descending',
                                         show_leaf_counts=True,
                                         ax=ax)
    return dendo


def ch10_ex9():
  logging.info("Chapter 10, Exercise 9.")
  us_arrests = USArrests()

  logging.info("\tPart a.")
  us_arrests.part_a()
  plt.savefig("../results/python/ch10_ex9_part_a.png")

  logging.info("\tPart b.")
  groups = us_arrests.part_b()
  with open("../results/python/ch10_ex9_part_b.txt", "w") as f:
    for group, states in groups.items():
      f.write("Group " + str(group) + ":\n")
      f.write(",".join(states))
      f.write("\n")

  logging.info("\tPart c.")
  us_arrests.part_c()
  plt.savefig("../results/python/ch10_ex9_part_c.png")

