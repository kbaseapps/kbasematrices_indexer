import os
import json


def matrix_indexer(scratch, params):
	""""""
    with open(params['obj_data_path']) as fd:
        obj_data = json.load(fd)
    with open(params['ws_info_path']) as fd:
        ws_info = json.load(fd)
    with open(params['obj_data_v1_path']) as fd:
        obj_data_v1 = json.load(fd)

    data = obj_data['data']

    doc = {
        "matrix_type": obj['info'][2],
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
        "attributes": [f'{k}|{v}' for k, v in data['attributes'].items()]
    }

    am_keys = ('attributes', 'attribute_ontology_ids', 'attribute_values')
    if 'row_attributemapping_ref' in data:
        row_data = self.attributemapping_index(data['row_attributemapping_ref'])
        doc.update({f'row_{x}': row_data[x] for x in am_keys})
    if 'col_attributemapping_ref' in data:
        col_data = self.attributemapping_index(data['col_attributemapping_ref'])
        doc.update({f'col_{x}': col_data[x] for x in am_keys})

    index = {
        'doc': doc,
        # 'sub_type': ,
        # 'sub_id': ,
    }

    output_path = os.path.join(self.scratch, "output.json")
    with open(output_path, "a") as fd:
        fd.write(json.dumps(index))

    return {'filepath': output_path}
