JSON = {
{
    "email": "bri_riva@hotmail.com",
    "excel": {
        "filename": "reporte-test-002-A", # excede tamaño
        "webhook": "true",
        "sheets": [
            {
                "name": "LaHoja001",
                "columns": [
                    [
                        "column-1",
                        "int"
                    ],
                    [
                        "column-2",
                        "float"
                    ]
                ],
                "data": [
                    {
                        "column-1": 1,
                        "column-2": 11.93
                    },
                    {
                        "column-1": 2,
                        "column-2": 3.1416
                    }
                ]
            },
            {
                "name": "LaHoja002",
                "columns": [
                    [
                        "column-A",
                        "bool"
                    ],
                    [
                        "column-Z",
                        "list"
                    ]
                ],
                "data": [
                    {
                        "column-A": "true",
                        "column-z": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    {
                        "column-A": "true",
                        "column-z": [
                            "1",
                            "2"
                        ]
                    },
                    {
                        "column-A": "false",
                        "column-Z": [
                            "a"
                        ]
                    }
                ]
            }
        ]
    }
}
}