# Python Programming Portfolio

This repository contains ten introductory Python programming exercises completed for **COMP502**. The tasks progress from variables and selection through loops, functions, collections, file handling, input validation, and Turtle graphics.

## Repository contents

| Path | Description |
| --- | --- |
| [`tasks/`](tasks/) | Ten independently runnable Python solutions and the data file used by Task 10 |
| [`docs/COMP502-Python-Assignment-Brief.pdf`](docs/COMP502-Python-Assignment-Brief.pdf) | Assignment requirements and marking guide |

## Tasks

| Task | File | Concepts demonstrated |
| --- | --- | --- |
| 1 | [`task_01_turtle_initial.py`](tasks/task_01_turtle_initial.py) | Turtle graphics, movement, and curves |
| 2 | [`task_02_circle_calculations.py`](tasks/task_02_circle_calculations.py) | User input, arithmetic, and the `math` module |
| 3 | [`task_03_pay_calculator.py`](tasks/task_03_pay_calculator.py) | Calculations and formatted output with f-strings |
| 4 | [`task_04_message_of_the_day.py`](tasks/task_04_message_of_the_day.py) | Multi-way selection with `if`, `elif`, and `else` |
| 5 | [`task_05_discount_eligibility.py`](tasks/task_05_discount_eligibility.py) | While loops, validation, and Boolean logic |
| 6 | [`task_06_turtle_circle_pattern.py`](tasks/task_06_turtle_circle_pattern.py) | Functions, loops, validation, and Turtle graphics |
| 7 | [`task_07_film_list.py`](tasks/task_07_film_list.py) | Lists, records, iteration, and tabular output |
| 8 | [`task_08_film_search.py`](tasks/task_08_film_search.py) | Functions, list processing, and record searching |
| 9 | [`task_09_budget_loss.py`](tasks/task_09_budget_loss.py) | Value-returning functions and aggregation |
| 10 | [`task_10_supermarket_records.py`](tasks/task_10_supermarket_records.py) | File I/O, data conversion, filtering, aggregation, and querying |

## Requirements

- Python 3.10 or later
- No third-party packages are required
- A graphical desktop environment is required for the two Turtle programs

## Running the programs

Run any task from the repository root. For example:

```bash
python3 tasks/task_04_message_of_the_day.py
python3 tasks/task_08_film_search.py
python3 tasks/task_10_supermarket_records.py
```

Tasks 1 and 6 open a Turtle graphics window:

```bash
python3 tasks/task_01_turtle_initial.py
python3 tasks/task_06_turtle_circle_pattern.py
```

Task 10 reads [`tasks/data.txt`](tasks/data.txt) and writes a local `backup.txt` file when executed. The generated backup file is intentionally excluded from version control.

## Skills demonstrated

- Clear variable naming and readable program structure
- Arithmetic calculations and formatted console output
- Conditional logic and defensive input validation
- `for` and `while` loops
- List-based record processing
- Reusable functions with parameters and return values
- Plain-text file reading and writing
- Basic exception handling
- Turtle-based graphical output

## Privacy

Student identification numbers and personal document metadata have been removed from the public portfolio materials.

## Academic integrity

This repository is provided as a personal learning portfolio. It should not be copied or submitted as another student's work.
