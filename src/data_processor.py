import csv


def csv_reader(file_path):
    """
    This function reads a CSV file and returns a list of dictionaries. Each
    dictionary represents a coordinate set that is row in the CSV file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = list(csv.DictReader(file))
        for row in data:
            row["Lat"] = float(row["Lat"])
            row["Long"] = float(row["Long"])
            row["Altitude"] = float(row["Altitude"])

        return data
