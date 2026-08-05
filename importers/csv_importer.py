import csv


class CSVImporter:
    """Reads participant data from a CSV file."""

    @staticmethod
    def read(file_path):
        participants = []

        with open(file_path, newline="", encoding="utf-8-sig") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                name = row.get("name", "").strip()

                if not name:
                    continue

                seed = row.get("seed", "").strip()

                participant = {
                    "name": name,
                }

                if seed:
                    participant["seed"] = int(seed)

                participants.append(participant)

        return participants