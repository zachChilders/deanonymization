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

### Data Processing

We need two notebooks minimum.  One is for analyzing the datasets and finding weaknesses.  The other is for performing attacks.  We may consider additionally having a notebook for data cleaning, and additional notebooks for targeting specific weaknesses (seperate diversity attacks, for instance).

### Egress

We need to output the data in some consumable format for manual analysis.  This should probably be SQL or csv for convenience sake, but it doesn't matter too much what we pick.  Whatever selection we make, we should add metadata to it.  We need to know what datasets a table was produced from at a minimum.  

### Milestones

1. Data.gov scraper scraper complete
1. K-anonymity notebook complete
1. General graph output
1. Basic Triage functionality
1. More scrapers
1. Generalization Triage functionality
1. Pretty graphs