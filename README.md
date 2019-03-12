# MICS 233 Privacy Engineering Implementation

## Deanonymization at Scale

We are aware of multiple high profile papers in which allegedly anonymized datasets with lower $k$ values are deanonymized.  The process is very straightforward, consisting only of matching generalizations and performing 
the equivalent of a SQL inner join.  

Given the relative ease of attacking a dataset, we would like to design a system that automates deanonymization on a large scale.  This process consists of three primary stages that make up a typical big data pipeline:
- Ingress, in which anonymous data is collected from various sources
- Processing, in which data is selected and attacked
- Egress, in which we prepare the identified data for additional processing and interpretation.

### Ingress

Our ingress point is a lightweight data collection service.  It needs to suck up arbitrary amounts of data, ensure its formatted okay, and then stuff it into a drop location the Triage notebook can pick up.

[data.gov](https://www.data.gov/)

[Internet Archive](https://archive.org/web/)

[r/datasets](https://www.reddit.com/r/datasets/)

[GoogleData](https://toolbox.google.com/datasetsearch)

[BerkeleyData](https://dlab.berkeley.edu/data-resources/data)

We will set up a script that finds csv dumps of data on the web.  The scraper would download those csvs and create a postgresql table from the data.  It would then inform the indexer that the table has added and what type of data it is.  We will end up with many tables in the database.  Our deanonmyzing algorithm will then look through the tables and deanonymize certain data creating new tables.  

### Data Processing

We would like to use Jupyter notebooks in light of having access to the MIDS instance.  We intend to implement them offline in R and then upload them to the cluster where they will have knowledge of the ingress.
We need three notebooks minimum:
- Triage for analyzing the datasets and finding weaknesses.
- Generalization for attempting generalization matches.
- Attack for actually performing joins and other deanons.

We may consider additionally having a notebook for more serious data cleaning, and additional notebooks for targeting specific weaknesses (seperate diversity attacks, for instance).

### Egress

We intend to reuse the Postgres DB from the Ingress. We need to add some sort of metadata, perhaps by table naming convention, in order to keep track of what attack was performed and with what datasets.

### Milestones

1. Data.gov scraper scraper complete
1. K-anonymity notebook complete
1. General graph output
1. Basic Triage functionality
1. Dataset deep dive
1. More scrapers
1. Generalization Triage functionality
1. Pretty graphs

### 

### Contributions

 - Aaron will take lead on workbook implementation.
 - Cameron will handle ingress & help with data deanon implementation
 - Zach will 
 