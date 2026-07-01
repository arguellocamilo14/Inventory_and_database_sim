# CSV Inventory Manager

A command-line inventory management system built in Python. Products are stored
in a plain CSV file, so the whole app runs with **zero external dependencies** —
just the Python standard library.

> Built as a learning project to practice file I/O, OOP, and CLI design in Python.

## Features

- Add new products with name, price, and stock
- Register sales (with stock-availability checks)
- Update price or stock for an existing product
- Delete products
- View all current inventory in a simple table
- Analytics: total sales, total stock, total stock value, total revenue
- Inventory persists between runs as a human-readable `.csv` file

## Project Structure

```
.
├── main.py        # CLI loop — menu, user input, dispatches to inventary.py
├── inventary.py    # Domain logic — product/inventary/analytics classes
└── machine.py      # Storage layer — reads/writes the CSV file (Table class)
```

**Architecture overview:**

- **`machine.py`** is the only module that touches the filesystem. Its `Table`
  class knows how to read a CSV into a list of dicts, append a row, update a
  row in place, and delete a row.
- **`inventary.py`** translates between the CLI and the storage layer. The
  `product` class represents a single item; `inventary` handles
  add/sell/update/delete operations; `analytics` computes aggregate stats.
- **`main.py`** is purely the user interface — it loops on a numbered menu and
  calls into `inventary.py`.

## Requirements

- **Python 3.12 or newer.**
  `main.py`'s "view inventory" option uses an f-string with a nested quote of
  the same type (`f'{row['id']}'`), a syntax only supported from Python 3.12
  onward (PEP 701). Running it on 3.11 or earlier will raise a `SyntaxError`.

No `pip install` needed — only the built-in `csv` and `time` modules are used.

## Getting Started

```bash
git clone https://github.com/arguellocamilo14/Inventory_and_database_sim.git
cd Inventory_and_database_sim
python3 main.py
```

You'll be prompted for the CSV file to use. If it doesn't exist yet, it's
created automatically with the right headers:

```
Enter the .csv file path you will be working on: inventory.csv
```

## Usage

After launching, you'll see a menu:

```
----------------Store Manager----------------
Options available:
0 - View all current products
1 - Add a product
2 - Register a sale
3 - Update the price of a product
4 - Update the stock of a product
5 - Total sales
6 - Total stock
7 - Total stock value
8 - Total revenue
9 - Delete a product
10 - QUIT
----------------------------------------------
```
You will be asked to enter an option between 0 -10


Each product is identified by an auto-incrementing **id**, assigned when it's
created and shown in the "View all current products" table.

## CSV Data Format

Each row in the CSV represents one product:

| Column  | Type  | Description                          |
|---------|-------|---------------------------------------|
| id      | int   | Auto-assigned, starts at 0            |
| name    | str   | Product name                          |
| price   | float | Unit price                            |
| stock   | int   | Units currently in stock              |
| sales   | int   | Cumulative units sold                 |

## Known Limitations / Roadmap

- **Python 3.12+ only**, due to the nested-quote f-string in `main.py`'s view
  option (see [Requirements](#requirements)). Rewriting that line to avoid the
  nested quotes would make the project compatible with Python 3.11 and
  earlier.

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2026 arguellocamilo14

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
