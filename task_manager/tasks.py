from celery import shared_task
import pandas as pd
import os

from config import settings


@shared_task
def add(x, y):
    return x + y


@shared_task
def import_export_file(project_list):
    os.makedirs(os.path.join(settings.MEDIA_ROOT, 'exported'), exist_ok=True)
    path = os.path.join(settings.MEDIA_ROOT, "exported/project_list.xlsx")
    df = pd.DataFrame(project_list)
    # pasta vaqtga nisbatan type bosa iwlatadi
    for col in df.select_dtypes(include=['datetimetz']).columns:
        df[col] = df[col].dt.tz_localize(None)

    df.to_excel(path, index=False)

    return path
