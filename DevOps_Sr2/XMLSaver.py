import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
from StudentData import StudentData
from DataSaver import DataSaver
from typing import Dict, Any


class XMLSaver(DataSaver):
    def __init__(self, data_aggregator: StudentData, filename_parts: Dict[str, str]):
        super().__init__(data_aggregator, filename_parts)

    @staticmethod
    def _dict_to_xml(tag: str, d: Dict[str, Any]) -> ET.Element:
        element = ET.Element(tag)
        for key, val in d.items():
            clean_key = key.replace(' ', '_').replace('.', '')

            if isinstance(val, dict):
                element.append(XMLSaver._dict_to_xml(clean_key, val))
            elif isinstance(val, list):
                list_element = ET.Element(clean_key)
                for item in val:
                    if isinstance(item, dict):
                        list_element.append(XMLSaver._dict_to_xml("Запис", item))
                    else:
                        item_elem = ET.Element("Елемент")
                        item_elem.text = str(item)
                        list_element.append(item_elem)

                element.append(list_element)
            else:
                child = ET.Element(clean_key)
                child.text = str(val) if val is not None else "N/A"
                element.append(child)
        return element

    def save(self) -> str:
        filename = self._generate_filename("xml")
        root = XMLSaver._dict_to_xml("StudentData", self._data_to_save)

        try:
            rough_string = ET.tostring(root, 'utf-8')
            reparsed = minidom.parseString(rough_string)
            pretty_xml = reparsed.toprettyxml(indent="  ", encoding="utf-8")

            with open(filename, 'wb') as f:
                f.write(pretty_xml)

            return os.path.abspath(filename)
        except Exception as e:
            raise Exception(f"Помилка при записі у файл XML {filename}: {e}")