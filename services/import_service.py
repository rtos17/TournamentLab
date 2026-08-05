from pathlib import Path

from importers.csv_importer import CSVImporter


class ImportService:
    """Coordinates participant imports."""

    @staticmethod
    def import_participants(file_path):
        extension = Path(file_path).suffix.lower()

        if extension == ".csv":
            return CSVImporter.read(file_path)

        raise ValueError(f"Unsupported file type: {extension}")