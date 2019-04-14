#Bootstrap deanonymize library
library('devtools')
if (!require('deanonymizeR')) {
    install_github('zachChilders/deanonymizeR')
    library('deanonymizeR')
}

# Get metadata table
index <- getTable('tables_index')
cleanIndex <- index[complete.cases(index$table_name),]
candidateTables <- subset(cleanIndex, state == stats$TRIAGESUCCESS)

# Select random candidate table
randomTable <- candidateTables[sample(nrow(candidateTables), 1),]
tableRowToTriage <- randomTable$table_name

#Pull that table
table <- getTable(tableRowToTriage)

head(table)
