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

print("Changing 6th level key:value pair into list format to 5th level")
list_item_1 = []
temp_key = None
for k, v in temp_dict['dependencies']['@types/express']['requires']['@types/server/nodes'].items():
    temp_key = k
[list_item_1.append(temp_key + ": " + k + ": " + v) for k, v in temp_dict['dependencies']['@types/express']['requires']['@types/server/nodes']['affect_version'].items()]
temp_dict['dependencies']['@types/express']['requires']['@types/server/nodes'] = list_item_1
for k, v in temp_dict['dependencies']['@types/express2']['requires']['@types/server/nodes'].items():
    temp_key = k
list_item_2 = []
[list_item_2.append(temp_key + ": " + k + ": " + v) for k, v in temp_dict['dependencies']['@types/express2']['requires']['@types/server/nodes']['affect_version'].items()]
temp_dict['dependencies']['@types/express2']['requires']['@types/server/nodes'] = list_item_2
print(temp_dict)
