# Package imports
import pandas as pd

# Project imports
from api.models import Book


def csv_to_db(file):
    try:
        csv_file = pd.read_csv(file)
        csv_dict = csv_file.to_dict("records")
        print(csv_dict)
        csv_objects = [
            Book(
                title=row["title"],
                story=row["story"],
                user_id=row["user_id"],
            )
            for row in csv_dict
        ]
        objects = Book.objects.bulk_create(csv_objects)

    except Exception as err:
        print(str(err))
