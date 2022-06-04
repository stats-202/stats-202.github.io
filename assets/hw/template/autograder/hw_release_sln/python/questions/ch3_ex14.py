import os
from typing import Text, Tuple

from absl import logging
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pearsonr
import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols

class Simulation(object):
  """Chapter 3, Exercise 14."""

  def __init__(self, data_path: Text="../data/ch3_q14.csv",
               figsize: Tuple[int, int]=(10, 10)):
    """Constructor

    Attrubutes:
      sim_data: A pd.DataFrame containing the simulation data to analyze.
      figsize: A tuple specifying the default size for figures.
    """
    self.data_path = data_path
    assert os.path.exists(self.data_path), "ch3_q14 dataset not found."
    logging.info("\tLoading %s", self.data_path)
    self.sim_data = pd.read_csv(self.data_path)
    self.figsize = figsize

  def part_b1(self) -> float:
    """
    Using the pearsonr() function from the scipy.stats module, estimate the
    Pearson correlation coefficient.

    Returns:
      A float value containing the Pearson correlation coefficient.
    """
    # YOUR CODE STARTS HERE
    corr, _ = pearsonr(self.sim_data.x1, self.sim_data.x2)
    # raise NotImplementedError
    # YOUR CODE ENDS HERE
    return corr

  def part_b2(self) -> matplotlib.collections.PathCollection:
    """
    Use the scatter() method from matplotlib to return a scatter plot of
    x1 vs x2. Comment on what you see.

    Returns:
      A matplotlib.collections.PathCollection object containing the scatter plot.
    """
    # YOUR CODE STARTS HERE
    _, ax = plt.subplots(figsize=self.figsize)
    ax.set_xlabel("x2")
    ax.set_ylabel("x1")
    figure = ax.scatter(self.sim_data.x2, self.sim_data.x1)
    # raise NotImplementedError
    # YOUR CODE ENDS HERE
    return figure

  def part_c(self) -> statsmodels.iolib.summary.Summary:
    """
    Use the statsmodels ols() function to perform a multiple linear regression with y
    as the response and x1, x2 as the predictors. Return the results using the
    summary() method. Comment on the output.

    Returns:
      A statsmodels Summary object, containing the summary results of the ols
      fit.
    """
    # YOUR CODE STARTS HERE
    formula = ("y ~ x1 + x2")
    ols_fit = ols(formula, data=self.sim_data).fit()
    ols_summary = ols_fit.summary()
    # YOUR CODE ENDS HERE
    return ols_summary

  def part_d(self) -> statsmodels.iolib.summary.Summary:
    """
    Use the sm.OLS() function to perform a multiple linear regression with y
    as the response and x1 as the predictor. Return the results using the
    summary() method. Comment on the output.
    """
    # YOUR CODE STARTS HERE
    formula = ("y ~ x1")
    ols_fit = ols(formula, data=self.sim_data).fit()
    ols_summary = ols_fit.summary()
    # YOUR CODE ENDS HERE
    return ols_summary

  def part_e(self) -> statsmodels.iolib.summary.Summary:
    """
    Use the statsmodels ols() function to perform a multiple linear regression with y
    as the response and x2 as the predictor. Return the results using the
    summary() method. Comment on the output.
    """
    # YOUR CODE STARTS HERE
    formula = ("y ~ x2")
    ols_fit = ols(formula, data=self.sim_data).fit()
    ols_summary = ols_fit.summary()
    # YOUR CODE ENDS HERE
    return ols_summary

  def part_g1(self) -> statsmodels.iolib.summary.Summary:
    """
    Use the statsmodels ols() function to perform a multiple linear regression with y
    as the response and x1, x2 as the predictors on the updated data. Return
    the results using the summary() method. Comment on the output.

    Returns:
      A statsmodels Summary object, containing the summary results of the ols
      fit.
    """
    extra_obs = pd.DataFrame({"x1": [0.1], "x2":[0.8], "y": [6]})
    updated_sim_data = self.sim_data.append(extra_obs)
    # YOUR CODE STARTS HERE
    formula = ("y ~ x1 + x2")
    ols_fit = ols(formula, data=updated_sim_data).fit()
    ols_summary = ols_fit.summary()
    # YOUR CODE ENDS HERE
    return ols_summary

  def part_g2(self) -> statsmodels.iolib.summary.Summary:
    """
    Use the sm.OLS() function to perform a multiple linear regression with y
    as the response and x1 as the predictors on the updated data. Return the
    results using the summary() method. Comment on the output.

    Returns:
      A statsmodels Summary object, containing the summary results of the ols
      fit.
    """
    extra_obs = pd.DataFrame({"x1": [0.1], "x2":[0.8], "y": [6]})
    updated_sim_data = self.sim_data.append(extra_obs)
    # YOUR CODE STARTS HERE
    formula = ("y ~ x1")
    ols_fit = ols(formula, data=updated_sim_data).fit()
    ols_summary = ols_fit.summary()
    # YOUR CODE ENDS HERE
    return ols_summary

  def part_g3(self) -> statsmodels.iolib.summary.Summary:
    """
    Use the statsmodels ols() function to perform a multiple linear regression with y
    as the response and x2 as the predictors on the updated data. Return the
    results using the summary() method. Comment on the output.

    Returns:
      A statsmodels Summary object, containing the summary results of the ols
      fit.
    """
    extra_obs = pd.DataFrame({"x1": [0.1], "x2":[0.8], "y": [6]})
    updated_sim_data = self.sim_data.append(extra_obs)
    # YOUR CODE STARTS HERE
    formula = ("y ~ x2")
    ols_fit = ols(formula, data=updated_sim_data).fit()
    ols_summary = ols_fit.summary()
    # YOUR CODE ENDS HERE
    return ols_summary

def ch3_ex14():
  """Wrapper function for Chapter 3, Exercise 14."""
  logging.info("Chapter 3, Exercise 14.")
  sim = Simulation()

  logging.info("\tPart b.")
  corr = sim.part_b1()
  with open("../results/python/ch3_ex14_part_b1.csv", "w") as f:
    f.write(str(corr))

  sim.part_b2()
  plt.savefig("../results/python/ch3_ex14_part_b2.png")

  logging.info("\tPart c.")
  ols = sim.part_c()
  with open("../results/python/ch3_ex14_part_c.csv", "w") as f:
    f.write(ols.as_text())

  logging.info("\tPart d.")
  ols = sim.part_d()
  with open("../results/python/ch3_ex14_part_d.csv", "w") as f:
    f.write(ols.as_text())

  logging.info("\tPart e.")
  ols = sim.part_e()
  with open("../results/python/ch3_ex14_part_e.csv", "w") as f:
    f.write(ols.as_text())

  logging.info("\tPart g.")
  ols = sim.part_g1()
  with open("../results/python/ch3_ex14_part_g1.csv", "w") as f:
    f.write(ols.as_text())
  ols = sim.part_g2()
  with open("../results/python/ch3_ex14_part_g2.csv", "w") as f:
    f.write(ols.as_text())
  ols = sim.part_g3()
  with open("../results/python/ch3_ex14_part_g3.csv", "w") as f:
    f.write(ols.as_text())

