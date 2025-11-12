import csv
import sqlite3

csv_path = "datasets/test_houses.csv"
db_path = "datasets/test_houses.db"
table_name = "test_houses"

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode = OFF;")
cur.execute("PRAGMA synchronous = OFF;")
cur.execute("PRAGMA cache_size = 100000;")

cur.execute(
    f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    Type TEXT,
    Region TEXT,
    MunicipalityCode INTEGER,
    Prefecture TEXT,
    Municipality TEXT,
    DistrictName TEXT,
    NearestStation TEXT,
    TimeToNearestStation TEXT,
    MinTimeToNearestStation REAL,
    MaxTimeToNearestStation REAL,
    FloorPlan TEXT,
    Area REAL,
    AreaIsGreaterFlag INTEGER,
    UnitPrice REAL,
    PricePerTsubo REAL,
    LandShape TEXT,
    Frontage REAL,
    FrontageIsGreaterFlag BOOLEAN,
    TotalFloorArea REAL,
    TotalFloorAreaIsGreaterFlag INTEGER,
    BuildingYear REAL,
    PrewarBuilding INTEGER,
    Structure TEXT,
    Use TEXT,
    Purpose TEXT,
    Direction TEXT,
    Classification TEXT,
    Breadth REAL,
    CityPlanning TEXT,
    CoverageRatio REAL,
    FloorAreaRatio REAL,
    Period TEXT,
    Year INTEGER,
    Quarter INTEGER,
    Renovation TEXT,
    Remarks TEXT,
    TradePrice REAL
);
"""
)

chunk_size = 10000
rows = []
with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, start=1):
        rows.append(tuple(row.values()))
        if i % chunk_size == 0:
            cur.executemany(f"INSERT INTO {table_name} VALUES ({','.join(['?']*len(row))})", rows)
            conn.commit()
            rows = []
            print(f"Inserted {i} rows...")

if rows:
    cur.executemany(f"INSERT INTO {table_name} VALUES ({','.join(['?']*len(rows[0]))})", rows)
    conn.commit()

conn.close()
print("Rows inserted successfully.")
