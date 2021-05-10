# Dateset Example (Simple)

A very simple example of plant-pollinator interaction. The dataset [example-simple.csv](/examples/example-simple.csv) contains records of flower visitations.

## Original data

PLANT FAMILY | PLANT SPECIES | BEE FAMILY | BEE SPECIES | NUMBER | SEX | DATE | HOUR
-- | -- | -- | -- | -- | -- | -- | --
Amaranthaceae | Pfaffia tuberosa |Apidae | Ceratina asunciana | 44119 | M | 26/2/2003 | 12:00
Amaranthaceae	| Pfaffia tuberosa |Apidae | Ceratina asunciana | 44111 | M | 26/2/2003 | 11:55
Amaranthaceae	| Pfaffia tuberosa | Halictidae | Dialictus (Chloralictus) sp.9 | 43917 | M | 22/2/2003 | 13:38
Amaranthaceae	| Pfaffia tuberosa | Halictidae | Dialictus (Chloralictus) parvus | 43714 |F | 3/5/2003 | 15:40

## Standarized Data (Event-ResourceRealionship Model)

**Event Core** (*interaction.csv*):

eventID | fieldNumber | eventDate 
-- | -- | -- |
1 | 44119 | 2003-02-26T12:00-0300
2 | 44111 | 2003-02-26T11:55-0300
3 | 43917 | 2003-02-22T13:38-0300
4 | 43714 | 2003-05-03T15:40-0300

**Occurrences** (*occurrences.csv*):

eventID | occurrenceID | sex | family | genus | specificEpithet | scienticName | taxonRank | verbatimTaxonRank
-- | -- | -- | -- | -- | -- | -- | -- | -- 
1 | 1 | | Amaranthaceae | Pfaffia | tuberosa | Pfaffia tuberosa | species | Pfaffia tuberosa
1 | 2 | M | Apidae | Ceratina | asunciana | Ceratina asunciana | species | Ceratina asunciana
2 | 3 | | Amaranthaceae | Pfaffia | tuberosa | Pfaffia tuberosa | species | Pfaffia tuberosa
2 | 4 | M | Apidae | Ceratina | asunciana | Ceratina asunciana | species | Ceratina asunciana
3 | 5 | | Amaranthaceae | Pfaffia | tuberosa | Pfaffia tuberosa | species | Pfaffia tuberosa
3 | 6 | M | Halictidae | Dialictus | | Dialictus | genus | Dialictus (Chloralictys) sp.9
4 | 7 | | Amaranthaceae | Pfaffia | tuberosa | Pfaffia tuberosa | species | Pfaffia tuberosa
4 | 8 | F | Halictidae | Dialictus | parvus | Dialictus parvus | species | Dialictus (Chloralictys) parvus

**ResourceRelationship** (*resourcerelationship.csv*):

eventID | resourceRelationshipID | resourceID | relatedResourceID | relationshipOfResource | relationshipEstablishedDate
-- | -- | -- | -- | -- | -- 
1 | 1 | 1 | 2 | flowersVisitedBy | 2003-02-26T12:00-0300
2 | 2 | 3 | 4 | flowersVisitedBy | 2003-02-26T11:55-0300
3 | 3 | 5 | 6 | flowersVisitedBy | 2003-02-26T13:38-0300
4 | 4 | 7 | 8 | flowersVisitedBy | 2003-05-03T15:40-0300



