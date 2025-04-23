import os
from os.path import exists

import pandas as pd

from config import settings


# def import_export_file(project_list):
#     os.mkdir(os.path.join(settings.MEDIA_ROOT, 'exported'), exist_ok= True)
#     path = os.path.join("exported/project_list.xlsx")
#     df = pd.DataFrame(project_list)
#     df.to_excel(path, index=False)
#     return path





if __name__ == '__main__':
    import_export_file(
        [
            {
                "id": 3,
                "name": "project2",
                "description": "YES",
                "created_at": "2025-04-17T16:41:16.215246+05:00",
                "updated_at": "2025-04-17T16:57:03.087171+05:00",
                "owner": 1
            },
            {
                "id": 2,
                "name": "Ramazon Djamolov",
                "description": "asdasda",
                "created_at": "2025-04-16T12:16:45.326259+05:00",
                "updated_at": "2025-04-20T15:49:04.578044+05:00",
                "owner": 1
            }
        ]
    )
