library(testthat)

source("../R/questions/ch10_ex9.R")

# Load data
us_arrests = LoadData(verbose=FALSE)

test_that("10.9.a: Dendogram.", {
  foo <- PartA(us_arrests)
  expect_true(dev.cur() == 2, label="Has active graphic device")
  foo <- dev.off()
})

test_that("10.9.b: Dendogram tree cut (3) groups.", {
  foo <- PartB(us_arrests)
  d <- dist(us_arrests, method="euclidean")
  h <- hclust(d, method="complete")
  tree_clusts <- cutree(h, 3)
  clusters <- list()
  for(i in 1:3) {
    clusters[[i]] = names(tree_clusts[tree_clusts==i])
  }
  expect_true(inherits(foo, "list"), label="Check is a list.")
  expect_equal(foo, clusters, label="Check equals solution.")
})

test_that("10.9.c: Dendogram with scaled features.", {
  foo <- PartC(us_arrests)
  expect_true(dev.cur() == 2, label="Has active graphic device")
  foo <- dev.off()
})