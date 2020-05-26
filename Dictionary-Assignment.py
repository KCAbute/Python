# Input json file:
temp_dict = {
    "name": "json-examples",
    "lockfileVersion": 1,
    "requires": True,
    "dependencies": {
        "@types/express": {
            "resolved": "https://registry.npmjs.org/@types/express/-/express-4.0.36.tgz",
            "integrity": "sha512-bT9q2eqH/E72AGBQKT50dh6AXzheTqigGZ1GwDiwmx7vfHff0bZOrvUWjvGpNWPNkRmX1vDF6wonG6rlpBHb1A==",
            "requires": {
                "@types/express-serve-static-core": "4.0.49",
                "@types/serve-static": "1.7.31",
                "@types/server/nodes": {
                    "affect_version": {
                        "version_1": "8.0.13",
                        "version_2": "8.0.14",
                        "version_3": "8.0.15",
                        "version_4": "8.0.16"
                    }
                }
            }
        },
        "@types/express2": {
            "resolved": "https://registry.npmjs.org/@types/node/-/node-8.0.13.tgz",
            "integrity": "sha512-Y3EAG7VA7NVNbZek/fjJtILnmTk/ZfpJuWZGDBqDZ1dVIxgJJJ82fXPW7pKnqyV9CD/9bcPOCi7eErUqGMHOrA==",
            "requires": {
                "@types/express-serve-static-core": "4.0.74",
                "@types/serve-static": "1.7.36",
                "@types/server/nodes": {
                    "affect_version": {
                        "version_1": "8.1.23",
                        "version_2": "8.1.44",
                        "version_3": "8.1.55",
                        "version_4": "8.1.76"
                    }
                }
            }
        }
    }
}

if "dict" in str(type(temp_dict)):
    print("temp_dict is of the type dictionary")

print("Changing 6th level key:value pair into list format to 5th level")


def flatten_dict(py_obj, key_string=''):
    if type(py_obj) == dict:
        keystring = key_string + ' : ' if key_string else key_string
        for k in py_obj:
            yield from flatten_dict(py_obj[k], keystring + str(k))
    else:
        yield key_string, py_obj


fifth_dict_to_list = []
for key_1, val_1 in temp_dict.items():
    if type(val_1) == dict:
        for key_2, val_2 in val_1.items():
            if type(val_2) == dict:
                for key_3, val_3 in val_2.items():
                    if type(val_3) == dict:
                        for k4, val_4 in val_3.items():
                            if type(val_4) == dict:
                                fifth_dict_to_list  .append(val_4)
var1 = {k: v for k, v in flatten_dict(fifth_dict_to_list[0])}
list_item_1 = []
[list_item_1.append(k + ' : ' + v) for k, v in var1.items()]
temp_dict['dependencies']['@types/express']['requires']['@types/server/nodes'] = list_item_1
var2 = {k: v for k, v in flatten_dict(fifth_dict_to_list[1])}
list_item_2 = []
[list_item_2.append(k + ' : ' + v) for k, v in var2.items()]
temp_dict['dependencies']['@types/express2']['requires']['@types/server/nodes'] = list_item_2
print(temp_dict)
