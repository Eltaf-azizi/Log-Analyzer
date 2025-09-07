
"""
Entry point for the log-analyzer-basic tool.
Run with: python -m src.main analyze --file data/sample.log ...
"""

import sys
from src.cli.args import build_parser
from src.cli.commands import run_analyze



def main():
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "analyze":
        run_analyzer(args)

    else:
        parser.print_help()


if __name == "__main__":
    main()