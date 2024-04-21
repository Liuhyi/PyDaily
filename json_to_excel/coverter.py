import openpyxl
import json


class Writer:
    def __init__(self, header, path="input.json", output_path="output.xlsx"):
        self.header = header
        self.json_file = path
        self.output_file = output_path
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active

    def parse_json(self):
        with open(self.json_file, 'r') as f:
            data = json.load(f)
        for d in data:
            row = []
            for field in self.header:
                value = str(d[field]) if d[field] else "None"
                row.append(value)
            yield row

    def write_json(self):
        self.ws.append(self.header)
        items = self.parse_json()
        for item in items:
            self.ws.append(item)
        self.wb.save(self.output_file)
        print(f"Data has been written to {self.output_file}")


if __name__ == '__main__':
    header = [
        "id", "full_name", "private", "html_url", "description",
        "homepage", "size", "stargazers_count", "language", "topics",
        "visibility", "forks"
    ]
    writer = Writer(header)
    writer.write_json()
