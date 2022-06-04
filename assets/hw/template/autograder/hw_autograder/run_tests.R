library(RJSONIO)
library(testthat)

# n.b. testthat changes the cwd to 'tests-R'
test_results = test_dir('tests-R', reporter=SilentReporter)

# Processes results
check_proportion_correct <- function(x) {
  successes <- lapply(
    x$results, function(y) return(class(y)[1] == "expectation_success"))
  return (mean(do.call("c", successes)))
}
n_tests <- length(test_results)
test_scores <- vector(mode="list", length=n_tests)
for (i in c(1:n_tests)) {
  result <- test_results[[i]]
  score <- list()
  score["name"] <- result$test
  score["percent"] <- check_proportion_correct(result)
  test_scores[[i]] <- score
}

# n.b. We only record the proportion of correct here.
#      Will calculate the actual score using the weights from the python run
exportJson <- toJSON(list(tests=test_scores))
cat(exportJson)
