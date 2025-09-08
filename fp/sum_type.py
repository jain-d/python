from enum import Enum

class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4

def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            converted_data = list(map(lambda a_list: list(map(lambda value: str(value), a_list)), data))
            return ("Pending...", converted_data)
        case CSVExportStatus.PROCESSING:
            converted_data = "\n".join(map(lambda line: ",".join(line), data))
            return ("Processing...", converted_data)
        case CSVExportStatus.SUCCESS:
            return ("Success!", data)
        case CSVExportStatus.FAILURE:
            converted_data = "\n".join(map(lambda line: ",".join(map(lambda element: str(element), line)), data))
            return ("Unknown error, retrying...", converted_data)
        case _:
            raise Exception("unknown export status")
