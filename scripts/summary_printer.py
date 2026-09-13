from models import Status
from issue_statistics import IssueStatistics


class SummaryPrinter:

    TITLELINE = "°" * 80
    LINE = "=" * 80
    SUBLINE = "-" * 80

    def __init__(self, statistics: IssueStatistics):
        self.stats = statistics

    @staticmethod
    def progress_bar(percent: float, width: int = 20) -> str:
        filled = round(width * percent / 100)

        return (
            "█" * filled +
            "░" * (width - filled)
        )

    def print_summary(self):

        self.print_header()
        self.print_overview()
        self.print_status_summary()
        # self.print_progress()
        self.print_type_summary()
        self.print_high_priority()
        # self.print_oldest_pending()
        self.print_newest()
        print(self.LINE)
        self.print_in_progress()
        print(self.LINE)
        self.print_pending()

    def print_header(self):

        print(self.TITLELINE)
        print("DiscounTJer Issue Summary")
        print(self.TITLELINE)
        print()

        print(f"Total Issues: {self.stats.total_issues()}")
        print()

    def print_overview(self):

        print(self.SUBLINE)
        print("Issue Overview")
        print(self.SUBLINE)

        for issue in self.stats.overview():

            print(
                f"{issue.issue_id:<10}"
                f"{'✔' if issue.aiu else '✖':<5}"
                f"{issue.title:<55}"
                f"{issue.status.icon} {issue.status.label}"
            )

        print()

    def print_status_summary(self):

        counts = self.stats.status_counts()
        progress = self.stats.progress()

        print(self.SUBLINE)
        print(f"{'Status Summary':<45}Progress")
        print(self.SUBLINE)

        print(
            f"{'Pending:      ' + str(counts.get(Status.PENDING, 0)):<45}"
            f"|   {self.progress_bar(progress)}"
        )
        print(
            f"{'In Progress:  ' + str(counts.get(Status.IN_PROGRESS, 0)):<45}"
            f"|   {progress:.1f}%"
        )
        print(
            f"{'Done:         ' + str(counts.get(Status.DONE, 0)):<45}"
            f"|"
        )
        label = f"Won't Fix:    {counts.get(Status.WONT_FIX, 0)}"
        print(
            f"{label:<45}|"
        )

        print()

    def print_progress(self):

        progress = self.stats.progress()

        print(self.SUBLINE)
        print("Progress")
        print(self.SUBLINE)

        print(self.progress_bar(progress))
        print(f"{progress:.1f}%")

        print()

    def print_type_summary(self):

        print(self.SUBLINE)
        print("By Type")
        print(self.SUBLINE)

        for issue_type, count in sorted(
            self.stats.type_counts().items()
        ):
            print(f"{issue_type:<15}{count}")

        print()

    def print_high_priority(self):

        print(self.SUBLINE)
        print("High Priority")
        print(self.SUBLINE)

        status_order = {
            Status.DONE: 0,
            Status.PENDING: 1,
            Status.IN_PROGRESS: 2,
            Status.WONT_FIX: 3,
        }

        issues = sorted(
            self.stats.high_priority(),
            key=lambda issue: status_order.get(issue.status, 99)
        )

        previous_status = None

        for issue in issues:

            if previous_status is not None and issue.status != previous_status:
                print()

            print(
                f"{issue.issue_id:<10}"
                f"{'✔' if issue.aiu else '✖':<5}"
                f"{issue.title:<55}"
                f"{issue.status.icon} {issue.status.label}"
            )

            previous_status = issue.status

        print()

    def print_oldest_pending(self):

        print(self.SUBLINE)
        print("Oldest Pending")
        print(self.SUBLINE)

        for issue in self.stats.oldest_pending():

            print(
                f"{issue.issue_id:<10}"
                f"{issue.title}"
            )

        print()

    def print_newest(self):

        print(self.SUBLINE)
        print("Latest Issues")
        print(self.SUBLINE)

        for issue in self.stats.newest()[:5]:

            print(
                f"{issue.issue_id:<10}"
                f"{issue.title}"
            )

        print()
        
    def print_in_progress(self):

        issues = [
            issue
            for issue in self.stats.overview()
            if issue.status == Status.IN_PROGRESS
        ]

        print(f"Total Issues in progress: {len(issues)}")
        print()

        print(self.SUBLINE)
        print("Issue Overview")
        print(self.SUBLINE)

        for issue in issues:

            print(
                f"{issue.issue_id:<10}"
                f"{'✔' if issue.aiu else '✖':<5}"
                f"{issue.title:<55}"
                f"{issue.status.icon} {issue.status.label}"
            )

        print()
        
    def print_pending(self):

        issues = [
            issue
            for issue in self.stats.overview()
            if issue.status == Status.PENDING
        ]

        print(f"Total Pending Issues: {len(issues)}")
        print()

        print(self.SUBLINE)
        print("Pending Issue Overview")
        print(self.SUBLINE)

        for issue in issues:

            print(
                f"{issue.issue_id:<10}"
                f"{'✔' if issue.aiu else '✖':<5}"
                f"{issue.title:<55}"
                f"{issue.status.icon} {issue.status.label}"
            )

        print()