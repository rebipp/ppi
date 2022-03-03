# Darwin Core XML guide

Title
: Plant-Pollinator Interactions Vocabulary XML guide

Date version issued
: 2021-12-03

Date created
: 2021-12-03

Part of Standard
: <http://www.rebipp.org.br/standards/ppi/>

This version
: <http://rs.rebipp.org.br/ppi/terms/guides/xml/2021-12-03>

Latest version
: <http://rs.rebipp.org.br/ppi/terms/guides/xml>

Previous version
: <http://rs.rebipp.org.br/ppi/terms/guides/xml/2021-12-03>

Abstract
: Guidelines for implementing Plant-Pollinator Interactions in XML.

Contributors
: Jose A Salim (Universidade de São Paulo), Paula Zermoglio (Universidad de Buenos Aires), Debora P Drucker (Embrapa Agricultura Digital), Filipi Soares (Universidade de São Paulo), Antonio M Saraiva (Universidade de São Paulo)

Creator
: REBIPP Maintenance Group

Bibliographic citation
: REBIPP Maintenance Group. 2021. Plant-Pollinator Interactions XML guide. Brazilian Network on Plant-Pollinator Interactions (REBIPP). <http://rs.rebipp.org.br/ppi/terms/guides/xml/2021-12-03>

## 1 Introduction

