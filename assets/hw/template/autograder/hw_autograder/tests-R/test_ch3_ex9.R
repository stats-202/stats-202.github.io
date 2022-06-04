library(testthat)

source("../R/questions/ch3_ex9.R")

# Load data
auto = LoadData(verbose=FALSE)

test_that("3.9.a: Scatter plot matrix size.", {
  foo <- PartA(auto)
  expect_true(dev.cur() == 2, label="Has active graphic device")
  foo <- dev.off()
})

test_that("3.9.b: Correlation matrix.", {
  foo <- PartB(auto)
  auto_tmp <- auto
  auto_tmp$name <- auto_tmp$origin <- NULL
  correlation = cor(auto_tmp)
  expect_true(inherits(foo, "matrix"), label="Check is a matrix.")
  expect_equal(foo, correlation, label="Check equals solution.")
})

test_that("3.9.c: Multiple linear regression.", {
  foo <- PartC(auto)
  lm_fit <- lm(mpg ~ . - name, data=auto)
  lm_summary <- summary(lm_fit)
  expect_true(inherits(foo, "summary.lm"), label="Check is a summary.lm.")
  expect_equal(foo$coefficients, lm_summary$coefficients,
               label="Check equals solution.")
})

test_that("3.9.d: lm summary plots.", {
  foo <- PartD(auto)
  expect_true(dev.cur() == 2, label="Has active graphic device")
  foo <- dev.off()
})

test_that("3.9.e: Custom (interactions) multiple linear regression.", {
  foo <- PartE(auto)
  expect_true(inherits(foo, "summary.lm"), label="Is a summary.lm")
})

test_that("3.9.f: Custom (transformations) multiple linear regression.", {
  foo <- PartF(auto)
  expect_true(inherits(foo, "summary.lm"), label="Is a summary.lm")
})
