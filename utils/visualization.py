def print_data_structure(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            children = value.get('children', [])
            if children:
                print(' ' * indent + str(key))
                print_data_structure(children, indent + 4)
            else:
                print(' ' * indent + str(value))
    elif isinstance(data, list):
        for item in data:
            print_data_structure(item, indent)
    else:
        print(' ' * indent + str(data))
