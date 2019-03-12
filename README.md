# MICS 233 Privacy Engineering Implementation

## Deanonymization at Scale

We know that deanonymization of arbitrary datasets is possible.

### Ingress

Our ingress point is a lightweight data collection service.  It needs to suck up arbitrary amounts of data, ensure its formatted okay, and then stuff it into a drop location the Triage notebook can pick up.

[data.gov](https://www.data.gov/)

[Internet Archive](https://archive.org/web/)

[r/datasets](https://www.reddit.com/r/datasets/)

[GoogleData](https://toolbox.google.com/datasetsearch)

[BerkeleyData](https://dlab.berkeley.edu/data-resources/data)

We would essentially set up a script that finds csv dumps of data on the web.  The scraper would download those csvs and create a postgresql table from the data.  It would then inform the indexer that the table has added and what type of data it is.  We will end up with many tables in the database.  Our deanonmyzing algorithm will then look through the tables and deanonymize certain data creating new tables.  

### Data Processing

We need two notebooks minimum.  One is for analyzing the datasets and finding weaknesses.  The other is for performing attacks.  We may consider additionally having a notebook for data cleaning, and additional notebooks for targeting specific weaknesses (seperate diversity attacks, for instance).

### Egress

We need to output the data in some consumable format for manual analysis.  This should probably be SQL or csv for convenience sake, but it doesn't matter too much what we pick.  Whatever selection we make, we should add metadata to it.  We need to know what datasets a table was produced from at a minimum.  

### Milestones

1. Data.gov scraper scraper complete
1. K-anonymity notebook complete
1. General graph output
1. Basic Triage functionality
1. Dataset deep dive
1. More scrapers
1. Generalization Triage functionality
1. Pretty graphs

### Contributions

 - Aaron will
 - Cameron will handle ingress & help with data deanon implementation
 - Zach will
 