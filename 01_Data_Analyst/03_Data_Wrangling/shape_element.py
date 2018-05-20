def shape_element(element, node_attr_fields=NODE_FIELDS, way_attr_fields=WAY_FIELDS,
                  problem_chars=PROBLEM_CHARS, default_tag_type='regular'):
    """Clean and shape node or way XML element to Python dict"""

    node_attribs = {}
    way_attribs = {}
    way_nodes = []
    tags = []  # Handle secondary tags the same way for both node and way elements

    # YOUR CODE HERE
    if element.tag == 'node':

        for field in node_attr_fields:
            node_attribs[field] = element.attrib[field]

        for tag in element.iter('tag'):
            if problem_chars.match(tag.attrib['k']):

                continue
            else:
                k_split = (tag.attrib['k']).split(':', 1)
                if len(k_split) == 1:
                    key = k_split[0]
                    type_ = default_tag_type
                else:
                    key = k_split[1]
                    type_ = k_split[0]

                tags.append({'id': element.attrib['id'],
                             'key': key,
                             'value': tag.attrib['v'],
                             'type': type_})

        return {'node': node_attribs, 'node_tags': tags}

    elif element.tag == 'way':

        for field in way_attr_fields:
            way_attribs[field] = element.attrib[field]

        for i, nodes in enumerate(element.iter('nd')):
            way_nodes.append({'id': way_attribs['id'],
                              'node_id': nodes.attrib['ref'],
                              'position': i})

        for tag in element.iter('tag'):
            if problem_chars.match(tag.attrib['k']):

                continue
            else:
                k_split = (tag.attrib['k']).split(':', 1)
                if len(k_split) == 1:
                    key = k_split[0]
                    type_ = default_tag_type
                else:
                    key = k_split[1]
                    type_ = k_split[0]

                tags.append({'id': element.attrib['id'],
                             'key': key,
                             'value': tag.attrib['v'],
                             'type': type_})

        return {'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': tags}
