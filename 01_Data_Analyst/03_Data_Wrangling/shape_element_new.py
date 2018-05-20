NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']



def get_tags(element):
    tags = []
    for tag in element.iter('tag'):
        if PROBLEM_CHARS.match(tag.attrib['k']):
            continue
        else:
            k_split = (tag.attrib['k']).split(':', 1)
            if len(k_split) == 1:
                key = k_split[0]
                type_ = 'regular'
            else:
                key = k_split[1]
                type_ = k_split[0]
            tags.append({'id': element.attrib['id'],
                         'key': key,
                         'value': tag.attrib['v'],
                         'type': type_})
    return tags


def shape_element(element, node_attr_fields=NODE_FIELDS, way_attr_fields=WAY_FIELDS):
    """Clean and shape node or way XML element to Python dict"""

    node_attribs = {}
    way_attribs = {}
    way_nodes = []

    if element.tag == 'node':

        for field in node_attr_fields:
            node_attribs[field] = element.attrib[field]

        return {'node': node_attribs, 'node_tags': get_tags(element)}

    elif element.tag == 'way':

        for field in way_attr_fields:
            way_attribs[field] = element.attrib[field]

        for i, nodes in enumerate(element.iter('nd')):
            way_nodes.append({'id': way_attribs['id'],
                              'node_id': nodes.attrib['ref'],
                              'position': i})

        return {'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': get_tags(element)}

