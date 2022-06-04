import unittest

from gradescope_utils.autograder_utils.decorators import weight, visibility
import matplotlib
import matplotlib.axes as axes
from pandas.testing import assert_frame_equal
import statsmodels
from statsmodels.formula.api import ols

from python.questions.ch3_ex9 import Auto

class TestAuto(unittest.TestCase):
  DATA_PATH = "./data/Auto.csv"

  def setUp(self):
    self.Auto = Auto(self.DATA_PATH)

  @weight(0.5)
  @visibility('after_due_date')
  def test_part_a_plot_count(self):
    """3.9.a: Scatter plot matrix size."""
    obs_fig = self.Auto.part_a()
    self.assertEqual(obs_fig.shape, (7, 7))

  @weight(0.5)
  @visibility('after_due_date')
  def test_part_a_plot_type(self):
    """3.9.a: Scatter plot matrix plots."""
    obs_fig = self.Auto.part_a()
    for i in range(7):
      for j in range(7):
        self.assertTrue(type(obs_fig[i][j]) is axes.Subplot)

  @weight(1)
  @visibility('after_due_date')
  def test_part_b(self):
    """3.9.b: Correlation matrix."""
    obs_matrix = self.Auto.part_b()
    exp_matrix = self.Auto.auto.corr()
    assert_frame_equal(obs_matrix, exp_matrix)

  @weight(1)
  @visibility('after_due_date')
  def test_part_c(self):
    """3.9.c: Multiple linear regression."""
    formula = ("mpg ~ cylinders + displacement + horsepower + weight "
               "+ acceleration + year + origin")
    ols_fit = ols(formula, data=self.Auto.auto).fit()
    ols_summary = ols_fit.summary()
    obs_summary = self.Auto.part_c()
    self.assertTrue(type(obs_summary) is statsmodels.iolib.summary.Summary)
    self.assertEqual(obs_summary.as_text(), ols_summary.as_text())

  @weight(0.25)
  @visibility('after_due_date')
  def test_part_d1(self):
    """3.9.d.1: fitted vs residuals."""
    obs_summary = self.Auto.part_c()
    self.assertTrue(hasattr(self.Auto, 'ols_fit'))
    figure = self.Auto.part_d1()
    self.assertTrue(type(figure) is matplotlib.collections.PathCollection)

  @weight(0.25)
  @visibility('after_due_date')
  def test_part_d2(self):
    """3.9.d.2: Q-Q plot."""
    obs_summary = self.Auto.part_c()
    self.assertTrue(hasattr(self.Auto, 'ols_fit'))
    figure = self.Auto.part_d2()
    self.assertTrue(type(figure) is matplotlib.figure.Figure)

  @weight(0.25)
  @visibility('after_due_date')
  def test_part_d3(self):
    """3.9.d.3: sqrt(|studentized residuals|) vs fitted values."""
    obs_summary = self.Auto.part_c()
    self.assertTrue(hasattr(self.Auto, 'ols_fit'))
    figure = self.Auto.part_d3()
    self.assertTrue(type(figure) is matplotlib.collections.PathCollection)

  @weight(0.25)
  @visibility('after_due_date')
  def test_part_d4(self):
    """3.9.d.4: studentized residuals vs leverage values."""
    obs_summary = self.Auto.part_c()
    self.assertTrue(hasattr(self.Auto, 'ols_fit'))
    figure = self.Auto.part_d4()
    self.assertTrue(type(figure) is matplotlib.figure.Figure)

  @weight(1)
  @visibility('after_due_date')
  def test_part_e(self):
    """3.9.e: Custom (interactions) multiple linear regression."""
    summary = self.Auto.part_e()
    self.assertTrue(type(summary) is statsmodels.iolib.summary.Summary)

  @weight(1)
  @visibility('after_due_date')
  def test_part_f(self):
    """3.9.f: Custom (transformations) multiple linear regression."""
    summary = self.Auto.part_f()
    self.assertTrue(type(summary) is statsmodels.iolib.summary.Summary)

