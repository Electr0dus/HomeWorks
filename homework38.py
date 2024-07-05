import inspect


def intospection_info(obj):
    dict_intospect = {}
    dict_intospect['type'] = type(obj)
    dict_intospect['attributes'] = dir(obj)
    dict_intospect['methods'] = inspect.getmembers(obj, inspect.ismethod)
    dict_intospect['module'] = inspect.getmodule(obj)

    return dict_intospect


number_info = intospection_info(42)
print(number_info)
