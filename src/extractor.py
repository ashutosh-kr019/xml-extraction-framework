from collections import Counter
from lxml.etree import QName

def flatten_xml(element, result=None, parent_path=""):
    if result is None:
        result = {}
    tag = QName(element).localname
    current_path = f"{parent_path}.{tag}" if parent_path else tag
    text = (element.text or "").strip()
    if text:
        result[current_path] = text
    child_counts = Counter(
        QName(child).localname
        for child in element
        if isinstance(child.tag, str)
    )

    seen = Counter()
    for child in element:
        if not isinstance(child.tag, str):
            continue
        child_tag = QName(child).localname
        seen[child_tag] += 1
        if child_counts[child_tag] > 1:
            next_parent = f"{current_path}.{child_tag}[{seen[child_tag]}]"
            flatten_xml_node(child, result, next_parent, indexed=True)
        else:
            flatten_xml_node(child, result, current_path, indexed=False)
    return result

def flatten_xml_node(element, result, parent_path, indexed):
    tag = QName(element).localname
    if indexed:
        current_path = parent_path
    else:
        current_path = f"{parent_path}.{tag}"

    text = (element.text or "").strip()
    if text:
        result[current_path] = text

    child_counts = Counter(
        QName(child).localname
        for child in element
        if isinstance(child.tag, str)
    )

    seen = Counter()
    for child in element:
        if not isinstance(child.tag, str):
            continue
        child_tag = QName(child).localname
        seen[child_tag] += 1
        if child_counts[child_tag] > 1:
            next_parent = f"{current_path}.{child_tag}[{seen[child_tag]}]"
            flatten_xml_node(child, result, next_parent, True)
        else:
            flatten_xml_node(child, result, current_path, False)