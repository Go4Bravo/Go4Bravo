import os
import csv
import xml.etree.ElementTree as ET

xmldir='/Users/jru/Documents/Digital Editions/Manifest'
savecsv='/Users/jru/Documents/eBooks/SavedTitles.csv'

def find_titles_in_directory(directory, csv_path):
    data = []
    
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            filepath = os.path.join(directory, filename)
            try:
                # Parse the XML file
                tree = ET.parse(filepath)
                root = tree.getroot()

                # Find the dc:title tag
                title = root.find('.//dc:title', namespaces={'dc': 'http://purl.org/dc/elements/1.1/'})
                title_text = title.text if title is not None else 'dc:title tag not found'
                
                # Add the filename and title to the data list
                data.append([filename, title_text])
            except ET.ParseError:
                print(f"Error parsing {filename}")
    
    # Write the data to the specified CSV file
    with open(csv_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Filename', 'Title'])
        csvwriter.writerows(data)

# Replace 'your_directory_path' with the path to your directory containing XML files
# Replace 'your_csv_path' with the desired path for the output CSV file
find_titles_in_directory(xmldir, savecsv)
