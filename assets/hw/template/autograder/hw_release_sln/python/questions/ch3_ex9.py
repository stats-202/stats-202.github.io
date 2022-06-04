import os
from typing import Text, Tuple
import warnings

from absl import logging
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import OLSInfluence

# scatter_matrix uses deprecated matplotlib commands.
# ignoring for now while developers catch up.
warnings.filterwarnings("ignore")


class Auto(object):
  """Chapter 3, Exercise 9."""

  def __init__(self, data_path: Text="../data/Auto.csv",
               figsize: Tuple[int, int]=(10, 10)):
    """Constructor.

    Attributes:
      data_path: A str indicating the location of the data.
      figsize: A tuple specifying the default size for figures.
    """
    self.data_path = data_path
    assert os.path.exists(self.data_path), "Auto dataset not found."
    logging.info("\tLoading %s", self.data_path)
    self.auto = pd.read_csv(self.data_path)
    self.auto.set_index("name", inplace=True)
    self.auto["origin"] = self.auto.origin.astype(str)
    self.figsize = figsize

  def part_a(self) -> np.ndarray:
    """
    Return a scatterplot matrix which includes all of the variables in the
    data set using the function scatter_matrix() on the 'Auto' data set.

    Returns:
      A matrix of scatter plots.
    """
    # YOUR CODE STARTS HERE
    fig = scatter_matrix(self.auto, figsize=self.figsize)
    # raise NotImplementedError
    # YOUR CODE ENDS HERE
    return fig

  def part_b(self) -> pd.DataFrame:
    """
    Returns the matrix of correlations between the variables using the pandas
    function corr().

    Returns:
      A pd.DataFrame containing the correlation matrix.
    """
    # YOUR CODE STARTS HERE
    # raise NotImplementedError
    corr_matrix = self.auto.corr()
    # YOUR CODE ENDS HERE
    return corr_matrix

  def part_c(self) -> statsmodels.iolib.summary.Summary:
    """
    Use the statsmodels ols() function to perform a multiple linear regression with mpg
    as the response and all other variables except name as the predictors.
    Return the results using the summary() method. Comment on the output.

    n.b. To reuse the ols fit results in subsequent questions, please save
    the ols fit as an attribute, i.e. self.ols_fit = ...

    Returns:
      A statsmodels Summary object, containing the summary results of the ols
      fit.
    """
    # YOUR CODE STARTS HERE
    # raise NotImplementedError
    formula = ("mpg ~ cylinders + displacement + horsepower + weight "
               "+ acceleration + year + origin")
    self.ols_fit = ols(formula, data=self.auto).fit()
    ols_summary = self.ols_fit.summary()
    # YOUR CODE ENDS HERE
    return ols_summary

  def part_d1(self) -> matplotlib.collections.PathCollection:
    """
    Use the scatter() method from matplotlib to return a scatter plot of the
    fitted values vs residuals. Comment on what you see.

    Returns:
      A matplotlib.collections.PathCollection object containing the scatter plot.
    """
    # YOUR CODE STARTS HERE
    # raise NotImplementedError
    if not hasattr(self, 'ols_fit'):
      raise ValueError("ols_fit not found")
    _, ax = plt.subplots(figsize=self.figsize)
    ax.set_xlabel("Fitted values")
    ax.set_ylabel("Residuals")
    figure = ax.scatter(self.ols_fit.fittedvalues, self.ols_fit.resid)
    # YOUR CODE ENDS HERE
    return figure

  def part_d2(self) -> matplotlib.figure.Figure:
    """
    Use the sm.qqplot() method to return a Q-Q plot of the studentized
    residuals. Comment on what you see.

    Returns:
       A matplotlib.figure.Figure object containing the plot.
    """
    # YOUR CODE STARTS HERE
    # raise NotImplementedError
    if not hasattr(self, 'ols_fit'):
      raise ValueError("ols_fit not found")
    outliers_influence = OLSInfluence(self.ols_fit)
    figure = sm.qqplot(outliers_influence.get_resid_studentized_external())
    # YOUR CODE ENDS HERE
    return figure

  def part_d3(self) -> matplotlib.collections.PathCollection:
    """
    Use the scatter() method from matplotlib to return a plot of
    the sqrt(|studentized residuals|) vs fitted values. Comment
    on what you see.

    Returns:
      A matplotlib.collections.PathCollection object containing the plot.
    """
    # YOUR CODE STARTS HERE
    # raise NotImplementedError
    if not hasattr(self, 'ols_fit'):
      raise ValueError("ols_fit not found")
    outliers_influence = OLSInfluence(self.ols_fit)
    _, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlabel("Fitted values")
    ax.set_ylabel("sqrt(studentized residuals)")
    figure = ax.scatter(
        self.ols_fit.fittedvalues,
        outliers_influence.get_resid_studentized_external().apply(
            lambda x: np.sqrt(abs(x))))
    # YOUR CODE ENDS HERE
    return figure

  def part_d4(self) -> matplotlib.figure.Figure:
    """
    Use the sm.graphics.influence_plot() method to return a plot
    of the studentized residuals vs leverage values. Comment on
    what you see.

    Returns:
      A matplotlib.figure.Figure object containing the plot.
    """
    # YOUR CODE STARTS HERE
    # raise NotImplementedError
    if not hasattr(self, 'ols_fit'):
      raise ValueError("ols_fit not found")
    _, ax = plt.subplots(figsize=(10,8))
    figure = sm.graphics.influence_plot(self.ols_fit, ax=ax)
    # YOUR CODE ENDS HERE
    return figure

  def part_e(self) -> statsmodels.iolib.summary.Summary:
    """
    Use the * and : symbols to fit linear regression models with some
    interaction effects. Do any interactions appear to be statistically
    significant? Similar to part c, return the fit summary.

    Returns:
      A statsmodels Summary object, containing the summary results of the ols
      fit.
    """
    # YOUR CODE STARTS HERE
    # raise NotImplementedError
    formula = ("mpg ~ cylinders + displacement + horsepower + weight "
               "+ acceleration*year*origin")
    self.ols_fit2 = ols(formula, data=self.auto).fit()
    ols_summary = self.ols_fit2.summary()
    # YOUR CODE ENDS HERE
    return ols_summary

  def part_f(self) -> statsmodels.iolib.summary.Summary:
    """
    Try a few different transformations of the variables, such as
    log(X), \\sqrt{X}, X^2. Comment on your findings. Similar to part c, return
    the fit summary.

    Returns:
      A statsmodels Summary object, containing the summary results of the ols
      fit.
    """
    # YOUR CODE STARTS HERE
    # raise NotImplementedError
    self.auto["displacement_sq"] = self.auto.displacement**2
    self.auto["log_year"] = self.auto.year.apply(np.log)
    formula = ("mpg ~ cylinders + displacement + horsepower + weight "
               "+ acceleration + year + origin + displacement_sq + log_year")
    self.ols_fit3 = ols(formula, data=self.auto).fit()
    ols_summary = self.ols_fit3.summary()
    # YOUR CODE ENDS HERE
    return ols_summary


