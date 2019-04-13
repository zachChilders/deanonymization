#Bootstrap deanonymize library
library('devtools')
if (!require('deanonymizeR')) {
    install_github('zachChilders/deanonymizeR')
    library('deanonymizeR')
}

index <- getTable('tables_index')
