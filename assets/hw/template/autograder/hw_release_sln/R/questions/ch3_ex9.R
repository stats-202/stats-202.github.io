# Chapter 3, Exercise 9.

suppressPackageStartupMessages({
  library(logging)
})

#' The width and height of exported plots.
FIGSIZE = c(1000, 1000)


#' Loads required data for exercise.
#'
#' @param data_path location of the data.
#' @return a data.frame containing the exercise data.
LoadData <- function(data_path ="../data/Auto.csv", verbose=TRUE) {
  stopifnot(file.exists(data_path))
  if (verbose)
    loginfo(sprintf("\tLoading %s", data_path))
  auto <- read.csv(data_path)
  auto$origin <- as.factor(auto$origin)
  return (auto)
}


#' Produce a scatterplot matrix which includes all of the
#' variables in the data set. Use the pairs() function.
#'
#' @param data_frame a data.frame containing the Auto data.
#' @return The scatter plot.
PartA <- function(data_frame) {
  # YOUR CODE STARTS HERE
  data_frame$name <- NULL
  data_frame$origin <- NULL
  fig <- pairs(data_frame)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (fig)
}


#' Compute the matrix of correlations between the variables using
#' the function cor(). You will need to exclude the name variable,
#' which is qualitative. Also exclude the origin variable.
#'
#' @param data_frame a data.frame containing the Auto data.
#' @return A matrix containing the pairwise correlation estimates.
PartB <- function(data_frame) {
  # YOUR CODE STARTS HERE
  data_frame$name <- NULL
  data_frame$origin <- NULL
  correlation = cor(data_frame)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (correlation)
}


#' Use the lm() function to perform a multiple linear regression with mpg
#' as the response and all other variables except name as the predictors.
#' Return the results using the summary() function Comment on the output.
#'
#' @param data_frame a data.frame containing the Auto data.
#' @return A summary.lm object containing the summary of the regression.
PartC <- function(data_frame) {
  # YOUR CODE STARTS HERE
  lm_fit <- lm(mpg ~ . - name, data=data_frame)
  lm_summary <- summary(lm_fit)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (lm_summary)
}


#' Use the plot() function to produce diagnostic plots of the linear
#' regression fit. Comment on any problems you see with the fit. Do the
#' residual plots suggest any unusually large outliers? Does the leverage
#' plot identify any observations with unusually high leverage?
#'
#' @param data_frame a data.frame containing the Auto data.
#' @return The regression plots.
PartD <- function(data_frame) {
  # YOUR CODE STARTS HERE
  lm_fit <- lm(mpg ~ . - name, data=data_frame)
  figure = plot(lm_fit)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE

  return (figure)
}


#' Use the * and : symbols to fit linear regression models with some
#' interaction effects. Do any interactions appear to be statistically
#' significant? Similar to part C, return the fit summary.
#'
#' @param data_frame a data.frame containing the Auto data.
#' @return A summary.lm object containing the summary of the regression.
PartE <- function(data_frame) {
  # YOUR CODE STARTS HERE
  data_frame$name <- NULL
  lm_fit <- lm(mpg ~ .*., data=data_frame)
  lm_summary <- summary(lm_fit)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (lm_summary)
}


#' Use the * and : symbols to fit linear regression models with some
#' interaction effects. Do any interactions appear to be statistically
#' significant? Similar to part C, return the fit summary.
#'
#' @param data_frame a data.frame containing the Auto data.
#' @return A summary.lm object containing the summary of the regression.
PartF <- function(data_frame) {
  # YOUR CODE STARTS HERE
  lm_fit_transformation <- lm(mpg ~ . - name + I(displacement^2) +
                              I(log(year)), data=data_frame)
  lm_summary <- summary(lm_fit_transformation)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (lm_summary)
}


#' Wrapper function for Chapter 3, Exercise 9.
Ch3Ex9 <- function() {
  loginfo("Chapter 3, Exercise 9.")
  auto = LoadData()

  loginfo("\tPart a.")
  png("../results/R/ch3_ex9_part_a.png", width=FIGSIZE[1], height=FIGSIZE[2])
  PartA(auto)
  dev.off()

  loginfo("\tPart b.")
  corr = PartB(auto)
  write.csv(corr, "../results/R/ch3_ex9_part_b.csv")

  loginfo("\tPart c.")
  ols = PartC(auto)
  sink("../results/R/ch3_ex9_part_c.csv")
  print(ols)
  sink()

  loginfo("\tPart d.")
  png("../results/R/ch3_ex9_part_d4.png", width=FIGSIZE[1], height=FIGSIZE[2])
  par(mfrow=c(2,2))
  PartD(auto)
  dev.off()

  loginfo("\tPart e.")
  ols = PartE(auto)
  sink("../results/R/ch3_ex9_part_e.csv")
  print(ols)
  sink()

  loginfo("\tPart f.")
  ols = PartF(auto)
  sink("../results/R/ch3_ex9_part_f.csv")
  print(ols)
  sink()
}
