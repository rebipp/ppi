# List of Plant-Pollinator Interactions terms

Title
: List of Plant-Pollinator Interactions terms

Date version issued
: 2022-01-06

Date created
: 2022-01-06

Part of Standard
: <http://www.rebipp.org.br/standards/ppi>

This version
: <http://rs.rebipp.org.br/ppi/doc/list/2022-01-06>

Latest version
: <http://rs.rebipp.org.br/ppi/doc/list/>

Previous version
: <http://rs.rebipp.org.br/ppi/doc/list/2022-01-06>

Abstract
: The Plant-Pollinator Interactions (PPI) is a vocabulary of terms for transmitting information about plant-pollinator interactions using the Darwin Core standard. This document lists all terms in namespaces currently used in the vocabulary.

Contributors
: José Augusto Salim (USP), Antonio Mauro Saravia (USP), Paula Zermoglio (), Kayna Agostini (UFSCAR), ..., John Wieczorek (VertNet),

Creator
: Brazilian Network on Plant-Pollinator Interactions

Bibliographic citation
: REBIPP. 2022. List of Plant-Pollinator Interactions Vocabulary terms. Brazilian Network on Plant-Pollinator Interactions (REBIPP). <http://rs.rebipp.org.br/ppi/doc/list/2022-01-06>


## 1 Introduction (Informative)

