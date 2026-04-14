import traceback
from datetime import datetime
from pathlib import Path

def crash_log(error, context):
    home = Path.home() 
    path = home/"myhome"/"review_time"/"logs"/"errors.log"
    date = datetime.now().strftime("%H:%M:%S")
    with open(path, 'a') as f:
        f.write("="* 30 + "\n")
        f.write(f"data: {date} \n")
        f.write(f"error type: {type(error).__name__}\n")
        f.write(f"context: \n")

        for key, value in context.items():
            f.write(f"  {key}:    {value}")

        f.write("traceback:\n")
        f.write(traceback.format_exc())
