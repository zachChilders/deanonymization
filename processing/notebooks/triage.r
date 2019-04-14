minimumKValue <- 4 # This needs to be tuned.

# K-anonymity function to triage tables
# TODO we are going to need qID to delcare equivalence classes
Kanon <- function(table, qID) {

  # get equivalence classes
  # table with just ec columns
  ec_cols <- table[,qID]

  # get equivalence classes
  ec <- unique(ec_cols)

  # set k
  k <- -1

  for (eq_id in 1:nrow(ec)) {
    count <- 0
    for (i in 1:nrow(table)) {
      if (table[i,qID] == ec[eq_id,]) {
        count <- count + 1
      }
    }

    if (count < k) {
      k <- count
    }
  }

  return k
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
# setTable(tableRowToTriage, state)   // uncomment later, when zach says its ok

