import csv
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

def create_tally_xml(csv_file, xml_file):
    envelope = ET.Element("ENVELOPE")
    header = ET.SubElement(envelope, "HEADER")
    ET.SubElement(header, "TALLYREQUEST").text = "Import Data"
    
    body = ET.SubElement(envelope, "BODY")
    import_data = ET.SubElement(body, "IMPORTDATA")
    req_desc = ET.SubElement(import_data, "REQUESTDESC")
    ET.SubElement(req_desc, "REPORTNAME").text = "Vouchers"
    
    req_data = ET.SubElement(import_data, "REQUESTDATA")

    try:
        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tally_msg = ET.SubElement(req_data, "TALLYMESSAGE", xmlns_UDF="TallyUDF")
                voucher = ET.SubElement(tally_msg, "VOUCHER", VCHTYPE="Receipt", ACTION="Create")
                ET.SubElement(voucher, "DATE").text = row.get("Date", datetime.today().strftime('%Y%m%d'))
                ET.SubElement(voucher, "NARRATION").text = row.get("Narration", "Auto Imported Transaction")
                ET.SubElement(voucher, "PARTYLEDGERNAME").text = row.get("Ledger", "Suspense A/c")
                ET.SubElement(voucher, "AMOUNT").text = str(row.get("Amount", "0.00"))
    except FileNotFoundError:
        print(f"Error: {csv_file} not found. Generating sample XML structure...")

    tree = ET.ElementTree(envelope)
    ET.indent(tree, space="  ", level=0)
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
    print(f"Successfully generated Tally XML: {xml_file}")

if __name__ == "__main__":
    input_csv = sys.argv[1] if len(sys.argv) > 1 else "sample.csv"
    output_xml = sys.argv[2] if len(sys.argv) > 2 else "tally_import.xml"
    create_tally_xml(input_csv, output_xml)
  
