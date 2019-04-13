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

# Get metadata table
index <- getTable('tables_index')

# Select ready for triage
scraped <- subset(index, state == states$SCRAPESUCCESS)

# Select table
triage <- scraped[complete.cases(scraped$table_name),][1,]
tableRowToTriage <- triage$table_name
table <- getTable(tableRowToTriage)

# Run K-anon or something
result <- Kanon(table) 
if (result > minimumKValue) {
  state <- states$TRIAGESUCCESS
} else {
  state <- states$TRIAGEFAIL
}

# Set 
setTable(tableRowToTriage, state)

