import json
from nltk import flatten


def find(file, key):
    """Recursion for fetching values from nested JSON."""

    f = open(file)
    data = json.load(f)
    arr = []
    output = []

    def closing():
        f.close()

    def cleaner(values):
        for i in values:
            if type(i) == list:
                cleaner(i)
            else:
                if i in output:
                    continue
                else:
                    output.append(i)
        return output

    def extract(data, arr, key):

        if isinstance(data, dict):
            for k, v in data.items():
                if not k != key:
                    arr.append(v)
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
            return arr

        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    if key in item.keys():
                        arr.append(item[key])
                    if not key in item.keys():
                        extract(item, arr, key)
            return arr
    values = extract(data, arr, key)
    # return values
    closing()
    return cleaner(values)


key = "password"
print(find('1.json', key))  # +++ ### >>> ['pass_1', 'qwerty']
print(find("2.json", key))  # +++ ### >>> ['1234qweQWE', 'pass_1', 'qwerty']
print(find("3.json", key))  # +++ ### >>> ["1234qweQWE"]
print(find("one_user_array_pass.json", key))  # +++ ### >>> ['_00_', 'try']
