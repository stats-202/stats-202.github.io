# Chapter 10, Exercise 9.

suppressPackageStartupMessages({
  library(logging)
})

#' The width and height of exported plots.
FIGSIZE = c(1000, 1000)


#' Loads required data for exercise.
#'
#' @param data_path location of the data.
#' @return a data.frame containing the exercise data.
LoadData <- function(data_path="../data/USArrests.csv", verbose=TRUE) {
  stopifnot(file.exists(data_path))
  if (verbose)
    loginfo(sprintf("\tLoading %s", data_path))
  us_arrests <- read.csv(data_path)
  rownames(us_arrests) <- us_arrests$X
  us_arrests$X <- NULL
  return (us_arrests)
}


#' Using hierarchical clustering with complete linkage and
#' Euclidean distance, cluster the states.
#'
#' @param data_frame a data.frame containing the US arrests data.
#' @return The dendogram plot.
PartA <- function(data_frame) {
  # YOUR CODE STARTS HERE
  d <- dist(data_frame, method="euclidean")
  h <- hclust(d, method="complete")
  fig <- plot(h)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (fig)
}


#' Cut the dendrogram at a height that results in three distinct
#' clusters. Which states belong to which clusters?
#'
#' n.b. You'll need to refit the cluster from Part A to complete this part.
#'
#' @param data_frame a data.frame containing the US arrests data.
#' @return A list containing a vector of state names for each cluster.
PartB <- function(data_frame) {
  # YOUR CODE STARTS HERE
  d <- dist(data_frame, method="euclidean")
  h <- hclust(d, method="complete")
  tree_clusts <- cutree(h, 3)
  clusters <- list()
  for(i in 1:3) {
    clusters[[i]] = names(tree_clusts[tree_clusts==i])
  }
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (clusters)
}


#' Hierarchically cluster the states using complete linkage and Euclidean
#' distance, after scaling the variables to have standard de- viation one.
#'
#' @param data_frame a data.frame containing the US arrests data.
#' @return The dendogram plot.
PartC <- function(data_frame) {
  # YOUR CODE STARTS HERE
  d <- dist(scale(data_frame), method="euclidean")
  h <- hclust(d, method="complete")
  fig <- plot(h)
  # stop("NotImplementedError")
  # YOUR CODE ENDS HERE
  return (fig)
}


#' Wrapper function for Chapter 3, Exercise 9.
Ch10Ex9 <- function() {
  loginfo("Chapter 10, Exercise 9.")
  us_arrests = LoadData()

  loginfo("\tPart a.")
  png("../results/R/ch10_ex9_part_a.png", width=FIGSIZE[1], height=FIGSIZE[2])
  PartA(us_arrests)
  dev.off()

  loginfo("\tPart b.")
  groups = PartB(us_arrests)
  sink("../results/R/ch10_ex9_part_b.csv")
  for (i in c(1:length(groups))) {
    print(paste0("Group ", i, ":"))
    print(paste(groups[[i]], collapse = ','))
    cat('\n')
  }
  sink()

  loginfo("\tPart c.")
  png("../results/R/ch10_ex9_part_c.png", width=FIGSIZE[1], height=FIGSIZE[2])
  PartC(us_arrests)
  dev.off()
}
