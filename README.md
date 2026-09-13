# Markdown Issue Tracker

A lightweight issue tracking system based on a single Markdown file.

Instead of using GitHub Issues or another issue tracker, issues are stored in `ISSUES.md` using a structured template. Python scripts parse the file, generate summaries, compute statistics, and export the data.

## Features

- Markdown-based issue tracker
- Strongly typed Issue model
- Automatic parser
- Issue statistics
- Console summary
- JSON export
- No external dependencies

## Folder Structure

```
project_management/
├── ISSUES.md
├── archive/
├── scripts/
│   ├── models.py
│   ├── issue_parser.py
│   ├── issue_statistics.py
│   ├── summary_printer.py
│   ├── issue_summary.py
│   └── issue_json_export.py
└── README.md
```

## Workflow

```
ISSUES.md
      │
      ▼
IssueParser
      │
      ▼
list[Issue]
      │
      ├─────────────┐
      ▼             ▼
Statistics      JSON Export
      │
      ▼
Summary Printer
```

## Usage

Print a summary:

```bash
python3 scripts/issue_summary.py
```

Export issues as JSON:

```bash
python3 scripts/issue_json_export.py
```

## Why Markdown?

- Human-readable
- Version-controlled
- Easy to edit
- Easy to review in pull requests
- No external service required

## Future Ideas

- HTML report
- CSV export
- Search and filtering
- Command-line interface
- Dependency graph
- Issue timeline