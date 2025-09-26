from CsvReader import CsvReader

if __name__ == "__main__":
    csv_url = "https://informer.com.ua/dut/python/import/st_gt.csv"
    csv_reader = CsvReader()
    data = csv_reader.read_data(csv_url)
    for row in data:
        print(row)
