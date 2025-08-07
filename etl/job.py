# etl/job.py
def extract():
    return [1, 2, 3]

def transform(data):
    return [i * 2 for i in data]

def load(data):
    print(f"Loading data: {data}")

def run():
    data = extract()
    data = transform(data)
    load(data)

if __name__ == "__main__":
    run()
