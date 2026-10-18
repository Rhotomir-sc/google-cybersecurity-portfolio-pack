"""Execute the documented SQL queries against an in-memory fixture."""
from pathlib import Path
import re
import sqlite3

case = Path(__file__).resolve().parents[1] / 'integrated-security-case'
with sqlite3.connect(':memory:') as connection:
    connection.executescript((case / 'sample-data/security-case.sql').read_text(encoding='utf-8'))
    queries = re.findall(r'```sql\s*\n(.*?)```', (case / '05-sql-security-analysis.md').read_text(encoding='utf-8'), re.S)
    if len(queries) != 7:
        raise SystemExit('Expected seven queries; review the reproduction guide.')
    for index, query in enumerate(queries, 1):
        cursor = connection.execute(query)
        print(f'\nQuery {index}')
        print(' | '.join(column[0] for column in cursor.description))
        for row in cursor:
            print(' | '.join(map(str, row)))
