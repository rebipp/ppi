# Script to build Markdown pages that provide term metadata for simple vocabularies
# Steve Baskauf 2020-06-28 CC0
# This script merges static Markdown header and footer documents with term information tables (in Markdown) generated from data in the rs.tdwg.org repo from the TDWG Github site

# Note: this script calls a function from http_library.py, which requires importing the requests, csv, and json modules
import re
import requests   # best library to manage HTTP transactions
import csv        # library to read/write/parse CSV files
import json       # library to convert JSON to Python data structures
import pandas as pd

# -----------------
# Configuration section
# -----------------

# !!!! Note !!!!
# This is an example of a simple vocabulary without categories. For a complex example
# with multiple namespaces and several categories, see build-page-categories.ipynb

# This is the base URL for raw files from the branch of the repo that has been pushed to GitHub. In this example,
# the branch is named "pathway"
githubBaseUri = 'https://raw.githubusercontent.com/rebipp/rs.rebipp.org.br/master/'

headerFileName = 'termlist-header.md'
footerFileName = 'termlist-footer.md'
outFileName = '../../docs/cv/index.md'

# This is a Python list of the database names of the term lists to be included in the document.
termLists = ['cv']

# NOTE! There may be problems unless every term list is of the same vocabulary type since the number of columns will differ
# However, there probably aren't any circumstances where mixed types will be used to generate the same page.
vocab_type = 2 # 1 is simple vocabulary, 2 is simple controlled vocabulary, 3 is c.v. with broader hierarchy

# Terms in large vocabularies like Darwin and Audubon Cores may be organized into categories using tdwgutility_organizedInClass
# If so, those categories can be used to group terms in the generated term list document.
organized_in_categories = False

# If organized in categories, the display_order list must contain the IRIs that are values of tdwgutility_organizedInClass
# If not organized into categories, the value is irrelevant. There just needs to be one item in the list.
display_order = ['']
display_label = ['Vocabulary'] # these are the section labels for the categories in the page
display_comments = [''] # these are the comments about the category to be appended following the section labels
display_id = ['Vocabulary'] # these are the fragment identifiers for the associated sections for the categories

# ---------------
# Function definitions
# ---------------

# replace URL with link
#
def createLinks(text):
    def repl(match):
        if match.group(1)[-1] == '.':
            return '<a href="' + match.group(1)[:-1] + '">' + match.group(1)[:-1] + '</a>.'
        return '<a href="' + match.group(1) + '">' + match.group(1) + '</a>'

    pattern = '(https?://[^\s,;\)"]*)'
    result = re.sub(pattern, repl, text)
    return result

# 2021-08-06 Replace the createLinks() function with functions copied from the QRG build script written by S. Van Hoey
def convert_code(text_with_backticks):
    """Takes all back-quoted sections in a text field and converts it to
    the html tagged version of code blocks <code>...</code>
    """
    return re.sub(r'`([^`]*)`', r'<code>\1</code>', text_with_backticks)

def convert_link(text_with_urls):
    """Takes all links in a text field and converts it to the html tagged
    version of the link
    """
    def _handle_matched(inputstring):
        """quick hack version of url handling on the current prime versions data"""
        url = inputstring.group()
        return "<a href=\"{}\">{}</a>".format(url, url)

    regx = "(http[s]?://[\w\d:#@%/;$()~_?\+-;=\\\.&]*)(?<![\)\.,])"
    return re.sub(regx, _handle_matched, text_with_urls)

term_lists_info = []

frame = pd.read_csv(githubBaseUri + 'term-lists/term-lists.csv', na_filter=False)
for termList in termLists:
    term_list_dict = {'list_iri': termList}
    term_list_dict = {'database': termList}
    for index,row in frame.iterrows():
        if row['database'] == termList:
            term_list_dict['pref_ns_prefix'] = row['vann_preferredNamespacePrefix']
            term_list_dict['pref_ns_uri'] = row['vann_preferredNamespaceUri']
            term_list_dict['list_iri'] = row['list']
    term_lists_info.append(term_list_dict)

# Create column list
column_list = ['pref_ns_prefix', 'pref_ns_uri', 'term_localName', 'label', 'definition', 'usage', 'notes', 'term_modified', 'term_deprecated', 'type']
if vocab_type == 2:
    column_list += ['controlled_value_string']
elif vocab_type == 3:
    column_list += ['controlled_value_string', 'skos_broader']
if organized_in_categories:
    column_list.append('tdwgutility_organizedInClass')
column_list.append('version_iri')

