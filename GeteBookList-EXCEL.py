import os
import csv
import xml.etree.ElementTree as ET
import pandas as pd  

filename='epubXMLInfo'
xmldir='/Users/jru/Documents/Digital Editions/Manifest'
savecsv='/Users/jru/Documents/eBooks/'+filename+'.csv'

def find_tags_in_directory(directory, csv_path):
    data = []

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            filepath = os.path.join(directory, filename)
            try:
                # Parse the XML file
                tree = ET.parse(filepath)
                root = tree.getroot()

                # Define the namespaces
                namespaces = {'dc': 'http://purl.org/dc/elements/1.1/', 'dp': 'http://ns.adobe.com/digitalpublishing'}

                # Find the tags
                title = root.find('.//dc:title', namespaces)
                creator = root.find('.//dc:creator', namespaces)
                identifier = root.find('.//dc:identifier', namespaces)
                publisher = root.find('.//dc:publisher', namespaces)
                add_date = root.find('.//dp:addDate', namespaces)

                # Extract text or set default if not found
                title_text = title.text if title is not None else 'dc:title tag not found'
                creator_text = creator.text if creator is not None else 'dc:creator tag not found'
                identifier_text = identifier.text if identifier is not None else 'dc:identifier tag not found'
                publisher_text = publisher.text if publisher is not None else 'dc:publisher tag not found'
                add_date_text = add_date.text if add_date is not None else 'dp:addDate tag not found'

                # Add the data to the list
                data.append([filename, title_text, creator_text, identifier_text, publisher_text, add_date_text])
            except ET.ParseError:
                print(f"Error parsing {filename}")
    
    # Write the data to the specified CSV file
    with open(csv_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Filename', 'Title', 'Creator', 'Identifier', 'Publisher', 'Add Date'])
        csvwriter.writerows(data)
    # Convert CSV to Excel
        excel_file_path = csv_file_path.replace('.csv', '.xlsx')
        df = pd.read_csv(csv_file_path)
        df.to_excel(excel_file_path, index=False)

# Replace 'your_directory_path' with the path to your directory containing XML files
# Replace 'your_csv_path' with the desired path for the output CSV file
find_tags_in_directory(xmldir, savecsv)
