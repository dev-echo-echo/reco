import argparse

def parser(): 
    parser = argparse.ArgumentParser(description="reco - simple recall / spaced repetition CLI tool")

    parser.add_argument('-a','--add', type=str, help='Add a new concept')
    parser.add_argument('-s','--show', action='store_true', help='Show all conecpts [✓  Done, ✗  Missed,•  Upcoming, ○  Due]')
    parser.add_argument('-t','--today', action='store_true', help="Show today's reviews [✓  Done, ✗  Missed,•  Upcoming, ○  Due]")

    parser.add_argument('-m','--mark', action='store_true', help='Mark a review as done')
    parser.add_argument('-v','--version', action='store_true', help='Show version')

    args = parser.parse_args()
    return args






