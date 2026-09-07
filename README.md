# Basic Python Project

A minimal Python project with application code in `src/` and tests in `tests/`.

## Run

```powershell
# Pass a name directly
py -m src.basic_python.main Ada

# Print an uppercase greeting
py -m src.basic_python.main Ada --shout

# Or omit the name and the app will ask for one
py -m src.basic_python.main
```

## Test

```powershell
py -m unittest discover -s tests
```
