import argparse
from pathlib import Path
from parser import load_xml
from extractor import flatten_xml
from utils import save_json

def main():
    BASE_DIR = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(
        description="Extract key-value pairs from an XML file."
    )
    parser.add_argument(
        "xml_file",
        help="Name of the XML file inside the data folder."
    )

    args = parser.parse_args()
    xml_path = BASE_DIR / "data" / args.xml_file
    if not xml_path.exists():
        parser.error(f"'{args.xml_file}' does not exist in the data folder.")

    root = load_xml(str(xml_path))
    data = flatten_xml(root)
    output_dir = BASE_DIR / "output"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "extracted.json"
    save_json(data, output_file)
    print(" XML Extraction Completed Successfully")
    print(f"{output_file}")


if __name__ == "__main__":
    main()