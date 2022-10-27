def build_xml_element(tag, content, **kwargs):
    result = "<" + tag
    for key in kwargs:
        result += " " + key + "=\"" + kwargs[key] + "\""
    result += ">" + content + "</" + tag + ">"
    return result

print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))