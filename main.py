#! /usr/bin/env python3 
from pathlib import Path
from datetime import datetime

from utils.load import load
from utils.save import  save
from utils.calculate_reviews import calculate_reviews
from utils.parser import parser
from utils.dispatcher import dispatcher

home = Path.home()
data_dir = home /'.local'/'share'/'reco'/'data'
data_dir.mkdir(parents=True, exist_ok=True)
path = home / data_dir / "data.json"
if not path.exists():
    path.write_text("[]")

var_today = datetime.today() 
reviews = calculate_reviews(var_today)

data: list = load(path)

args = parser()

arguments = {'name': args.add,
             'reviews': reviews,
             'data': data,
             'path': path,
             'save': save}

for key, func in dispatcher.items():
    if getattr(args, key, False):            
        func(arguments)
        break # ot prevent multiple commands from running at same time reco --add "x" --show 