# Create list of lists metadata table
table_list = []
for term_list in term_lists_info:
    # retrieve versions metadata for term list
    versions_url = githubBaseUri + term_list['database'] + '-versions/' + term_list['database'] + '-versions.csv'
    versions_df = pd.read_csv(versions_url, na_filter=False)

    # retrieve current term metadata for term list
    data_url = githubBaseUri + term_list['database'] + '/' + term_list['database'] + '.csv'
    frame = pd.read_csv(data_url, na_filter=False)
    for index,row in frame.iterrows():
        row_list = [term_list['pref_ns_prefix'], term_list['pref_ns_uri'], row['term_localName'], row['label'], row['definition'], row['usage'], row['notes'], row['term_modified'], row['term_deprecated'], row['type']]
        if vocab_type == 2:
            row_list += [row['controlled_value_string']]
        elif vocab_type == 3:
            if row['skos_broader'] =='':
                row_list += [row['controlled_value_string'], '']
            else:
                row_list += [row['controlled_value_string'], term_list['pref_ns_prefix'] + ':' + row['skos_broader']]
        if organized_in_categories:
            row_list.append(row['tdwgutility_organizedInClass'])

        # Borrowed terms really don't have implemented versions. They may be lacking values for version_status.
        # In their case, their version IRI will be omitted.
        found = False
        for vindex, vrow in versions_df.iterrows():
            if vrow['term_localName']==row['term_localName'] and vrow['version_status']=='recommended':
                found = True
                version_iri = vrow['version']
                # NOTE: the current hack for non-TDWG terms without a version is to append # to the end of the term IRI
                if version_iri[len(version_iri)-1] == '#':
                    version_iri = ''
        if not found:
            version_iri = ''
        row_list.append(version_iri)

        table_list.append(row_list)

# Turn list of lists into dataframe
terms_df = pd.DataFrame(table_list, columns = column_list)

terms_sorted_by_label = terms_df.sort_values(by='label')
terms_sorted_by_localname = terms_df.sort_values(by='term_localName')
terms_sorted_by_label

# generate the index of terms grouped by category and sorted alphabetically by lowercase term local name

text = '### 3.1 Index By Term Name\n\n'
text += '(See also [3.2 Index By Label](#32-index-by-label))\n\n'
for category in range(0,len(display_order)):
    text += '**' + display_label[category] + '**\n'
    text += '\n'
    if organized_in_categories:
        filtered_table = terms_sorted_by_localname[terms_sorted_by_localname['tdwgutility_organizedInClass']==display_order[category]]
        filtered_table.reset_index(drop=True, inplace=True)
    else:
        filtered_table = terms_sorted_by_localname
        filtered_table.reset_index(drop=True, inplace=True)

    for row_index,row in filtered_table.iterrows():
        curie = row['pref_ns_prefix'] + ":" + row['term_localName']
        curie_anchor = curie.replace(':','_')
        text += '[' + curie + '](#' + curie_anchor + ')'
        if row_index < len(filtered_table) - 1:
            text += ' |'
        text += '\n'
    text += '\n'
index_by_name = text

text = '\n\n'

# Comment out the following two lines if there is no index by local names
#text = '### 3.2 Index By Label\n\n'
#text += '(See also [3.1 Index By Term Name](#31-index-by-term-name))\n\n'
for category in range(0,len(display_order)):
    if organized_in_categories:
        text += '**' + display_label[category] + '**\n'
        text += '\n'
        filtered_table = terms_sorted_by_label[terms_sorted_by_label['tdwgutility_organizedInClass']==display_order[category]]
        filtered_table.reset_index(drop=True, inplace=True)
    else:
        filtered_table = terms_sorted_by_label
        filtered_table.reset_index(drop=True, inplace=True)

    for row_index,row in filtered_table.iterrows():
        if row_index == 0 or (row_index != 0 and row['label'] != filtered_table.iloc[row_index - 1].loc['label']): # this is a hack to prevent duplicate labels
            curie_anchor = row['pref_ns_prefix'] + "_" + row['term_localName']
            text += '[' + row['label'] + '](#' + curie_anchor + ')'
            if row_index < len(filtered_table) - 2 or (row_index == len(filtered_table) - 2 and row['label'] != filtered_table.iloc[row_index + 1].loc['label']):
                text += ' |'
            text += '\n'
    text += '\n'
index_by_label = text

decisions_df = pd.read_csv('https://raw.githubusercontent.com/rebipp/rs.rebipp.org.br/master/decisions/decisions-links.csv', na_filter=False)

# generate a table for each term, with terms grouped by category

