import unittest

from gradescope_utils.autograder_utils.decorators import weight, visibility
import matplotlib
import matplotlib.axes as axes
import pandas as pd
from scipy.stats import pearsonr
import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols

from python.questions.ch3_ex14 import Simulation

class TestSimulation(unittest.TestCase):
  DATA_PATH = "./data/ch3_q14.csv"

  def setUp(self):
    self.sim = Simulation(self.DATA_PATH)

  @weight(0.5)
  @visibility('after_due_date')
  def test_part_b_corr(self):
    """3.14.b.1: Correlation coefficient."""
    obs_corr = self.sim.part_b1()
    exp_corr, _ = pearsonr(self.sim.sim_data.x1, self.sim.sim_data.x2)
    self.assertEqual(obs_corr, exp_corr)

  @weight(0.5)
  @visibility('after_due_date')
  def test_part_b_plot_type(self):
    """3.14.b.2: Scatter plot."""
    figure = self.sim.part_b2()
    self.assertTrue(type(figure) is matplotlib.collections.PathCollection)

  @weight(1)
  @visibility('after_due_date')
  def test_part_c(self):
    """3.14.c: Multiple linear regression."""
    formula = ("y ~ x1 + x2")
    ols_fit = ols(formula, data=self.sim.sim_data).fit()
    ols_summary = ols_fit.summary()
    obs_summary = self.sim.part_c()
    self.assertTrue(type(obs_summary) is statsmodels.iolib.summary.Summary)
    self.assertEqual(obs_summary.as_text(), ols_summary.as_text())

  @weight(1)
  @visibility('after_due_date')
  def test_part_d(self):
    """3.14.d: x1 simple linear regression."""
    formula = ("y ~ x1")
    ols_fit = ols(formula, data=self.sim.sim_data).fit()
    ols_summary = ols_fit.summary()
    obs_summary = self.sim.part_d()
    self.assertTrue(type(obs_summary) is statsmodels.iolib.summary.Summary)
    self.assertEqual(obs_summary.as_text(), ols_summary.as_text())

  @weight(1)
  @visibility('after_due_date')
  def test_part_e(self):
    """3.14.e: x2 simple linear regression."""
    formula = ("y ~ x2")
    ols_fit = ols(formula, data=self.sim.sim_data).fit()
    ols_summary = ols_fit.summary()
    obs_summary = self.sim.part_e()
    self.assertTrue(type(obs_summary) is statsmodels.iolib.summary.Summary)
    self.assertEqual(obs_summary.as_text(), ols_summary.as_text())

  @weight(0.333)
  @visibility('after_due_date')
  def test_part_g1(self):
    """3.14.g.1: Multiple linear regression."""
    extra_obs = pd.DataFrame({"x1": [0.1], "x2":[0.8], "y": [6]})
    updated_sim_data = self.sim.sim_data.append(extra_obs)
    formula = ("y ~ x1 + x2")
    ols_fit = ols(formula, data=updated_sim_data).fit()
    ols_summary = ols_fit.summary()
    obs_summary = self.sim.part_g1()
    self.assertTrue(type(obs_summary) is statsmodels.iolib.summary.Summary)
    self.assertEqual(obs_summary.as_text(), ols_summary.as_text())


  @weight(0.333)
  @visibility('after_due_date')
  def test_part_g2(self):
    """3.14.g.2: x1 simple linear regression."""
    extra_obs = pd.DataFrame({"x1": [0.1], "x2":[0.8], "y": [6]})
    updated_sim_data = self.sim.sim_data.append(extra_obs)
    formula = ("y ~ x1")
    ols_fit = ols(formula, data=updated_sim_data).fit()
    ols_summary = ols_fit.summary()
    obs_summary = self.sim.part_g2()
    self.assertTrue(type(obs_summary) is statsmodels.iolib.summary.Summary)
    self.assertEqual(obs_summary.as_text(), ols_summary.as_text())

  @weight(0.333)
  @visibility('after_due_date')
  def test_part_g3(self):
    """3.14.g.3: x2 linear regression."""
    extra_obs = pd.DataFrame({"x1": [0.1], "x2":[0.8], "y": [6]})
    updated_sim_data = self.sim.sim_data.append(extra_obs)
    formula = ("y ~ x2")
    ols_fit = ols(formula, data=updated_sim_data).fit()
    ols_summary = ols_fit.summary()
    obs_summary = self.sim.part_g3()
    self.assertTrue(type(obs_summary) is statsmodels.iolib.summary.Summary)
    self.assertEqual(obs_summary.as_text(), ols_summary.as_text())
