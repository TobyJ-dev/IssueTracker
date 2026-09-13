from issue_parser import IssueParser
from issue_statistics import IssueStatistics
from summary_printer import SummaryPrinter


def main():

    parser = IssueParser("project_management/ISSUES.md")
    issues = parser.parse()

    statistics = IssueStatistics(issues)

    printer = SummaryPrinter(statistics)
    printer.print_summary()


if __name__ == "__main__":
    main()