# generate the Markdown for the terms table
text = '## 4 Vocabulary\n'
for category in range(0,len(display_order)):
    if organized_in_categories:
        text += '### 4.' + str(category + 1) + ' ' + display_label[category] + '\n'
        text += '\n'
        text += display_comments[category] # insert the comments for the category, if any.
        filtered_table = terms_sorted_by_localname[terms_sorted_by_localname['tdwgutility_organizedInClass']==display_order[category]]
        filtered_table.reset_index(drop=True, inplace=True)
    else:
        filtered_table = terms_sorted_by_localname
        filtered_table.reset_index(drop=True, inplace=True)

    for row_index,row in filtered_table.iterrows():
        text += '<table>\n'
        curie = row['pref_ns_prefix'] + ":" + row['term_localName']
        curieAnchor = curie.replace(':','_')
        text += '\t<thead>\n'
        text += '\t\t<tr>\n'
        text += '\t\t\t<th colspan="2"><a id="' + curieAnchor + '"></a>Term Name  ' + curie + '</th>\n'
        text += '\t\t</tr>\n'
        text += '\t</thead>\n'
        text += '\t<tbody>\n'
        text += '\t\t<tr>\n'
        text += '\t\t\t<td>Term IRI</td>\n'
        uri = row['pref_ns_uri'] + row['term_localName']
        text += '\t\t\t<td><a href="' + uri + '">' + uri + '</a></td>\n'
        text += '\t\t</tr>\n'
        text += '\t\t<tr>\n'
        text += '\t\t\t<td>Modified</td>\n'
        text += '\t\t\t<td>' + row['term_modified'] + '</td>\n'
        text += '\t\t</tr>\n'

        if row['version_iri'] != '':
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Term version IRI</td>\n'
            text += '\t\t\t<td><a href="' + row['version_iri'] + '">' + row['version_iri'] + '</a></td>\n'
            text += '\t\t</tr>\n'

        text += '\t\t<tr>\n'
        text += '\t\t\t<td>Label</td>\n'
        text += '\t\t\t<td>' + row['label'] + '</td>\n'
        text += '\t\t</tr>\n'

        if row['term_deprecated'] != '':
            text += '\t\t<tr>\n'
            text += '\t\t\t<td></td>\n'
            text += '\t\t\t<td><strong>This term is deprecated and should no longer be used.</strong></td>\n'
            text += '\t\t</tr>\n'

        text += '\t\t<tr>\n'
        text += '\t\t\t<td>Definition</td>\n'
        text += '\t\t\t<td>' + row['definition'] + '</td>\n'
        text += '\t\t</tr>\n'

        if row['usage'] != '':
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Usage</td>\n'
            text += '\t\t\t<td>' + convert_link(convert_code(row['usage'])) + '</td>\n'
            text += '\t\t</tr>\n'

        if row['notes'] != '':
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Notes</td>\n'
            text += '\t\t\t<td>' + convert_link(convert_code(row['notes'])) + '</td>\n'
            text += '\t\t</tr>\n'

        if (vocab_type == 2 or vocab_type == 3) and row['controlled_value_string'] != '': # controlled vocabulary
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Controlled value</td>\n'
            text += '\t\t\t<td>' + row['controlled_value_string'] + '</td>\n'
            text += '\t\t</tr>\n'

        if vocab_type == 3 and row['skos_broader'] != '': # controlled vocabulary with skos:broader relationships
            text += '\t\t<tr>\n'
            text += '\t\t\t<td>Has broader concept</td>\n'
            curieAnchor = row['skos_broader'].replace(':','_')
            text += '\t\t\t<td><a href="#' + curieAnchor + '">' + row['skos_broader'] + '</a></td>\n'
            text += '\t\t</tr>\n'

        text += '\t\t<tr>\n'
        text += '\t\t\t<td>Type</td>\n'
        if row['type'] == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property':
            text += '\t\t\t<td>Property</td>\n'
        elif row['type'] == 'http://www.w3.org/2000/01/rdf-schema#Class':
            text += '\t\t\t<td>Class</td>\n'
        elif row['type'] == 'http://www.w3.org/2004/02/skos/core#Concept':
            text += '\t\t\t<td>Concept</td>\n'
        else:
            text += '\t\t\t<td>' + row['type'] + '</td>\n' # this should rarely happen
        text += '\t\t</tr>\n'

        # Look up decisions related to this term
        for drow_index,drow in decisions_df.iterrows():
            if drow['linked_affected_resource'] == uri:
                text += '\t\t<tr>\n'
                text += '\t\t\t<td>Executive Committee decision</td>\n'
                text += '\t\t\t<td><a href="http://rs.rebipp.org.br/decisions/' + drow['decision_localName'] + '">http://rs.rebipp.org.br/decisions/' + drow['decision_localName'] + '</a></td>\n'
                text += '\t\t</tr>\n'

        text += '\t</tbody>\n'
        text += '</table>\n'
        text += '\n'
    text += '\n'
term_table = text

text = index_by_label + term_table

# read in header and footer, merge with terms table, and output

headerObject = open(headerFileName, 'rt', encoding='utf-8')
header = headerObject.read()
headerObject.close()

footerObject = open(footerFileName, 'rt', encoding='utf-8')
footer = footerObject.read()
footerObject.close()

output = header + text + footer
outputObject = open(outFileName, 'wt', encoding='utf-8')
outputObject.write(output)
outputObject.close()

print('done')