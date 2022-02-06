# Package imports
import pandas as pd

# Project imports
from api.models import Book


def csv_to_db(file):
    """[Function to convert csv rows into Book objects]

    Args:
        file ([csv_file]): [Contains multiple csv of books with required columns.]
    """
    try:
        csv_file = pd.read_csv(file)
        csv_dict = csv_file.to_dict("records")
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
