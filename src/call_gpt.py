from openai import OpenAI
client = OpenAI()

def execute_query(question):

    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": """Given the following SQL tables, your job is to write queries given a user’s request.\n    \n    CREATE TABLE purchased_bonds (\n      Name_of_the_Purchaser VARCHAR(512),\n      Denominations DOUBLE,\n      purchase_date INT,\n      purchase_month VARCHAR(10),\n      purchase_year INT,\n      bond_no VARCHAR(10) PRIMARY KEY\n    );\n    \n    CREATE TABLE encashed_bonds (\n      Name_of_the_Political_Party VARCHAR(512),\n      Denominations DOUBLE,\n      Date INT,\n      Month VARCHAR(512),\n      Year INT,\n      bond_no VARCHAR(512) PRIMARY KEY,\n      FOREIGN KEY (bond_no) REFERENCES purchased_bonds(bond_no)\n    );"""
        },
        {
        "role": "user",
        "content": question
        }
    ],
    temperature=0,
    max_tokens=200,
    top_p=1
    )

    return response.choices[0].message.content