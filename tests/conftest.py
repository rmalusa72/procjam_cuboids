import sys
import re

CYAN = "\033[36m"
RED = "\033[31m"
RESET = "\033[0m"


# This is a hook that pytest exposes at the end of its run
def pytest_terminal_summary(terminalreporter, exitstatus):
    terminalreporter.summary_stats()
    print("\n")
    failed_nodes = terminalreporter.stats.get("failed", [])
    [_print_failed_node(node) for node in failed_nodes]
    sys.exit(exitstatus)


#  Intended to print out the failing tests so they may be
#  run individually. (Ignores linting failures.)
def _print_failed_node(node):
    error = re.search("^E(.+)", node.longreprtext, re.MULTILINE)
    if error is None:
        return
    msg = error[1].strip()
    cmd = f"make test node={node.nodeid}"
    print(f"{RED}{cmd}{CYAN} # {msg}{RESET}")