This document provides guidelines for implementing application schemas based on [PPI terms]((http://rs.rebipp.org.br/ppi/terms)) and [Darwin Core terms](../../terms/) using [XML](http://www.w3.org/XML/). The underlying metadata model is described (in a syntax neutral way), followed by some specific guidelines for XML implementations.

This document does not provide guidelines for encoding Plant-Pollinator Interactions data in RDF/XML. Nor does it take a position on the relative merits of encoding metadata in "plain" XML rather than RDF/XML. This document provides guidelines in those cases where RDF/XML is not considered appropriate.

### 1.1 Status of the content of this document

All sections of this document are normative, except for sections that are explicitly marked as non-normative.

#### 1.1.1 RFC 2119 key words

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.2 Audience

This document is targeted toward those who wish to use or construct application schemas using PPI terms in XML. It includes explanations of existing schemas and how to build new schemas to meet specific models of information.

## 2 Implementation guide

### 2.1 XML schema

Implementors SHOULD base their XML applications on [XML Schemas](http://www.w3.org/XML/Schema) rather than _XML DTDs_. Approaches based on _XML Schemas_ are more flexible and are more easily re-used within other XML applications.

### 2.2 XML namespaces

Implementors MUST use [XML Namespaces](http://www.w3.org/TR/1999/REC-xml-names-19990114/) to uniquely identify elements. Plant-Pollinator Interactions Vocabulary namespaces are defined in the [Plant-Pollinator Interactions vocabulary namespace policy](../../namespace/), the Darwin Core namespaces are defined in the [Darwin Core Namespace Policy](https://dwc.tdwg.org/namespace/), while Dublin Core namespaces are defined in the [DCMI Namespace Recommendation](http://dublincore.org/documents/dcmi-namespace/).

### 2.3 Abstract model

The Darwin Core follows the [Dublin Core Metadata Initiative Abstract Model](http://dublincore.org/documents/abstract-model/) except that the Darwin Core _record_ is roughly equivalent to the Dublin Core _resource_.

- Darwin Core terms MUST be either `classes` or `properties`.
- A `Darwin Core record` MUST be made up of zero or more `classes` and one or more `properties` with their associated `values`.
- Each `value` MUST be a literal string.
- The `values` of `properties` within a `Darwin Core record` describe that record.
- A `Darwin Core record` MUST include all required `properties`, if any, and their associated `values`.
- Plant-Pollinator Interactions Vocabulary terms MUST be used as controlled vocabulary for `dwc:measurementType` term.
- Plant-Pollinator Interactions Controlled Vocabulary terms MUST be used as controlled vocabulary for `dwc:measurementValue` when appropriated.

### 2.4 Properties and values

Plant-Pollinator Interactions schema follows the guidelines for expressing [Dublin Core metadata using XML](http://dublincore.org/documents/dc-xml/) except in that implementors MUST encode `properties` as XML elements and `values` as the content of those elements instead of having each property contain a value representation and its associated value. The name of the XML element MUST be an XML qualified name (QName), which associates the value given in the `Term name` attribute in the [Darwin Core Terms](https://dwc.tdwg.org/list/) recommendation with the appropriate namespace name. For example, use:

```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
    targetNamespace="http://rs.tdwg.org/dwc/terms/"
    xmlns:dwc="http://rs.tdwg.org/dwc/terms/"
    xmlns:ppi="https://rs.rebipp.org.br/ppi/terms/">
...
<dwc:measurementType>ppi:resourceCollected</dwc:measurementType>
```

rather than:

```xml
<dwc:measurementType value="ppi:resourceCollected"/>
```

### 2.5 Null values

Elements for which the value is null SHOULD be omitted from the document or explicitly coded using the attribute `xsi:nil="true"`.

```xml
<dwc:measurementValue xsi:nil="true"/>
```

An empty string - an element with no content - MUST NOT be used:

```xml
<dwc:measurementValue></dwc:measurementValue>
```

#### 2.6 Examples (non-normative)

Following is an example of using a normalized class-based schema to represent a interaction of two specimen occurrences from one interaction Event. In this example a individual of *Euterpe edulis* was found to have flowers visited by a *Apis mellifera* individual. Note the reuse of class instances by referring to the identifiers declared in the instances of those classes:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<dwr:DarwinRecordSet xmlns:dwr="http://rs.tdwg.org/dwc/dwcrecord/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dwc="http://rs.tdwg.org/dwc/terms/" xmlns:ppi="https://rs.rebipp.org.br/ppi/terms/" xmlns:obis="http://rs.iobis.org/obis/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://rs.tdwg.org/dwc/dwcrecord/  http://rs.tdwg.org/dwc/xsd/tdwg_dwc_classes.xsd">
   <dwc:Occurrence>
      <dwc:occurrenceID>REBIPP:OCC:00101</dwc:occurrenceID>
      <dwc:basisOfRecord>HumanObservation</dwc:basisOfRecord>
      <dwc:recordedBy>Kayna Agostini</dwc:recordedBy>
      <dwc:eventID>REBIPP:PPI:0001</dwc:eventID>
   </dwc:Occurrence>
   <dwc:Occurrence>
      <dwc:occurrenceID>REBIPP:OCC:00102</dwc:occurrenceID>
      <dwc:basisOfRecord>HumanObservation</dwc:basisOfRecord>
      <dwc:recordedBy>Kayna Agostini</dwc:recordedBy>
      <dwc:eventID>REBIPP:PPI:0001</dwc:eventID>
   </dwc:Occurrence>
   <dwc:Event>
      <dwc:eventID>REBIPP:PPI:0001</dwc:eventID>
      <dwc:eventDate>2000-01-05</dwc:eventDate>
      <dwc:locationID>REBIPP:LOC:0001</dwc:locationID>
   </dwc:Event>
   <dcterms:Location>
      <dwc:locationID>REBIPP:LOC:0001</dwc:locationID>
      <dwc:country>Brazil</dwc:country>
      <dwc:countryCode>BR</dwc:countryCode>
      <dwc:decimalLatitude>-47.0680352</dwc:decimalLatitude>
      <dwc:decimalLongitude>-22.8261888</dwc:decimalLongitude>
   </dcterms:Location>
   <dwc:Identification>
      <dwc:identifiedBy>Kayna Agostini</dwc:identifiedBy>
      <dwc:dateIdentified>2000-01-05</dwc:dateIdentified>
      <dwc:occurrenceID>REBIPP:OCC:00101</dwc:occurrenceID>
      <dwc:taxonID>https://www.gbif.org/species/5293403</dwc:taxonID>
   </dwc:Identification>
   <dwc:Taxon>
      <dwc:taxonID>https://www.gbif.org/species/5293403</dwc:taxonID>
      <dwc:scientificName>Euterpe edulis Mart.</dwc:scientificName>
      <dwc:taxonRank>species</dwc:taxonRank>
      <dwc:genus>Euterpe</dwc:genus>
      <dwc:specificEpithet>edulis</dwc:specificEpithet>
   </dwc:Taxon>
   <dwc:Identification>
      <dwc:identifiedBy>Kayna Agostini</dwc:identifiedBy>
      <dwc:dateIdentified>2000-01-05</dwc:dateIdentified>
      <dwc:occurrenceID>REBIPP:OCC:00102</dwc:occurrenceID>
      <dwc:taxonID>https://www.gbif.org/species/1341976</dwc:taxonID>
   </dwc:Identification>
   <dwc:Taxon>
      <dwc:taxonID>https://www.gbif.org/species/1341976</dwc:taxonID>
      <dwc:scientificName>Apis mellifera (Linnaeus, 1758)</dwc:scientificName>
      <dwc:taxonRank>species</dwc:taxonRank>
      <dwc:genus>Apis</dwc:genus>
      <dwc:specificEpithet>mellifera</dwc:specificEpithet>
   </dwc:Taxon>

   <dwc:ResourceRelationship>
      <dwc:eventID>REBIPP:PPI:0001</dwc:eventID>
      <dwc:resourceID>REBIPP:OCC:00101</dwc:resourceID>
      <dwc:relationshipOfResource>has flowers visited bt</dwc:relationshipOfResource>
      <dwc:relationshipOfResourceID>http://purl.obolibrary.org/obo/RO_0002623</dwc:relationshipOfResourceID>
      <dwc:relatedResourceID>REBIPP:OCC:00102</dwc:relatedResourceID>
   </dwc:ResourceRelationship>

   <dwc:MeasurementOrFact>
      <dwc:measurementID>REBIPP:MOF:0001</dwc:measurementID>
      <dwc:eventID>REBIPP:PPI:00001</dwc:eventID>
      <dwc:measurementType>ppi:resourceCollected</dwc:measurementType>
      <dwc:measurementValue>pollen</dwc:measurementValue>
   </obis:ExtendedMeasurementOrFact>

  <obis:ExtendedMeasurementOrFact>
      <dwc:measurementID>REBIPP:MOF:0002</dwc:measurementID>
      <dwc:eventID>REBIPP:PPI:00001</dwc:eventID>
      <dwc:occurrenceID>REBIPP:OCC:00101</dwc:occurrenceID>
      <obis:measurementTypeID>http://rs.rebipp.org.br/ppi/terms/habit</obis:measurementTypeID>
      <dwc:measurementType>ppi:habit</dwc:measurementType>
      <obis:measurementValueID>http://purl.obolibrary.org/obo/FLOPO_0900033</obis:measurementValueID>
      <dwc:measurementValue>whole plant arborescent</dwc:measurementValue>
   </obis:ExtendedMeasurementOrFact>

   <obis:ExtendedMeasurementOrFact>
      <dwc:measurementID>REBIPP:MOF:0003</dwc:measurementID>
      <dwc:eventID>REBIPP:PPI:00001</dwc:eventID>
      <dwc:occurrenceID>REBIPP:OCC:00101</dwc:occurrenceID>
      <obis:measurementTypeID>http://rs.rebipp.org.br/ppi/terms/flowerLongevity</obis:measurementTypeID>
      <dwc:measurementType>ppi:flowerLongevity</dwc:measurementType>
      <dwc:measurementValue>168</dwc:measurementValue>
   </obis:ExtendedMeasurementOrFact>

   <obis:ExtendedMeasurementOrFact>
      <dwc:measurementID>REBIPP:MOF:0004</dwc:measurementID>
      <dwc:eventID>REBIPP:PPI:00001</dwc:eventID>
      <dwc:occurrenceID>REBIPP:OCC:00102</dwc:occurrenceID>
      <obis:measurementTypeID>http://rs.rebipp.org.br/ppi/terms/caste</obis:measurementTypeID>
      <dwc:measurementType>ppi:caste</dwc:measurementType>
      <dwc:measurementValue>worker</dwc:measurementValue>
   </obis:ExtendedMeasurementOrFact>
</dwr:DarwinRecordSet>```