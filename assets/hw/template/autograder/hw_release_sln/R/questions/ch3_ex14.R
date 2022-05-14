# Chapter 3, Exercise 14.

suppressPackageStartupMessages({
  library(logging)
})

#' The width and height of exported plots.
FIGSIZE = c(1000, 1000)


#' Loads required data for exercise.
#'
#' @param data_path location of the data.
#' @return a data.frame containing the exercise data.
LoadData <- function(data_path ="../data/ch3_q14.csv", verbose=TRUE) {
  stopifnot(file.exists(data_path))
  if (verbose)
    loginfo(sprintf("\tLoading %s", data_path))
  sim_data <- read.csv(data_path)
  return (sim_data)
}


#' Using the cor() function, estimate the Pearson correlation
#' coefficient.
#'
#' @param data_frame a data.frame containing the Simulation data.
#' @return A numeric corresponding to the Pearson correlation.
PartB1 <- function(data_frame) {
  # YOUR CODE STARTS HERE
  est_cor <- with(data_frame, cor(x1, x2))
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (est_cor)
}


#' Return a scatter plot of x1 vs x2. Comment on what you see.
#'
#' @param data_frame a data.frame containing the Simulation data.
#' @return A matrix containing the pairwise correlation estimates.
PartB2 <- function(data_frame) {
  # YOUR CODE STARTS HERE
  figure <- with(data_frame, plot(x1 ~ x2))
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (figure)
}


#' Using the data, fit a least squares regression to predict y using
#' x1 and x2. Describe the results obtained.
#'
#' @param data_frame a data.frame containing the Simulation data.
#' @return A summary.lm object containing the summary of the regression.
PartC <- function(data_frame) {
  # YOUR CODE STARTS HERE
  fit_1 <- lm(y ~ x1 + x2, data=data_frame)
  lm_summary <- summary(fit_1)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (lm_summary)
}


#' Now fit a least squares regression to predict y using only x1.
#' Comment on your results.
#'
#' @param data_frame a data.frame containing the Simulation data.
#' @return A summary.lm object containing the summary of the regression.
PartD <- function(data_frame) {
  # YOUR CODE STARTS HERE
  fit_2 <- lm(y ~ x1, data=data_frame)
  lm_summary <- summary(fit_2)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE

  return (lm_summary)
}


#' Now fit a least squares regression to predict y using only x1.
#' Comment on your results.
#'
#' @param data_frame a data.frame containing the Simulation data.
#' @return A summary.lm object containing the summary of the regression.
PartE <- function(data_frame) {
  # YOUR CODE STARTS HERE
  fit_3 <- lm(y ~ x2, data=data_frame)
  lm_summary <- summary(fit_3)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (lm_summary)
}


#' Perform a multiple linear regression with y as the response and
#' x1, x2 as the predictors on the updated data. Return
#' the results using the summary() function Comment on the output.
#'
#' @param data_frame a data.frame containing the Simulation data.
#' @return A summary.lm object containing the summary of the regression.
PartG1 <- function(data_frame) {
  extra_obs = c(0.1, 0.8, 6)
  updated_data_frame = rbind(data_frame, extra_obs)
  # YOUR CODE STARTS HERE
  fit_1 <- lm(y ~ x1 + x2, data=updated_data_frame)
  lm_summary <- summary(fit_1)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (lm_summary)
}


#' Perform a multiple linear regression with y as the response and
#' x1 as the predictors on the updated data. Return
#' the results using the summary() function Comment on the output.
#'
#' @param data_frame a data.frame containing the Simulation data.
#' @return A summary.lm object containing the summary of the regression.
PartG2 <- function(data_frame) {
  extra_obs = c(0.1, 0.8, 6)
  updated_data_frame = rbind(data_frame, extra_obs)
  # YOUR CODE STARTS HERE
  fit_2 <- lm(y ~ x1, data=updated_data_frame)
  lm_summary <- summary(fit_2)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (lm_summary)
}


#' Perform a multiple linear regression with y as the response and
#' x2 as the predictors on the updated data. Return
#' the results using the summary() function Comment on the output.
#'
#' @param data_frame a data.frame containing the Simulation data.
#' @return A summary.lm object containing the summary of the regression.
PartG3 <- function(data_frame) {
  extra_obs = c(0.1, 0.8, 6)
  updated_data_frame = rbind(data_frame, extra_obs)
  # YOUR CODE STARTS HERE
  fit_3 <- lm(y ~ x2, data=updated_data_frame)
  lm_summary <- summary(fit_3)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (lm_summary)
}

#' Wrapper function for Chapter 3, Exercise 14.
Ch3Ex14 <- function() {
  loginfo("Chapter 3, Exercise 14.")
  sim_data = LoadData()

  loginfo("\tPart b.")
  corr = PartB1(sim_data)
  sink("../results/R/ch3_ex14_part_b1.csv")
  print(corr)
  sink()

  png("../results/R/ch3_ex14_part_b2.png", width=FIGSIZE[1], height=FIGSIZE[2])
  PartB2(sim_data)
  dev.off()

  loginfo("\tPart c.")
  ols = PartC(sim_data)
  sink("../results/R/ch3_ex14_part_c.csv")
  print(ols)
  sink()

  loginfo("\tPart d.")
  ols = PartD(sim_data)
  sink("../results/R/ch3_ex14_part_d.csv")
  print(ols)
  sink()

  loginfo("\tPart e.")
  ols = PartE(sim_data)
  sink("../results/R/ch3_ex14_part_e.csv")
  print(ols)
  sink()

  loginfo("\tPart g.")
  ols = PartG1(sim_data)
  sink("../results/R/ch3_ex14_part_g1.csv")
  print(ols)
  sink()

  ols = PartG2(sim_data)
  sink("../results/R/ch3_ex14_part_g2.csv")
  print(ols)
  sink()

  ols = PartG3(sim_data)
  sink("../results/R/ch3_ex14_part_g3.csv")
  print(ols)
  sink()
}
