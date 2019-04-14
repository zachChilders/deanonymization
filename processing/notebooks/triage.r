minimumKValue <- 4 # This needs to be tuned.

# K-anonymity function to triage tables
# TODO: write this
Kanon <- function(table) {
  5
}

#Bootstrap deanonymize library
library('devtools')
if (!require('deanonymizeR')) {
    install_github('zachChilders/deanonymizeR')
    library('deanonymizeR')
}

# Select all tables in desiredState
index <- getTable('tables_index')
cleanIndex <- index[complete.cases(index$table_name),]
candidateTables <- subset(cleanIndex, state == stats$S)

# Select random candidate table
randomTable <- candidateTables[sample(nrow(candidateTables), 1),]
tableRowToTriage <- randomTable$table_name

#Pull that table
table <- getTable(tableRowToTriage)

# Run K-anon or something
result <- Kanon(table) 
if (result > minimumKValue) {
  state <- states$TRIAGESUCCESS
} else {
  state <- states$TRIAGEFAIL
}

# Set 
setTable(randomTable$id, state)

