import importlib

IMPLEMENTATION_PATH = 'wot_api.models'
print('hub imported')


def invoke_implementation(function_name, arguments, request, device):
    import_path = IMPLEMENTATION_PATH + '.' + device

    implementation_spec = importlib.util.find_spec(import_path)
    found = implementation_spec is not None

    if found:
        implementation = importlib.import_module(import_path)
        method = getattr(implementation, function_name)
        return method()
    else:
        return 'Implementation Required for %s of device %s' % (function_name, device)
