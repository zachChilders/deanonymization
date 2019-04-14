minimumKValue <- 4 # This needs to be tuned.

# K-anonymity function to triage tables
# TODO: write this
Kanon <- function(table) {
    function [k, equivalence_classes] = kAnonymity_Analyze(data_table, quasi_identifiers)
    % Let's first get the unique rows when the table is projected only on
    % quasi identifiers. This will yield the equivalence classes as a data
    % table (and will return it as a second return value, if the function
    % call requested two return values)
    equivalence_classes = unique(data_table(:,quasi_identifiers), 'rows');
    % We will now augment this table with a new column, called "k" that
    % counts for each equivalence class, the number of rows in the original
    % table "data_table" that belong to that equivalence class.
    equivalence_classes.k(:) = NaN;
    for eqv_class_id = 1:size(equivalence_classes, 1)
        % these are the values of the qids for the equivalence class
        eqv_class = equivalence_classes{eqv_class_id,quasi_identifiers};
        
        table = ones;
        i = 1;
        for attribute = quasi_identifiers
           col = table2array(data_table(:, attribute));
           bool = col == eqv_class(i);
           table = table .* bool;
           i = i+1;
        end
            
        equivalence_classes.k(eqv_class_id) = sum(table); 
    end
    % The k in k-Anonymity is the size of the smallest equivalence class.
    % TODO: complete this code to assign the return value k
    k = min(equivalence_classes.k); % TODO: fill this here
end
    
    
    
    
    
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
# setTable(tableRowToTriage, state)   // uncomment later, when zach says its ok

