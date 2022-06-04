import unittest

import collections
from gradescope_utils.autograder_utils.decorators import weight, visibility
import matplotlib.pyplot as plt
import pandas as pd
from scipy import cluster
from sklearn import preprocessing

from python.questions.ch10_ex9 import USArrests


class TestUSArrests(unittest.TestCase):
  DATA_PATH = "./data/USArrests.csv"

  def setUp(self):
    self.USArrests = USArrests(self.DATA_PATH)

  @weight(1)
  @visibility('after_due_date')
  def test_part_a(self):
    """10.9.a: Dendogram."""
    obs_fig = self.USArrests.part_a()
    clusters = cluster.hierarchy.linkage(self.USArrests.us_arrests,
                                         method='complete')
    dendo = cluster.hierarchy.dendrogram(clusters,
                                         orientation='top',
                                         labels=self.USArrests.us_arrests.index,
                                         distance_sort='descending',
                                         show_leaf_counts=True)
    self.assertCountEqual(obs_fig, dendo)

  @weight(1)
  @visibility('after_due_date')
  def test_part_b(self):
    """10.9.b: Dendogram tree cut (3) groups."""
    fig = self.USArrests.part_a()
    self.assertTrue(hasattr(self.USArrests, 'clusters'))
    obs_groups = self.USArrests.part_b()
    clusters = cluster.hierarchy.linkage(self.USArrests.us_arrests,
                                         method='complete')
    clusts = cluster.hierarchy.cut_tree(clusters, n_clusters=[3])
    exp_groups = collections.defaultdict(list)
    for state, group in zip(self.USArrests.us_arrests.index, clusts[:,0]):
      exp_groups[group].append(state)

    self.assertCountEqual(obs_groups, exp_groups)

  @weight(1)
  @visibility('after_due_date')
  def test_part_c(self):
    """10.9.c: Dendogram with scaled features."""
    obs_fig = self.USArrests.part_c()
    us_arrests_std = pd.DataFrame(preprocessing.scale(self.USArrests.us_arrests,
                                                      axis=0),
                                  columns=self.USArrests.us_arrests.columns)
    clusters = cluster.hierarchy.linkage(us_arrests_std, method='complete')
    dendo = cluster.hierarchy.dendrogram(clusters,
                                         orientation='top',
                                         labels=self.USArrests.us_arrests.index,
                                         distance_sort='descending',
                                         show_leaf_counts=True)
    self.assertCountEqual(obs_fig, dendo)