def ch3_ex9():
  """Wrapper function for Chapter 3, Exercise 9."""
  logging.info("Chapter 3, Exercise 9.")
  auto = Auto()

  logging.info("\tPart a.")
  auto.part_a()
  plt.savefig("../results/python/ch3_ex9_part_a.png")

  logging.info("\tPart b.")
  corr = auto.part_b()
  corr.to_csv("../results/python/ch3_ex9_part_b.csv")

  logging.info("\tPart c.")
  ols = auto.part_c()
  with open("../results/python/ch3_ex9_part_c.csv", "w") as f:
    f.write(ols.as_text())

  logging.info("\tPart d.")
  auto.part_d1()
  plt.savefig("../results/python/ch3_ex9_part_d1.png")
  auto.part_d2()
  plt.savefig("../results/python/ch3_ex9_part_d2.png")
  auto.part_d3()
  plt.savefig("../results/python/ch3_ex9_part_d3.png")
  auto.part_d4()
  plt.savefig("../results/python/ch3_ex9_part_d4.png")

  logging.info("\tPart e.")
  ols2 = auto.part_e()
  with open("../results/python/ch3_ex9_part_e.csv", "w") as f:
    f.write(ols2.as_text())

  logging.info("\tPart f.")
  ols3 = auto.part_f()
  with open("../results/python/ch3_ex9_part_f.csv", "w") as f:
    f.write(ols3.as_text())
