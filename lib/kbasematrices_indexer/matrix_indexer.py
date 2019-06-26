import os
import json

from installed_clients.WorkspaceClient import Workspace


upa_delimeter = '.'


def _attributemapping_index(ws_url, upa, parent_upa):
    """"""
    ws = Workspace(ws_url)
    obj = ws.get_objects2({'objects': [{'ref': parent_upa + ";" + upa}]})['data'][0]
    data = obj['data']
    doc = {
        "attributes": [],
        "attribute_ontology_ids": [],
        "attribute_units": [],
        "attribute_unit_ontology_ids": [],
        "attribute_values": [],
        "attribute_value_ontology_ids": [],
        "instances": data['instances'],
        "num_attributes": len(data['attributes']),
        "num_instances": len(data['instances']),
    }
    for attr in data['attributes']:
        doc['attributes'].append(attr['attribute'])
        if 'attribute_ont_id' in attr:
            doc['attribute_ontology_ids'].append(attr['attribute_ont_id'])
        if 'unit' in attr:
            doc['attribute_units'].append(attr['unit'])
        if 'attribute_ont_id' in attr:
            doc['attribute_unit_ontology_ids'].append(attr['attribute_ont_id'])
        if 'categories' in attr:
            doc['attribute_values'].extend(attr['categories'].keys())
            doc['attribute_value_ontology_ids'].extend(
                x['attribute_ont_id'] for x in attr['categories'] if 'attribute_ont_id' in x)

    return {
        'doc': doc,
        'sub_id': str(upa_delimeter.join(list(upa.split('/')))),
        'sub_type': "atrrmapping"
    }


def matrix_indexer(ws_url, scratch, params):
    """"""
    with open(params['obj_data_path']) as fd:
        obj_data = json.load(fd)
    data = obj_data['data']

    upa = '/'.join([
        str(obj_data['info'][6]),
        str(obj_data['info'][0]),
        str(obj_data['info'][4])
    ])

    doc = {
        "matrix_type": obj_data['info'][2],
        "row_attributes": [],
        "col_attributes": [],
        "row_attribute_ontology_ids": [],
        "col_attribute_ontology_ids": [],
        "row_attribute_values": [],
        "col_attribute_values": [],
        "row_ids": data['data']['row_ids'],
        "col_ids": data['data']['col_ids'],
        "num_rows": len(data['data']['row_ids']),
        "num_columns": len(data['data']['col_ids']),
        "attributes": [f'{k}|{v}' for k, v in data.get('attributes', {}).items()]
    }

    sub_objects = []

    am_keys = ('attributes', 'attribute_ontology_ids', 'attribute_values')
    if 'row_attributemapping_ref' in data:
        row_data = _attributemapping_index(ws_url, data['row_attributemapping_ref'], upa)
        doc.update({f'row_{x}': row_data['doc'][x] for x in am_keys})
        sub_objects.append(row_data)
    if 'col_attributemapping_ref' in data:
        col_data = _attributemapping_index(ws_url, data['row_attributemapping_ref'], upa)
        doc.update({f'col_{x}': col_data['doc'][x] for x in am_keys})
        sub_objects.append(col_data)

    index = {
        'doc': doc,
    }

    output_path = os.path.join(scratch, "output.json")
    with open(output_path, "a") as fd:
        fd.write(json.dumps(index) + "\n")
        for sub_index in sub_objects:
            fd.write(json.dumps(sub_index) + "\n")

    return {'filepath': output_path}
