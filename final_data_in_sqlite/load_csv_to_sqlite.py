import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlite_shema import UsaGov, engine

Session = sessionmaker(bind=engine)
session = Session()

# Read the merged csv file
csv_file_path = './merged_output/final_file.csv'
df = pd.read_csv(csv_file_path)

# Change df to list of dict then bulk insert into DB
data = df.to_dict(orient='records')
session.bulk_insert_mappings(UsaGov, data)

# Commit these changes
session.commit()
print(f"Loaded {len(df)} records into the database.")
