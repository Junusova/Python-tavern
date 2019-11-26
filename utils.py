import os
from requests_toolbelt.multipart.encoder import MultipartEncoder
def format_multipart(*args, **kwargs):
    output = {}
    for key, value in kwargs.items():
        if key == 'boundary':
            continue
        if isinstance(value, dict):
            output[key] = (
                value['name'],
                open(os.path.dirname(os.path.abspath(__file__)) + value['path'], 'rb'),
                value['type']
            )
        else:
            output[key] = "{}".format(value)
    encoded = MultipartEncoder(fields=output, boundary=kwargs['boundary'])
    return encoded.to_string()
