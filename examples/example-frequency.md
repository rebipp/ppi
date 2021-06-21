# Dataset Example (Frequency)

An example of dataset with visitation frequency [example-frequency](/examples/example-frequency.csv).

Since we don't have any metadata associated with this example, the exact meaning of the fields can't be determined. 

So, we are assuming the follow defintions for the fields *Numero de flores* (number of flowers) and *Frequencia* (frequency):
- **Numero de flores** (number of flowers): the number of flowers of a plant which are observed for floral visitors (to record interactions)
- **Frequencia** (frequency): the number of visits per observed flower

## Original Data

Sitio | Parcela | Data | ID | Especie | Numero de flores | Altura | X | Angulo |Y |Interacao | Horario | Frequencia | Comportamento beija-flor
-- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
Modulo Cachoeira | 3 | 11/5/2014 | 24928 | Nidularium innocentii | 1 | 1.4 | 2.2| NA| 8.25 | Ramphodon naevius | 11:45| 4| Trapliner
Modulo Cachoeira | 7 | 11/6/2014 | 24946 | Nidularium innocentii | 1 | 5 | 104.5 | NA | 7.28 | Ramphodon naevius | 11:44 | 1 | Trapliner
Modulo Cachoeira | 7 | 11/6/2014 | 24947 | Nidularium innocentii | 2 | 1.58 | 198.2 | NA | 6.5 | Thalurania glaucopis | NA | 1 | Trapliner
Modulo Cachoeira | 7 | 11/6/2014 | 24948 | Nidularium innocentii | 1 | 3.2 | 247.54 | NA | NA | Thalurania glaucopis | NA | 1 | Trapliner

## Standadized Data

**Event Core** (*interactions.csv*):

eventID | eventDate | fieldNumber
-- | -- | -- 
evt_1 | 2014-05-11T11:45-0300 | 24928
evt_2 | 2014-06-11T11:44-0300 | 24946
evt_3 | 2014-06-11 | 24947
evt_4 | 2014-06-11 | 24948

**Occurrences** (*occurrences.csv*):

eventID | occurrenceID | scientificName | taxonRank | behavior | verbatimLocality
-- | -- | -- | -- | -- | --
evt_1 | occ_1 | Nidularium innocentii | species | | Modulo Cachoeira Parcela 3
evt_1 | occ_2 | Ramphodon naevius | species | trapliner | Modulo Cachoeira Parcela 3
evt_2 | occ_3 | Nidularium innocentii | species | | Modulo Cachoeira Parcela 7
evt_2 | occ_4 | Ramphodon naevius | species | trapliner | Modulo Cachoeira Parcela 3
evt_3 | occ_5 | Nidularium innocentii | species | | Modulo Cachoeira Parcela 7
evt_3 | occ_6 | Ramphodon naevius | species | trapliner | Modulo Cachoeira Parcela 3
evt_4 | occ_7 | Nidularium innocentii | species | | Modulo Cachoeira Parcela 7
evt_4 | occ_8 | Ramphodon naevius | species | trapliner | Modulo Cachoeira Parcela 3

**ResourceRelationship Extension** (*resourcerealtionship.csv*):

eventID | resourceRelationshipID | resourceID | relatedResourceID | relationshipOfResource | relationshipEstablishedDate
-- | -- | -- | -- | -- | -- 
evt_1 | rr_1 | occ_1 | occ_2 | flowersVisitedBy | 2014-05-11T11:45-0300
evt_2 | rr_2 | occ_3 | occ_4 | flowersVisitedBy | 2014-06-11T11:44-0300
evt_3 | rr_3 | occ_5 | occ_6 | flowersVisitedBy | 2014-06-11
evt_4 | rr_4 | occ_7 | occ_8 | flowersVisitedBy | 2014-06-11 

**MeasurementOrFact Extension** (*measurements.csv*):

eventID | measurementID | measurementType | measurementValue | measurementUnit 
-- | -- | -- | -- | --
evt_1 | m_1 | flowersVisitedQuantity | 4 | flowers
evt_2 | m_2 | flowersVisitedQuantity | 1 | flowers
evt_3 | m_3 | flowersVisitedQuantity | 1 | flowers
evt_4 | m_4 | flowersVisitedQuantity | 1 | flowers

**Obs:**: the `measurementType` (*flowersVisisedQuantity*) reflects the frequency of an interaction (the number of flowers visited by an animal). The term `flowersVisitedQuantity` is marked as **`removed`** but it is used here as an example of how to use `MeasurementOrFact` extension.
