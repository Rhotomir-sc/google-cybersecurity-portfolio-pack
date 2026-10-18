# Reproduce the examples

Requires Python 3.10+; standard library only. Run from the repository root. Substitute `python3` where needed.

## Integrated authentication case
```sh
python integrated-security-case/scripts/analyze_signin_case.py
python -m unittest discover -s integrated-security-case/tests -v
```

Expected: 12 events; one sequence for emma.lee@northstar.example from 198.51.100.23; six failures before the first matching success at 2026-09-10 08:15:19. Later successful application events are printed as context.

Options: `--input PATH --threshold 3 --window-minutes 10`.
The detector sorts timestamps, groups by user and IP, and requires failures strictly before success. A success resets the sequence. The time-window boundary is inclusive. Equal timestamps do not establish order; duplicate rows count separately. All timestamps must use one scenario timezone. This heuristic does not prove compromise.

## SQL
```sh
python tools/run_sql_case.py
```
Loads the fixture into in-memory SQLite and runs all seven queries from the [SQL investigation](integrated-security-case/05-sql-security-analysis.md). Expect six failures, three successes from the reviewed source, and five high/critical assets. No external database service is required.

## Module 7
```sh
python 07_Module-7_Automate-Cybersecurity-Tasks-with-Python/scripts/failed_login_analyzer.py
python 07_Module-7_Automate-Cybersecurity-Tasks-with-Python/scripts/ioc_extractor.py
python 07_Module-7_Automate-Cybersecurity-Tasks-with-Python/scripts/access_list_updater.py
```
The failed-login example counts events, not time-based bursts. The IOC extractor uses limited patterns on embedded text; matching text is not proof of maliciousness. The access-list example modifies an in-memory list, not a live control.

## Evidence boundaries
The network baseline still needs genuine local outputs. Historical screenshots are retained, not presented as new lab execution. Run the current commands for current output.
