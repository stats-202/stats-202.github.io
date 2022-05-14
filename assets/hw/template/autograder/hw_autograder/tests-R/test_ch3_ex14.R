library(testthat)

source("../R/questions/ch3_ex14.R")

# Load data
sim_data = LoadData(verbose=FALSE)

test_that("3.14.b: Scatter plot.", {
  foo <- PartB1(sim_data)
  est_cor <- with(sim_data, cor(x1, x2))
  expect_equal(foo, est_cor, label="3.14.b.1: Correlation coefficient.")

  foo <- PartB2(sim_data)
  expect_true(dev.cur() == 2, label="3.14.b.2: Scatter plot.")
  foo <- dev.off()
})

test_that("3.14.c: Multiple linear regression.", {
  foo <- PartC(sim_data)
  fit_1 <- lm(y ~ x1 + x2, data=sim_data)
  lm_summary <- summary(fit_1)
  expect_true(inherits(foo, "summary.lm"), label="Check is a summary.lm.")
  expect_equal(foo$coefficients, lm_summary$coefficients,
               label="Check equals solution.")
})

test_that("3.14.d: x1 simple linear regression.", {
  foo <- PartD(sim_data)
  fit_2 <- lm(y ~ x1, data=sim_data)
  lm_summary <- summary(fit_2)
  expect_true(inherits(foo, "summary.lm"), label="Check is a summary.lm.")
  expect_equal(foo$coefficients, lm_summary$coefficients,
               label="Check equals solution.")
})

test_that("3.14.e: x2 simple linear regression.", {
  foo <- PartE(sim_data)
  fit_3 <- lm(y ~ x2, data=sim_data)
  lm_summary <- summary(fit_3)
  expect_true(inherits(foo, "summary.lm"), label="Check is a summary.lm.")
  expect_equal(foo$coefficients, lm_summary$coefficients,
               label="Check equals solution.")
})

test_that("3.14.g.1: Multiple linear regression.", {
  foo <- PartG1(sim_data)
  extra_obs = c(0.1, 0.8, 6)
  updated_data_frame = rbind(sim_data, extra_obs)
  fit_1 <- lm(y ~ x1 + x2, data=updated_data_frame)
  lm_summary <- summary(fit_1)
  expect_true(inherits(foo, "summary.lm"), label="Check is a summary.lm.")
  expect_equal(foo$coefficients, lm_summary$coefficients,
               label="Check equals solution.")
})

test_that("3.14.g.2: x1 simple linear regression.", {
  foo <- PartG2(sim_data)
  extra_obs = c(0.1, 0.8, 6)
  updated_data_frame = rbind(sim_data, extra_obs)
  fit_2 <- lm(y ~ x1, data=updated_data_frame)
  lm_summary <- summary(fit_2)
  expect_true(inherits(foo, "summary.lm"), label="Check is a summary.lm.")
  expect_equal(foo$coefficients, lm_summary$coefficients,
               label="Check equals solution.")
})

test_that("3.14.g.3: x2 linear regression.", {
  foo <- PartG3(sim_data)
  extra_obs = c(0.1, 0.8, 6)
  updated_data_frame = rbind(sim_data, extra_obs)
  fit_3 <- lm(y ~ x2, data=updated_data_frame)
  lm_summary <- summary(fit_3)
  expect_true(inherits(foo, "summary.lm"), label="Check is a summary.lm.")
  expect_equal(foo$coefficients, lm_summary$coefficients,
               label="Check equals solution.")
})
