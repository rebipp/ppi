# Plant-Pollinator Interactions Vocabulary text guide

Title
: Plant-Pollinator Interactions Vocabulary text guide

Date version issued
: 2021-12-03

Date created
: 2021-12-03

Part of Standard
: <http://www.rebipp.org.br/standards/ppi/>

This version
: <http://rs.rebipp.org.br/ppi/terms/guides/text/2021-12-03>

Latest version
: <http://rs.rebipp.org.br/ppi/terms/guides/>

Previous version
: <http://rs.rebipp.org.br/ppi/terms/guides/text/2021-12-03>

Abstract
: Guidelines for implementing Plant-Pollinator Interactions in Text files.

Contributors
: Jose A Salim (USP), Paula Zermoglio (VertNet), Debora Drucker (Embrapa), Filipi Soares (USP), Antonio M Saraiva (USP), John Wieczorek (VertNet)

Creator
: REBIPP Maintenance Group

Bibliographic citation
: REBIPP Maintenance Group. 2021. Plant-Pollinator Interactions text guide. Brazilian Network on Plant-Pollinator Interactions (REBIPP). <http://rs.rebipp.org.br/ppi/terms/guides/text/2021-12-03>

## 1 Introduction

This document provides guidelines for formatting and sharing [PPI terms](http://rs.rebipp.org.br/ppi/terms) in _fielded text_ formats, such as one or more comma separated value (CSV) files. Data MAY be shared using an [XML](http://www.w3.org/XML/) metafile to describe its contents and formatting. A [Darwin Core Archive](https://ipt.gbif.org/manual/en/ipt/2.5/dwca-guide) is an example of an implementation of the Plant-Pollinator Interactions Text recommendation.

![Usage](usage.png)

More complex structure MAY be shared in multiple related files. The description of content and relationships between files can be achieved using the metafile. This guideline makes recommendations for the simple case of a _core_ file, upon which [Darwin Core](http://dwc.tdwg.org) [`dwc:Event`](http://rs.tdwg.org/dwc/terms/Event) class is used to represent an *interaction*, and multiple _extensions_, which are linked to records in that core file, documeting the occurrences of interacting organisms, their respective traits and the interactions outcomes. Specifically, extension records have a _many-to-one_ relationship with records in the core file. For example, a core file might contain interaction records, with one interaction per row in the file, while an extension file contains one or more traits or outcomes for those interactions, with one trait or outcome per row in the extension file, and with an identifier to the interaction for each trait or outcome row. This example would allow many traits or outcomes to be associated with each interaction.

### 1.1 Status of the content of this document

All sections of this document are normative, except for examples, whose sections are marked as non-normative.

#### 1.1.1 RFC 2119 key words

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.2 Simple example metafile content (non-normative)

A simple comma separated values (CSV) data file named interactions.csv with the following content:

```csv
ID, interactionDate, interactionTime, decimalLatitude, decimalLongitude, country
123, 2000-01-05, 15:13:00Z,-47.0680352, -22.8261888, Brazil
124, 2000-01-15, 09:32:00Z,-47.0680467, -22.8261789, Brazil
```

can be described with the following metafile:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<archive xmlns="http://rs.tdwg.org/dwc/text/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xsi:schemaLocation="http://rs.tdwg.org/dwc/text/ http://rs.tdwg.org/dwc/text/tdwg_dwc_text.xsd">

    <core encoding="UTF-8" fieldsTerminatedBy="," linesTerminatedBy="\n" ignoreHeaderLines="1" rowType="http://rs.tdwg.org/dwc/terms/Event">
        <files>
            <location>interactions.csv</location>
        </files>
        <id index="0" />
        <field index="0" term="http://rs.tdwg.org/dwc/terms/eventID" />
        <field index="1" term="http://rs.tdwg.org/dwc/terms/eventDate" />
        <field index="2" term="http://rs.tdwg.org/dwc/terms/eventTime"/>
        <field index="3" term="http://rs.tdwg.org/dwc/terms/decimalLatitude"/>
        <field index="4" term="http://rs.tdwg.org/dwc/terms/decimalLongitude"/>
        <field index="5" term="http://rs.tdwg.org/dwc/terms/country"/>
        <!-- A constant value has no index, but applies to all rows -->
    	<field term="http://rs.tdwg.org/dwc/terms/datasetID" default="urn:lsid:ppi.lsid.rebipp.org.br:interactions:1"/>
    </core>
</archive>
```

## 2 Metafile content

The [Darwin Core text metafile schema](https://github.com/tdwg/dwc/blob/master/docs/text/tdwg_dwc_text.xsd) provides technical details for the structure of a metafile by defining the elements and attributes necessary to describe the contents and relationships between text files. These elements and attributes, with descriptions and specifications for their use in a metafile, are described in the following table.

The same schema is adopted for documeting plant-pollinator interactions in _fielded text_ formats. However, some constraintis are applied to which classes and terms MUST be adopted for the `<core>` and `<extension>` elements in the metafile.

### 2.1 The `<archive>` element

The `<archive>` element is the container for the list of related files (one core and zero or more extensions). The `<archive>` element SHOULD have a `metadata` attribute.

#### 2.1.1 Attributes

Attribute | Description | Required | Default
--- | --- | --- | ---
`metadata` | If used, the value MUST be a qualified Uniform Resource Locator (URL) defining the location of a metadata description of the entire archive. The format of the metadata is not prescribed, but a standardized format such as Ecological Metadata Language (EML), Federal Geographic Data Committee (FGDC), or a format from the ISO 19115 family is RECOMMENDED. | no |

#### 2.1.2 Elements

Element | Description
--- | ---
`<core>` | An `<archive>` MUST contain exactly one `<core>` element of `rowType` set to `Event`: <http://rs.tdwg.org/dwc/terms/Event>, representing the data entity (the actual file and its column header mappings to Darwin Core terms) upon which records are based. In the extensions each record in the core data MUST have a unique identifier. The field for this identifier MUST be specified in an explicit `<id>` field in order to associate extension records with the core record.
`<extension>` | An `<archive>` MUST define `<extension>` elements of such Darwin Core classes: `Occurrence`: <http://rs.tdwg.org/dwc/terms/Occurrence>, `ResourceRelationship`: <http://rs.tdwg.org/dwc/terms/ResourceRelationship>, and MAY define `<extension>` elements of `MeasurementOrFact`: <http://rs.tdwg.org/dwc/terms/MeasurementOrFact> class or [`ExtendedMeasurementOrFact`](https://tools.gbif.org/dwca-validator/extension.do?id=dwc:MeasurementOrFact): <http://rs.iobis.org/obis/terms/ExtendedMeasurementOrFact>, each representing an individual extension entity directly related to the core. In addition to the general file attributes described below, every extension entity MUST have an explicit `<coreid>` field to relate the extension record to a row in the core entity. The extension itself does not have to have a unique ID field and many rows can point to the same core record.

### 2.2 The `<core>` or `<extension>` element

#### 2.2.1 Attributes

Attribute | Description | Required | Default
--- | --- | --- | ---
`rowType` | The row type is REQUIRED and MUST be a Unified Resource Identifier (URI). For the `<core>` element the `rowType` MUST be set to `dwc:Event`: <http://rs.tdwg.org/dwc/terms/Event>. For the `<extension>` elements any the term identifying the class of data represented MAY be defined, incluing terms outside the Darwin Core specification if denoted by a URI. However, a `<archive>` MUST have `<extension>` elements of the following Darwin Core classes: `Occurrence`: <http://rs.tdwg.org/dwc/terms/Occurrence> (represeting the occurrences of the interactiong organisms) and `ResourceRelationship`: <http://rs.tdwg.org/dwc/terms/ResourceRelationship> (representing the direction and type of the interactions). Optionally, it MAY contains `<extension>` elements with `rowType` of `MeasurementOrFact`: <http://rs.tdwg.org/dwc/terms/MeasurementOrFact> or `ExtendedMeasurementOrFact`: <http://rs.iobis.org/obis/terms/ExtendedMeasurementOrFact> (representing traits of the organisms, or interaction outcomes),  | yes |
`fieldsTerminatedBy` | Specifies the delimiter between fields. Typical values MAY be `,` or `\t` for CSV or Tab files respectively. | no | `,`
`linesTerminatedBy` | Specifies the row separator character. | no | `\n`
`fieldsEnclosedBy` | Specifies the character used to enclose (mark the start and end of) each field. CSV files frequently use the double quote character (`"`), which is the default value if none is explicitly provided. Note that a comma separated value file that has commas within the content of any field MUST have an enclosing character. | no | `"`
`encoding` | Specifies the [character encoding](https://en.wikipedia.org/wiki/Character_encoding) for the data file. The encoding is extremely important, but often ignored. The most frequently used encodings are: `UTF-8`: 8-bit Unicode Transformation Format, `UTF-16`: 16-bit Unicode Transformation Format, `ISO-8859-1`: commonly known as "Latin-1" and a common default on systems configured for a single western European language, `Windows-1252`: commonly known as "WinLatin" and a common default of legacy versions of Microsoft Windows-based operating systems. | no | `UTF-8`
`ignoreHeaderLines` | Specifies the number lines to ignore from the beginning of the file. This MAY be used to ignore files with column headings or preamble comments. | no | `0`
`dateFormat` | If date fields throughout the entire dataset follow a consistent format, this format MAY be specified by the `dateFormat` parameter. This SHOULD be considered a 'hint' for consumers in cases where the date fields do not follow the RECOMMENDED ISO 8601:2019-1 specification. The format for this parameter MUST be a combination of year (`YYYY`), month (`MM`), and day (`DD`) indicators in combination with a separator (`/` or `-`). Examples: `DDMMYYYY` for dates of the form 21121978, `DD-MM-YYYY` for dates of the form 21-12-1978, `MMDDYYYY` for dates of the form 12211978, `MM-DD-YYYY` for dates of the form 12-21-1978, `YYYYMMDD` for dates of the form 19781221. | no | `YYYY-MM-DD`

#### 2.2.2 Elements

Element | Description
--- | ---
`<files>` | A `<core>` element MUST contain one `<files>` element to locate the data being described. An `<extension>` element MUST also contain one `<files>` element.
`<id>` | The `<core>` MUST contain an `<id>` element, which indicates the identifier for a record.
`<coreid>` | The `<extension>` element MUST contain a `<coreid>` element, which indicates the column in the extension file that contains the core record identifier (the value that is supposed to match the `<id>` in the core file).
`<field>` | A `<core>` or `<extension>` element MUST contain one or more `<field>` elements, each representing a 'column' in the row.

### 2.3 `<files>` element

The `<files>` element MUST contain one or more `<location>` elements, each defining where a file resides. Each `<core>` or `<extension>` entity MAY be composed from one or more files. If an entity has data in more than one file, the `<location>` element MUST be present once for each distinct `<file>` that makes up the entity.

#### 2.3.1 Elements

Element | Description
--- | ---
`<location>` | Specifies the location of the `<file>` being described. The `<location>` element MUST take one of the following forms: 1) a web accessible URL such as `http://www.rebipp.org.br/data/interactions.csv` or `ftp://ftp.rebipp.org.br/ppi/interactions.txt`, or 2) a file path relative to the location of the metafile such as `interactions.txt`, `./interactions.txt`, `./data/interactions.txt`.

### 2.4 The `<field>` element

The `<field>` element is used to specify the location and content of data within a `<file>`. There MUST be one `<field>` element for every term being shared for the entity, whether explicitly or through the use of a `<default>` value for all rows in the `<file>`.

#### 2.4.1 Attributes

Attribute | Description | Required | Default
--- | --- | --- | ---
`index` | Specifies the position of the column in the row. The first column has an index of 0, the second column has an index of 1, etc. If no column index is specified, the term and a default constant value for it MAY be defined for all rows. | no |
`term` | MUST be a Unified Resource Identifier (URI) for the term represented by this `<field>`. For example, a column containing the scientific name would have `term="http://rs.tdwg.org/dwc/terms/scientificName"`. Terms outside of the Darwin Core specification, such as those from the Dublin Core Metadata Initative, MAY be used. For example, `dcterms:modified` would be `term="http://purl.org/dc/terms/modified"`. | yes |
`default` | Specifies a value to use if one is not supplied for the `<field>` in a given row. If no index is supplied for a given `<field>`, the `<default>` MAY be used to define a constant for all rows for that `<field>`. | no |
`vocabulary` | When present, MUST be a Unified Resource Identifier (URI) for a vocabulary that the source values for this `<field>` are based on. The URI SHOULD resolve to some machine readable definition such as SKOS or RDF, or a simple text or HTML file such as often found for ISO or RFC standards. For example <http://rs.gbif.org/vocabulary/gbif/nomenclatural_code.xml>, <http://www.ietf.org/rfc/rfc3066.txt> or <http://www.iso.org/iso/list-en1-semic-3.txt>. | no |

## 3 Implementation guide (non-normative)

The representation of plant-pollinator interactions in _fielded text_ format follows the same rule of the Darwin Core Text with additional constraints on which classes and terms MUST be used and how.

### 3.1 The metafile (non-normative)

The following example illustrates the use of the [Plant-Pollinator Interactions vocabulary of terms](../terms) and the [Plant-Pollinator Interactions controlled vocabulary](../cv). In this example there are four files in the archive, all of which are located in the same directory as the metafile. The _interactions.txt_ file acts as a core file of _dwc:Event_ records. The interactions.txt file is extended by three other files, _occurrences.txt_, _resrelat.txt_ and _emof.txt_. The _occurrences.txt_ file contains records of _dwc:Occurrence_ class, while the _resrelat.txt_ file contains records of _dwc:ResourceRelationship_ class, and the _emof_ file contains records specified in an external definition at <http://rs.iobis.org/obis/terms/ExtendedMeasurementOrFact> and consists of Darwin Core terms and new terms introduced by the [OBIS ExtendedMeasurementOrFact extension (eMoF)](https://obis.org/manual/dataformat/). In the example the OBIS eMoF extension MAY be replaced by the Darwin Core `dwc:MeasurementOrFact` class when the records are linked directly to the `<core>` element (e.g. interaction outcomes), opposed to when the records are linked to the occurrences in the `<extension>` element (e.g. organisms traits).

The extension files are related to the core file by the `dwc:EventID` fields. This archive contains information about interaction events, the occurrences of interactiong organisms, the direction and nature (i.e. type) of the interactions and the traits and interactions outcomes.

![Extension](extension.png)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<archive xmlns="http://rs.tdwg.org/dwc/text/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xsi:schemaLocation="http://rs.tdwg.org/dwc/text/ http://rs.tdwg.org/dwc/text/tdwg_dwc_text.xsd">

    <core encoding="UTF-8" fieldsTerminatedBy="," linesTerminatedBy="\n" ignoreHeaderLines="1" rowType="http://rs.tdwg.org/dwc/terms/Event">
        <files>
            <location>interactions.csv</location>
        </files>
        <id index="0" />
        <field index="0" term="http://rs.tdwg.org/dwc/terms/eventID" />
        <field index="1" term="http://rs.tdwg.org/dwc/terms/eventDate" />
        <field index="2" term="http://rs.tdwg.org/dwc/terms/eventTime"/>
        <field index="3" term="http://rs.tdwg.org/dwc/terms/decimalLatitude"/>
        <field index="4" term="http://rs.tdwg.org/dwc/terms/decimalLongitude"/>
        <field index="5" term="http://rs.tdwg.org/dwc/terms/country"/>
    </core>

    <extension encoding="UTF-8" fieldsTerminatedBy="," linesTerminatedBy="\n" fieldsEnclosedBy='"' ignoreHeaderLines="1" rowType="http://rs.tdwg.org/dwc/terms/Occurrence">
        <files>
            <location>occurrences.csv</location>
        </files>
        <coreid index="0" />
        <field index="1" term="http://rs.tdwg.org/dwc/terms/occurrecenID"/>
        <field index="2" term="http://rs.tdwg.org/dwc/terms/scientificaNameID"/>
        <field index="3" term="http://rs.tdwg.org/dwc/terms/scientificaName"/>
    </extension>

    <extension encoding="UTF-8" fieldsTerminatedBy="," linesTerminatedBy="\n" fieldsEnclosedBy='"' ignoreHeaderLines="1" rowType="http://rs.tdwg.org/dwc/terms/ResourceRelationship">
        <files>
            <location>resrelat.csv</location>
        </files>
        <coreid index="0" />
        <field index="1" term="http://rs.tdwg.org/dwc/terms/resourceRelationshipID"/>
        <field index="2" term="http://rs.tdwg.org/dwc/terms/resourceID"/>
        <field index="3" term="http://rs.tdwg.org/dwc/terms/relatedResourceID"/>
        <field index="4" term="http://rs.tdwg.org/dwc/terms/relationshipOfResourceID"/>
        <field index="5" term="http://rs.tdwg.org/dwc/terms/relationshipOfResource"/>
        <field index="6" term="http://rs.tdwg.org/dwc/terms/relationshipAccordingTo"/>
    </extension>

    <extension encoding="UTF-8" fieldsTerminatedBy="," linesTerminatedBy="\n" fieldsEnclosedBy='"' ignoreHeaderLines="1" rowType="http://rs.iobis.org/obis/terms/ExtendedMeasurementOrFact">
        <files>
            <location>emof.csv</location>
        </files>
        <coreid index="0" />
        <field index="1" term="http://rs.tdwg.org/dwc/terms/measurementID"/>
        <field index="2" term="http://rs.tdwg.org/dwc/terms/occurrenceID"/>
        <field index="3" term="http://rs.tdwg.org/dwc/terms/measurementTypeID"/>
        <field index="4" term="http://rs.tdwg.org/dwc/terms/measurementType"/>
        <field index="5" term="http://rs.tdwg.org/dwc/terms/measurementValueID"/>
        <field index="6" term="http://rs.tdwg.org/dwc/terms/measurementValue"/>
    </extension>
</archive>
```

### 3.2 Using the PPI vocabulary (non-normative)

The Plant-Pollinator Interactions vocabulary is meant to be used as controlled vocabulary for terms defined in the Darwin Core `MeasurementOrFact` class and in the OBIS `ExtendedMeasurementOrFact` extension. The terms in the PPI vocabulary MUST be used to document the type of the measurements or facts linked to the interactions and to the occurrences.

The main difference between the `obis:ExtendedMeasurementOrFact` and `dwc:MeasurementOrFact` and the is that the former extends the Darwin Core class with the follow terms:

- `dwc:occurrenceID`: The identifier of the occurrence the measurement or fact refers to. If not applicable, it should be left empty.
- `obis:measurementTypeID`: An identifier for the measurementType (global unique identifier, URI). The identifier should reference the measurementType in a vocabulary.
- `obis:measurementValueID`: An identifier for facts stored in the column measurementValue (global unique identifier, URI). This identifier can reference a controlled vocabulary (e.g. for sampling instrument names, methodologies, life stages) or reference a methodology paper with a DOI. When the measurementValue refers to a value and not to a fact, the measurementvalueID has no meaning and should remain empty.
- `obis:measurementUnitID`: An identifier for the measurementUnit (global unique identifier, URI). The identifier should reference the measurementUnit in a vocabulary.

The `dwc:occurrenceID` allows circuvent the limitations of the star-schema and to link records in the measurements or facts _extension_ file (e.g. _emof.csv_) to records in both the _core_ file (e.g. _interactions.csv_) and the ocurrences _extension_ file (e.g. _occurrences.csv_). If the data does not contains measurements of facts about the occurrences, the usage of eMoF is OPTIONAL. However, as will be discussed bellow, other terms in the eMoF extension allows the usage of the terms in the PPI vocabulary identified by their URI, instead of by their local names (when using `dwc:MeasurementOrFact`).

The terms in the PPI vocabulary MUST be used as values for the terms `dwc:measurementType` and `obis:measurementTypeID`, while the terms in the PPI-CV MUST be used as values for the terms `dwc:measurementValue` and `obis:measurementValueID`. The main difference is that `dwc:measurementType` MUST be filled with the labels of the terms (e.g. `flowerShape`, `caste`, `resourceCollected`), while the `obis:measurementTypeID` MUST be filled with URI of the terms (e.g. [http://rs.rebipp.org.br/ppi/terms/flowerShape](http://rs.rebipp.org.br/ppi/terms/flowerShape), [http://rs.rebipp.org.br/ppi/terms/caste](http://rs.rebipp.org.br/ppi/terms/caste), [http://rs.rebipp.org.br/ppi/terms/resourceCollected](http://rs.rebipp.org.br/ppi/terms/resourceCollected)).

The example bellow use the eMoF extension of representing the resource collected during the interaction (first row), two characteriscts of the plant (second and third rows) and the caste of a bee interacting with the plant (last row). **Note** that in the first row the _occurrenceID_ is empty since it is a measurement or fact of an interaction (second column). In the remain rows the _occurrenceID_ field contains the identifier of the occurrences in the ocurrences _extension_ file providing a link between the interaction (in the _core_ file), the occurrence (in the occurrence _extension_) and the measurement or fact.

```csv
eventID, occurrenceID, measurementID, measurementTypeID, measurementType, measurementValueID, measurementValue
123,,REBIPP:MOF:0001,http://rs.rebipp.org.br/ppi/terms/resourceCollected,resourceCollected,http://rs.rebipp.org.br/ppicv/values/pollen, pollen
123,REBIPP:OCC:00101,REBIPP:MOF:0002,http://rs.rebipp.org.br/ppi/terms/habit,habit,http://rs.rebipp.org.br/ppicv/values/tree,tree
123,REBIPP:OCC:00101,REBIPP:MOF:0003,http://rs.rebipp.org.br/ppi/terms/flowerLongevity,flowerLongevity,,168
123,REBIPP:OCC:00102,REBIPP:MOF:0004,http://rs.rebipp.org.br/ppi/terms/caste,caste,http://rs.rebipp.org.br/ppicv/values/worker,worker
```

### 3.3 The direction and type of the interactions (non-normative)