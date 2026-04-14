from utils.struct import data_parser
from datetime import datetime, timedelta

def show(data):
    print('-'*52)
    print(f"{'ID':<5}", end="")
    print(f"{'Name':<40}", end="")
    print(f"{'Reviews':<15}")
    print('-'*73)
    date = 'review'
    status = 'status'
    now = datetime.today().strftime("%d-%m-%Y")
    count = 0
    for struct in data_parser(data):
        print(f"{struct.concept_id:<4} ", end="")
        print(f"{struct.name[:30] + '...' if len(struct.name) > 30 else struct.name :<39} ",end="")
        for item in struct.review_one, struct.review_two, struct.review_three:
            if  datetime.today() > datetime.strptime(item[date], "%d-%m-%Y")+timedelta(days=1) and item[status] == False:
                print(f"✗ {item[date][:5]} | ", end="")
            elif datetime.today() < datetime.strptime(item[date], "%d-%m-%Y"): 
                print(f"• {item[date][:5]} | ", end="")
            elif now == item[date] and item[status] == False: 
                print(f"○ {item[date][:5]} | ", end="")
            else:
                print(f"✓ {item[date][:5]} | ", end="")
        print()

