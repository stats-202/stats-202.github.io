#!Rscript

suppressPackageStartupMessages({
  library(logging)
})


main <- function() {
  stopifnot(file.exists("../results"))
  stopifnot(file.exists("../data"))

  source("./questions/ch3_ex9.R")
  Ch3Ex9()

  source("./questions/ch3_ex14.R")
  Ch3Ex14()

  source("./questions/ch10_ex9.R")
  Ch10Ex9()

  loginfo("Run successful. Shutting down...")
  return (0)
}

foo = main()
stopifnot(foo == 0)