This document contains terms that are part of the most recent version of the Plant-Pollinator Interactions vocabulary (<http://rs.rebipp.org.br/version/ppi/2022-01-06>).

This document includes terms in the namespace `ppi` that contain recommended terms. However, some terms in these namespaces are deprecated or superseded and should no longer be used. Deprecation or supersession is noted in the term metadata. Namespaces that contain only deprecated terms are not included in this document, but metadata about those terms can be retrieved by dereferencing their IRIs.

For a simplified list that contains only the currently recommended terms, see the [Quick Reference Guide](../terms/).

### 1.1 Status of the content of this document

Sections 1 and 3 are non-normative.

Section 2 is normative.

In Section 4, the values of the `Term IRI` and `Definition` are normative. The values of `Term Name` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  `Label` and the values of all other properties (such as `Examples` and `Notes`) are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.3 Namespace abbreviations

The following namespace abbreviations are used in this document:

| abbreviation | IRI |
| --- | --- |
| dwc: | http://rs.rebipp.org.br/dwc/terms/ |
| dwciri: | http://rs.rebipp.org.br/dwc/iri/ |
| dc: | http://purl.org/dc/elements/1.1/ |
| dcterms: | http://purl.org/dc/terms/ |
| ppi: | http://rs.rebipp.org.br/ppi/terms/ |
| obis: | http://rs.iobis.org/obis/terms/ |

## 2 Use of Terms

The terms in the Plant-Pollinator Interactions vocabulary are meant to be used as controlled vocabulary for the terms in [Darwin Core Standard](http://dwc.tdwg.org): `dwc:measurementType`, `dwc:measurementValue` and `dwciri:measurementType`. However, the terms could be used with other extensions like the [OBIS ExtendedMeasurementOrFact](https://obis.org/manual/dataformat/) providing a controlled vocabulary for `obis:measurementTypeID` and `obis:measurementValueID`.

See [Section XXX of the Text Guide](../text/#XXX), [Section XXX of the XML Guide](../xml/#XXX) and [Section XXX of the RDF Guide](../rdf/#XXX) for details.

## 3 Term indices
### 3.1 Index By Term Name

(See also [3.2 Index By Label](#32-index-by-label))

**Classes**

[ppi:Animal](#ppi_Animal) |
[ppi:Flower](#ppi_Flower) |
[ppi:Interaction](#ppi_Interaction) |
[ppi:NectarDynamics](#ppi_NectarDynamics) |
[ppi:Plant](#ppi_Plant) |
[ppi:ReproductiveSuccess](#ppi_ReproductiveSuccess) 

**Animal**

[ppi:caste](#ppi_caste) 

**Plant**

[ppi:antherDehiscenceType](#ppi_antherDehiscenceType) |
[ppi:apomiticSystemEmbryoOrigin](#ppi_apomiticSystemEmbryoOrigin) |
[ppi:apomiticSystemFertilization](#ppi_apomiticSystemFertilization) |
[ppi:apomiticSystemReproduction](#ppi_apomiticSystemReproduction) |
[ppi:floralSymmetry](#ppi_floralSymmetry) |
[ppi:floralSystem](#ppi_floralSystem) |
[ppi:flowerAbundance](#ppi_flowerAbundance) |
[ppi:humanUse](#ppi_humanUse) |
[ppi:matingSystem](#ppi_matingSystem) |
[ppi:plantHabit](#ppi_plantHabit) |
[ppi:selfIncompatibilityType](#ppi_selfIncompatibilityType) |
[ppi:sexualSystem](#ppi_sexualSystem) 

**Flower**

[ppi:antherPollenGrainsQuantity](#ppi_antherPollenGrainsQuantity) |
[ppi:coloredFlowerStructure](#ppi_coloredFlowerStructure) |
[ppi:floralAttractants](#ppi_floralAttractants) |
[ppi:flowerColor](#ppi_flowerColor) |
[ppi:flowerLongevity](#ppi_flowerLongevity) |
[ppi:flowerOpeningPeriod](#ppi_flowerOpeningPeriod) |
[ppi:flowerOpeningType](#ppi_flowerOpeningType) |
[ppi:flowerOrientation](#ppi_flowerOrientation) |
[ppi:flowerShape](#ppi_flowerShape) |
[ppi:functionalFlowerLifespanInHours](#ppi_functionalFlowerLifespanInHours) |
[ppi:ovuleQuantity](#ppi_ovuleQuantity) |
[ppi:stigmaticAreaInSquareMilimiters](#ppi_stigmaticAreaInSquareMilimiters) |
[ppi:styleLengthInMilimiters](#ppi_styleLengthInMilimiters) 

**Interaction**

**ReproductiveSuccess**

[ppi:fruitMassInGrams](#ppi_fruitMassInGrams) |
[ppi:fruitSet](#ppi_fruitSet) |
[ppi:numberOfConspecificPollenGrains](#ppi_numberOfConspecificPollenGrains) |
[ppi:numberOfExposedFlowers](#ppi_numberOfExposedFlowers) |
[ppi:numberOfFertilizedOvules](#ppi_numberOfFertilizedOvules) |
[ppi:numberOfHeterospecificPollenGrains](#ppi_numberOfHeterospecificPollenGrains) |
[ppi:numberOfPollenTubes](#ppi_numberOfPollenTubes) |
[ppi:numberOfRemovedPollenGrains](#ppi_numberOfRemovedPollenGrains) |
[ppi:seedMassInMiligrams](#ppi_seedMassInMiligrams) |
[ppi:seedSet](#ppi_seedSet) 

**NectarDynamics**

[ppi:accumlatedNectarVolumeInMicroliters](#ppi_accumlatedNectarVolumeInMicroliters) |
[ppi:accumulatedNectarConcentration](#ppi_accumulatedNectarConcentration) |
[ppi:accumulatedNectarFlowers](#ppi_accumulatedNectarFlowers) |
[ppi:accumulatedNectarHours](#ppi_accumulatedNectarHours) 

### 3.2 Index By Label

(See also [3.1 Index By Term Name](#31-index-by-term-name))

**Classes**

[Animal](#ppi_Animal) |
[Flower](#ppi_Flower) |
[Interaction](#ppi_Interaction) |
[Nectar Dynamics](#ppi_NectarDynamics) |
[Plant](#ppi_Plant) |
[Reproductive Success](#ppi_ReproductiveSuccess) 

**Animal**

[Caste](#ppi_caste) 

**Plant**

[Anther Dehiscence Type](#ppi_antherDehiscenceType) |
[Apomitic System Embryo Origin](#ppi_apomiticSystemEmbryoOrigin) |
[Apomitic System Fertilization](#ppi_apomiticSystemFertilization) |
[Apomitic System Reproduction](#ppi_apomiticSystemReproduction) |
[Floral Symmetry](#ppi_floralSymmetry) |
[Floral System](#ppi_floralSystem) |
[Flower Abundance](#ppi_flowerAbundance) |
[Human Use](#ppi_humanUse) |
[Mating System](#ppi_matingSystem) |
[Plant Habit](#ppi_plantHabit) |
[Self Incompatibility Type](#ppi_selfIncompatibilityType) |
[Sexual System](#ppi_sexualSystem) 

**Flower**

[Anther Pollen Grains Quantity](#ppi_antherPollenGrainsQuantity) |
[Colored Flower Structure](#ppi_coloredFlowerStructure) |
[Floral Attractants](#ppi_floralAttractants) |
[Flower Color](#ppi_flowerColor) |
[Flower Longevity](#ppi_flowerLongevity) |
[Flower Opening Period](#ppi_flowerOpeningPeriod) |
[Flower Opening Type](#ppi_flowerOpeningType) |
[Flower Orientation](#ppi_flowerOrientation) |
[Flower Shape](#ppi_flowerShape) |
[Functional Flower Lifespan In Hours](#ppi_functionalFlowerLifespanInHours) |
[Ovule Quantity](#ppi_ovuleQuantity) |
[Stigmatic Area In Square Milimiters](#ppi_stigmaticAreaInSquareMilimiters) |
[Style Length In Milimiters](#ppi_styleLengthInMilimiters) 

**Interaction**

**ReproductiveSuccess**

[Fruit Mass In Grams](#ppi_fruitMassInGrams) |
[Fruit Set](#ppi_fruitSet) |
[Number Of Conspecific Pollen Grains](#ppi_numberOfConspecificPollenGrains) |
[Number Of Exposed Flowers](#ppi_numberOfExposedFlowers) |
[Number Of Fertilized Ovules](#ppi_numberOfFertilizedOvules) |
[Number Of Heterospecific Pollen Grains](#ppi_numberOfHeterospecificPollenGrains) |
[Number Of Pollen Tubes](#ppi_numberOfPollenTubes) |
[Number Of Removed Pollen Grains](#ppi_numberOfRemovedPollenGrains) |
[Seed Mass In Miligrams](#ppi_seedMassInMiligrams) |
[Seed Set](#ppi_seedSet) 

**NectarDynamics**

[Accumlated Nectar Volume In Microliters](#ppi_accumlatedNectarVolumeInMicroliters) |
[Accumulated Nectar Concentration](#ppi_accumulatedNectarConcentration) |
[Accumulated Nectar Flowers](#ppi_accumulatedNectarFlowers) |
[Accumulated Nectar Hours](#ppi_accumulatedNectarHours) 

## 4 Vocabulary
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_accumlatedNectarVolumeInMicroliters"></a>Term Name  ppi:accumlatedNectarVolumeInMicroliters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/accumlatedNectarVolumeInMicroliters">http://rs.rebipp.org.br/ppi/terms/accumlatedNectarVolumeInMicroliters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/accumlatedNectarVolumeInMicroliters-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/accumlatedNectarVolumeInMicroliters-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Accumlated Nectar Volume In Microliters</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total volume in microliters of nectar accumulated by the flower(s)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The total volume of nectar should be provided for flowers which were not exposed to floral visitors during all their longevity. If reporting this value, the <code>accumulatedNectarHours</code> should also be provided.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>5</code>, <code>10</code>, <code>5.5</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_accumulatedNectarConcentration"></a>Term Name  ppi:accumulatedNectarConcentration</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/accumulatedNectarConcentration">http://rs.rebipp.org.br/ppi/terms/accumulatedNectarConcentration</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/accumulatedNectarConcentration-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/accumulatedNectarConcentration-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Accumulated Nectar Concentration</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The concentration of the nectar, in percentage of sugar, accumulated by the flower(s)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The accumulated nectar concentration should be provided for flowers which were not exposed to floral visitors during all their longevity. If reporting this value, the <code>accumulatedNectarHours</code> should also be provided</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>10.2</code>, <code>25</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_accumulatedNectarFlowers"></a>Term Name  ppi:accumulatedNectarFlowers</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/accumulatedNectarFlowers">http://rs.rebipp.org.br/ppi/terms/accumulatedNectarFlowers</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/accumulatedNectarFlowers-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/accumulatedNectarFlowers-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Accumulated Nectar Flowers</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total number of flowers which the accumulated nectar measurements were made</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The flowers should be prevented from visitation (not exposed to floral visitors) during all their logenvity</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>4</code>, <code>23</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_accumulatedNectarHours"></a>Term Name  ppi:accumulatedNectarHours</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/accumulatedNectarHours">http://rs.rebipp.org.br/ppi/terms/accumulatedNectarHours</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/accumulatedNectarHours-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/accumulatedNectarHours-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Accumulated Nectar Hours</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The time in hours in which the nectar was let to accumulated in the flower(s)</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>0.5</code>, <code>2</code>, <code>48</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_Animal"></a>Term Name  ppi:Animal</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/Animal">http://rs.rebipp.org.br/ppi/terms/Animal</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/Animal-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/Animal-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Animal</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Any attribute of a particular animal or a definied group of animals individuals</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Class</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_animalPlaceOfContact"></a>Term Name  ppi:animalPlaceOfContact</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/animalPlaceOfContact">http://rs.rebipp.org.br/ppi/terms/animalPlaceOfContact</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/animalPlaceOfContact-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/animalPlaceOfContact-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Animal Place Of Contact</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A list (concatenated and separated) of the animal body parts that contact the plant during the interaction</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to separate the values in a list with space vertical bar space ( <code>|</code> ) and to use a controlled vocabulary</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_antherDehiscenceType"></a>Term Name  ppi:antherDehiscenceType</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/antherDehiscenceType">http://rs.rebipp.org.br/ppi/terms/antherDehiscenceType</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/antherDehiscenceType-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/antherDehiscenceType-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Anther Dehiscence Type</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The physical mechanism of anther dehiscence (release of the pollen grains)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>poricidal</code>, <code>longitudinal</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_antherPollenGrainsQuantity"></a>Term Name  ppi:antherPollenGrainsQuantity</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/antherPollenGrainsQuantity">http://rs.rebipp.org.br/ppi/terms/antherPollenGrainsQuantity</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/antherPollenGrainsQuantity-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/antherPollenGrainsQuantity-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Anther Pollen Grains Quantity</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total number of pollen grains in the anther(s) of a flower</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For flowers with multiple anthers the number provided should be the sum of pollen grains in all anthers</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_apomiticSystemEmbryoOrigin"></a>Term Name  ppi:apomiticSystemEmbryoOrigin</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/apomiticSystemEmbryoOrigin">http://rs.rebipp.org.br/ppi/terms/apomiticSystemEmbryoOrigin</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/apomiticSystemEmbryoOrigin-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/apomiticSystemEmbryoOrigin-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Apomitic System Embryo Origin</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The general mode of apomixis embryo origin of a plant</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary.
</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>gametophytic,sporpophytic
</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_apomiticSystemFertilization"></a>Term Name  ppi:apomiticSystemFertilization</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/apomiticSystemFertilization">http://rs.rebipp.org.br/ppi/terms/apomiticSystemFertilization</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/apomiticSystemFertilization-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/apomiticSystemFertilization-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Apomitic System Fertilization</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The general mode of apomixis endosperm development of a plant</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary.
</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>autonomous,pseudogamy</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_apomiticSystemReproduction"></a>Term Name  ppi:apomiticSystemReproduction</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/apomiticSystemReproduction">http://rs.rebipp.org.br/ppi/terms/apomiticSystemReproduction</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/apomiticSystemReproduction-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/apomiticSystemReproduction-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Apomitic System Reproduction</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The general mode of apomixis reproduction of a plant</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary.
</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>facultative, obligate</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_caste"></a>Term Name  ppi:caste</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/caste">http://rs.rebipp.org.br/ppi/terms/caste</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/caste-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/caste-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Caste</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The society division that is specialized in the function it performs and is distinguished by anatomical or morphological features from other individuals of in the society</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best pratices is to use a controlled vocabulary</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_coloredFlowerStructure"></a>Term Name  ppi:coloredFlowerStructure</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/coloredFlowerStructure">http://rs.rebipp.org.br/ppi/terms/coloredFlowerStructure</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/coloredFlowerStructure-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/coloredFlowerStructure-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Colored Flower Structure</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The predominant colored structure(s) of the flower(s)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to separate the values in a list with space vertical bar space ( | ).

Recommended best practice is to use a controlled vocabulary.
</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_floralAttractants"></a>Term Name  ppi:floralAttractants</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/floralAttractants">http://rs.rebipp.org.br/ppi/terms/floralAttractants</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/floralAttractants-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/floralAttractants-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Floral Attractants</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Types of attractants (visual, chemical or tactile) present in the flowers that floral visitors may use to locate them and their resources</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to separate the values in a list with space vertical bar space ( | ) and to use a controlled vocabulary</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_floralSymmetry"></a>Term Name  ppi:floralSymmetry</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/floralSymmetry">http://rs.rebipp.org.br/ppi/terms/floralSymmetry</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/floralSymmetry-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/floralSymmetry-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Floral Symmetry</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The symmetry describing whether, and how, a flower, in particular its perianth, can be divided into two or more identical or mirror-image parts.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary such as the Phenotype and Trait Ontology</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>zygomorphic</code>, <code>bilateral</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_floralSystem"></a>Term Name  ppi:floralSystem</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/floralSystem">http://rs.rebipp.org.br/ppi/terms/floralSystem</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/floralSystem-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/floralSystem-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Floral System</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The system by which bisexual flowers optimize their reproductive success, through mechanisms that promote self- or cross-pollination</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>It can be a morphological, temporal or movement-based mechanism.
Recommended best practice is to use a controlled vocabulary.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>herkogamy</code>, <code>heterostyly</code>, <code>stylar dimorphism</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_Flower"></a>Term Name  ppi:Flower</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/Flower">http://rs.rebipp.org.br/ppi/terms/Flower</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/Flower-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/Flower-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Flower</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Any attribute of a particular flower or a definied group of flowers </td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Class</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_flowerAbundance"></a>Term Name  ppi:flowerAbundance</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/flowerAbundance">http://rs.rebipp.org.br/ppi/terms/flowerAbundance</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/flowerAbundance-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/flowerAbundance-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Flower Abundance</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The number of open flowers or inflorescences on the plant</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If it is an estimate then you should describe the accuracy of the measurement using <a href="http://rs.tdwg.org/dwc/terms/measurementAccuracy">http://rs.tdwg.org/dwc/terms/measurementAccuracy</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>0</code>, <code>30</code>, <code>40</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_flowerColor"></a>Term Name  ppi:flowerColor</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/flowerColor">http://rs.rebipp.org.br/ppi/terms/flowerColor</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/flowerColor-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/flowerColor-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Flower Color</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The predominant color(s) of the flower(s)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to separate the values with space vertical bar space ( | ).

Recommended best practice is to use a controlled vocabulary.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_flowerLongevity"></a>Term Name  ppi:flowerLongevity</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/flowerLongevity">http://rs.rebipp.org.br/ppi/terms/flowerLongevity</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/flowerLongevity-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/flowerLongevity-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Flower Longevity</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total amount of hours comprising the time between flower opening and flower senescence</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>A flower is considered opened when its petals are fully open regardless of anther maturation and stigma receptivity, and flower senescence is when floral parts begin to wilt and fall off or the ovary starts to develop into fruit</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_flowerOpeningPeriod"></a>Term Name  ppi:flowerOpeningPeriod</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/flowerOpeningPeriod">http://rs.rebipp.org.br/ppi/terms/flowerOpeningPeriod</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/flowerOpeningPeriod-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/flowerOpeningPeriod-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Flower Opening Period</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The time or interval during which a chasmogamous flower opens exposing its reproductive parts</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a time interval that conforms to ISO  8601-1:2019.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_flowerOpeningType"></a>Term Name  ppi:flowerOpeningType</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/flowerOpeningType">http://rs.rebipp.org.br/ppi/terms/flowerOpeningType</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/flowerOpeningType-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/flowerOpeningType-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Flower Opening Type</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The type of flower describing whether the flower's corolla opens or not, exposing its reproductive parts</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_flowerOrientation"></a>Term Name  ppi:flowerOrientation</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/flowerOrientation">http://rs.rebipp.org.br/ppi/terms/flowerOrientation</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/flowerOrientation-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/flowerOrientation-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Flower Orientation</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The orientation (presentation) of the flower with respect to the flower or inflorescence main axis</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_flowerPlaceOfContact"></a>Term Name  ppi:flowerPlaceOfContact</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/flowerPlaceOfContact">http://rs.rebipp.org.br/ppi/terms/flowerPlaceOfContact</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/flowerPlaceOfContact-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/flowerPlaceOfContact-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Flower Place Of Contact</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A list (concatenated and separated) of flower parts touched by the animal during the interaction</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to separate the values in a list with space vertical bar space ( <code>|</code> ) and to use a controlled vocabulary
</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_flowerShape"></a>Term Name  ppi:flowerShape</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/flowerShape">http://rs.rebipp.org.br/ppi/terms/flowerShape</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/flowerShape-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/flowerShape-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Flower Shape</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The overall shape of the flowers</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_fruitMassInGrams"></a>Term Name  ppi:fruitMassInGrams</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/fruitMassInGrams">http://rs.rebipp.org.br/ppi/terms/fruitMassInGrams</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/fruitMassInGrams-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/fruitMassInGrams-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Fruit Mass In Grams</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total mass in grams of the fruit(s)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If reporting this value, the <code>fruitSet</code> should also be provided.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>500</code>, <code>1256.55</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_fruitSet"></a>Term Name  ppi:fruitSet</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/fruitSet">http://rs.rebipp.org.br/ppi/terms/fruitSet</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/fruitSet-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/fruitSet-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Fruit Set</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total number of mature fruits of the exposed flower(s)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If reporting this value, the <code>numberOfExposedFlowers</code> should also be provided</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>5</code>, <code>12</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_functionalFlowerLifespanInHours"></a>Term Name  ppi:functionalFlowerLifespanInHours</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/functionalFlowerLifespanInHours">http://rs.rebipp.org.br/ppi/terms/functionalFlowerLifespanInHours</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/functionalFlowerLifespanInHours-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/functionalFlowerLifespanInHours-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Functional Flower Lifespan In Hours</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total amount of hours during which a flower is sexually functional</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The period of time when stigma is receptive to the germination of pollen grains, ovules are receptive to the pollen tubes or anthers present viable pollen grains</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_humanUse"></a>Term Name  ppi:humanUse</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/humanUse">http://rs.rebipp.org.br/ppi/terms/humanUse</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/humanUse-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/humanUse-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Human Use</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Ways in which species are utilized by people, including cultural use</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary.
</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>human food </code>, <code>animal food</code>, <code>medicine</code>, <code>ritual</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_Interaction"></a>Term Name  ppi:Interaction</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/Interaction">http://rs.rebipp.org.br/ppi/terms/Interaction</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/Interaction-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/Interaction-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Interaction</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An interaction event that occurs at some location during some time.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Class</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_matingSystem"></a>Term Name  ppi:matingSystem</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/matingSystem">http://rs.rebipp.org.br/ppi/terms/matingSystem</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/matingSystem-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/matingSystem-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Mating System</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A list (concatenated and separated) of the modes of gene transfer from one generation to the next through sexual reproduction</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to separate the values in a list with space vertical bar space ( | ) and to use a controlled vocabulary.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>autogamous</code>, <code>xenogamous</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_nectarCollectingBodyPart"></a>Term Name  ppi:nectarCollectingBodyPart</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/nectarCollectingBodyPart">http://rs.rebipp.org.br/ppi/terms/nectarCollectingBodyPart</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/nectarCollectingBodyPart-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/nectarCollectingBodyPart-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Nectar Collecting Body Part</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The animal body part used to collect nectar from the plant nectaries</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The plant nectaries can be floral or extrafloral nectaries. Recommended best practice is to use a controlled vocabulary such as Uberon or the Hymenoptera Anatomy Ontology</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_nectarCollectingBodyPartLengthInMilimiters"></a>Term Name  ppi:nectarCollectingBodyPartLengthInMilimiters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/nectarCollectingBodyPartLengthInMilimiters">http://rs.rebipp.org.br/ppi/terms/nectarCollectingBodyPartLengthInMilimiters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/nectarCollectingBodyPartLengthInMilimiters-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/nectarCollectingBodyPartLengthInMilimiters-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Nectar Collecting Body Part Length In Milimiters</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The length in millimeters of the body part used to collect nectar from the plant nectaries</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If reporting this value, the <code>nectarCollectingBodyPart</code> should also be provided.</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_NectarDynamics"></a>Term Name  ppi:NectarDynamics</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/NectarDynamics">http://rs.rebipp.org.br/ppi/terms/NectarDynamics</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/NectarDynamics-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/NectarDynamics-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Nectar Dynamics</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The measurements of nectar dynamics</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>A nectar dynamics measurement is related to the plant occurrence(s) </td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>The accumulated nectar in the monitored flowers</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Class</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_numberOfConspecificPollenGrains"></a>Term Name  ppi:numberOfConspecificPollenGrains</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/numberOfConspecificPollenGrains">http://rs.rebipp.org.br/ppi/terms/numberOfConspecificPollenGrains</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/numberOfConspecificPollenGrains-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/numberOfConspecificPollenGrains-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Number Of Conspecific Pollen Grains</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total number of conspecific pollen grains deposited on the stigma(s) of the visited flower(s)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The pollen grains may have been deposited at the end of the flower(s) anthesis by multiple floral visitors </td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>356</code>, <code>500</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_numberOfExposedFlowers"></a>Term Name  ppi:numberOfExposedFlowers</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/numberOfExposedFlowers">http://rs.rebipp.org.br/ppi/terms/numberOfExposedFlowers</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/numberOfExposedFlowers-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/numberOfExposedFlowers-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Number Of Exposed Flowers</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total number of flowers exposed to floral visitors</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The exposed flowers are the flowers monitored to measure the reproductive success of the plant(s). For the total number of flowers available to floral visitors (including flowers unmonitored) use <code>flowerAbundance</code>.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>4</code>, <code>11</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_numberOfFertilizedOvules"></a>Term Name  ppi:numberOfFertilizedOvules</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/numberOfFertilizedOvules">http://rs.rebipp.org.br/ppi/terms/numberOfFertilizedOvules</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/numberOfFertilizedOvules-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/numberOfFertilizedOvules-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Number Of Fertilized Ovules</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total number of fertilized ovules in the visited flower(s)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The ovules may have been fertilized as a result of multiple floral visits</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>3</code>, <code>5</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_numberOfHeterospecificPollenGrains"></a>Term Name  ppi:numberOfHeterospecificPollenGrains</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/numberOfHeterospecificPollenGrains">http://rs.rebipp.org.br/ppi/terms/numberOfHeterospecificPollenGrains</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/numberOfHeterospecificPollenGrains-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/numberOfHeterospecificPollenGrains-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Number Of Heterospecific Pollen Grains</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total number of heterospecific pollen grains deposited on a the stigma(s) of the visited flower(s)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The pollen grains may have been deposited at the end of the flower(s) anthesis by multiple floral visitors </td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>356</code>, <code>500</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_numberOfPollenTubes"></a>Term Name  ppi:numberOfPollenTubes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/numberOfPollenTubes">http://rs.rebipp.org.br/ppi/terms/numberOfPollenTubes</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/numberOfPollenTubes-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/numberOfPollenTubes-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Number Of Pollen Tubes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total number of pollen tubes growing in the style(s) of the visited flower(s)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The flower(s) may have been exposed by multiple floral visitors. The number should include pollen tubes growing from all styles of the flower(s)</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>1</code>, <code>5</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_numberOfRemovedPollenGrains"></a>Term Name  ppi:numberOfRemovedPollenGrains</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/numberOfRemovedPollenGrains">http://rs.rebipp.org.br/ppi/terms/numberOfRemovedPollenGrains</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/numberOfRemovedPollenGrains-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/numberOfRemovedPollenGrains-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Number Of Removed Pollen Grains</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total number of pollen grains removed from the anther(s) of the visited flower(s)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The pollen grains may have been removed by multiple floral visitors. The number should include pollen grains from all anthers of the flower(s)</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>156</code>, <code>350</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_ovuleQuantity"></a>Term Name  ppi:ovuleQuantity</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/ovuleQuantity">http://rs.rebipp.org.br/ppi/terms/ovuleQuantity</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/ovuleQuantity-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/ovuleQuantity-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Ovule Quantity</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total amount of ovules in a flower</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_Plant"></a>Term Name  ppi:Plant</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/Plant">http://rs.rebipp.org.br/ppi/terms/Plant</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/Plant-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/Plant-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Plant</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Any attribute of a particular plant or a defined group of plants inviduals</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Class</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_plantHabit"></a>Term Name  ppi:plantHabit</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/plantHabit">http://rs.rebipp.org.br/ppi/terms/plantHabit</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/plantHabit-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/plantHabit-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Plant Habit</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The general appearance, characteristic form, or mode of growth of the plant</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>tree</code>, <code>bush</code>, <code>herb</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_ReproductiveSuccess"></a>Term Name  ppi:ReproductiveSuccess</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/ReproductiveSuccess">http://rs.rebipp.org.br/ppi/terms/ReproductiveSuccess</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/ReproductiveSuccess-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/ReproductiveSuccess-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Reproductive Success</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A reproductive success measurement as a result or a effect of the interaction(s) on the subject or object of the interaction</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>An outcome is related to one or more interactions, but limited to the same subject or object of the related interactions (e.g. a dwc:Occurrence or a dwc:Taxon)</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>The mass of a fruit exposed to multiple visitors was 100 grams</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Class</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_resourceCollected"></a>Term Name  ppi:resourceCollected</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/resourceCollected">http://rs.rebipp.org.br/ppi/terms/resourceCollected</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/resourceCollected-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/resourceCollected-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Resource Collected</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A list (concatenated and separated) of floral resources used or removed from the visited flower(s) during the interaction</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to separate the values in a list with space vertical bar space ( <code>|</code> ) and to use a controlled vocabulary</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_seedMassInMiligrams"></a>Term Name  ppi:seedMassInMiligrams</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/seedMassInMiligrams">http://rs.rebipp.org.br/ppi/terms/seedMassInMiligrams</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/seedMassInMiligrams-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/seedMassInMiligrams-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Seed Mass In Miligrams</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total mass in miligrams of the seeds of mature fruit(s)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If reporting this value, the <code>seedSet</code> should also be provided.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>50</code>, <code>231.6</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_seedSet"></a>Term Name  ppi:seedSet</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/seedSet">http://rs.rebipp.org.br/ppi/terms/seedSet</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/seedSet-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/seedSet-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Seed Set</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total number of seeds of mature fruit(s)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If reporting this value, the <code>fruitSet</code> should also be provided.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>20</code>, <code>55</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_selfIncompatibilityType"></a>Term Name  ppi:selfIncompatibilityType</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/selfIncompatibilityType">http://rs.rebipp.org.br/ppi/terms/selfIncompatibilityType</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/selfIncompatibilityType-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/selfIncompatibilityType-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Self Incompatibility Type</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The type or class of self-incompatibility system of the plant species</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary. If the plant has no self-incompatibility system use the value <code>absent</code>.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>gametophytic</code>, <code>sporophytic</code>, <code>absent</code>, <code>homomorphic sporophytic</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_sexualSystem"></a>Term Name  ppi:sexualSystem</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/sexualSystem">http://rs.rebipp.org.br/ppi/terms/sexualSystem</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/sexualSystem-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/sexualSystem-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Sexual System</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The distribution of floral types within and among the individuals of the same population</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The gender expression is based in the presence and distribution of fertile whorls within the flower. Recommended best practice is to use a controlled vocabulary</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>monoceius</code>, <code>dioceius</code></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_stigmaticAreaInSquareMilimiters"></a>Term Name  ppi:stigmaticAreaInSquareMilimiters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/stigmaticAreaInSquareMilimiters">http://rs.rebipp.org.br/ppi/terms/stigmaticAreaInSquareMilimiters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/stigmaticAreaInSquareMilimiters-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/stigmaticAreaInSquareMilimiters-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Stigmatic Area In Square Milimiters</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total surface area in square millimeters of the stigma of a flower</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_styleLengthInMilimiters"></a>Term Name  ppi:styleLengthInMilimiters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/styleLengthInMilimiters">http://rs.rebipp.org.br/ppi/terms/styleLengthInMilimiters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/styleLengthInMilimiters-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/styleLengthInMilimiters-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Style Length In Milimiters</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The length in milimiters from the base to the tip of the style of a flower</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_visitedFlowerSex"></a>Term Name  ppi:visitedFlowerSex</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/visitedFlowerSex">http://rs.rebipp.org.br/ppi/terms/visitedFlowerSex</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/visitedFlowerSex-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/visitedFlowerSex-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Visited Flower Sex</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The sex of the visited flower</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ppi_visitedFlowersQuantity"></a>Term Name  ppi:visitedFlowersQuantity</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/visitedFlowersQuantity">http://rs.rebipp.org.br/ppi/terms/visitedFlowersQuantity</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-12-03</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.rebipp.org.br/ppi/terms/version/visitedFlowersQuantity-2021-12-03">http://rs.rebipp.org.br/ppi/terms/version/visitedFlowersQuantity-2021-12-03</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Visited Flowers Quantity</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The total number of flowers visited during the interaction</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Property</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.rebipp.org.br/decisions/decision-2022-01-06_1">http://rs.rebipp.org.br/decisions/decision-2022-01-06_1</a></td>
		</tr>
	</tbody>
</table>


