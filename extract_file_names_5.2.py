
dict1 = {
    "name": "root",
    "contents":
        [
            {
                "name": "boot",
                "contents":
                    [
                        {
                            "name": "boot.img"
                        },
                        {
                            "name": "kernel.img"
                        },
                        {
                            "name": "loaders",
                            "contents":
                                [
                                    {
                                        "name": "file1.txt",
                                    },
                                    {
                                        "name": "file2.py"
                                    }
                                ]
                        }
                    ]
            },
            {
                "name": "/tmp",
                "contents":
                    [
                        {
                            "name": "file2.docx",
                        },
                        {
                            "name": "file3.doc",
                        },
                        {
                            "name": "folder1",
                            "contents":
                                [
                                    {
                                        "name": "file4.txt",
                                    },
                                    {
                                        "name": "file5.py"
                                    }
                                ]
                        }
                    ]
            }
        ]
}
print("input files: ", dict1)


def print_def(input_dict):
    for key, value in input_dict.items():
        if isinstance(value, list):
            list_itr(value)
        elif value.__contains__('.'):
            print(value)


def list_itr(input_list):
    for i in input_list:
        if isinstance(i, dict):
            print_def(i)
        elif i.__contains__('.'):
            print(i)


print("\nList of all the files from a dictionary : ")
print_def(dict1)
