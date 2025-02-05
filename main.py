import json
import csv
import xml.etree.ElementTree as ET

def parse_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def parse_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return parse_xml_element(root)

def parse_xml_element(element):
    parsed_data = {}
    for child in element:
        if len(child):
            parsed_data[child.tag] = parse_xml_element(child)
        else:
            parsed_data[child.tag] = child.text
    return parsed_data

# Example usage
if __name__ == "__main__":
    json_data = parse_json('data.json')
    csv_data = parse_csv('data.csv')
    xml_data = parse_xml('data.xml')
    
    print("JSON Data:", json_data)
    print("CSV Data:", csv_data)
    print("XML Data:", xml_data)
