from datetime import datetime, timedelta
from utils.struct import data_parser


def today_review(review_one, review_two, review_three):
    now = datetime.today().strftime("%d-%m-%Y")
    rev = 'review'
    sta = 'status'
    iterations = 0
    for item in review_one, review_two, review_three:
        iterations += 1
        if item[rev] == now: 
            if iterations == 1:
                return item, 0 
            elif iterations == 2:
                return item, 1 
            else:
                return item, 2
    return None, None

def today(data: list[dict]):
    rev = 'review'
    sta = 'status'
    now = datetime.today().strftime("%d-%m-%Y")
    for struct in data_parser(data):
        is_review, review_num = today_review(struct.review_one, struct.review_two, struct.review_three)
        if is_review != None:
            print()
            print(f"ID[{struct.concept_id}] CONCEPT: {struct.name}")
            print()
            print("review:")
            # show less thing to reduce congnitive load=mental effort needed to understand something.
            if  datetime.today() > datetime.strptime(is_review[rev], "%d-%m-%Y")+timedelta(days=1) and is_review[sta] == False:
                print(f" [] {is_review[rev]:<12} (missed)")
            elif datetime.today() < datetime.strptime(is_review[rev], "%d-%m-%Y"): 
                print(f" []  {is_review[rev]:<12} (upcoming)")
            elif now == is_review[rev] and is_review[sta] == False: 
                print(f" [ ] {is_review[rev]:<12} (due)")
            else:
                print(f" []  {is_review[rev]:<12} (done)")
            print()

            if now == struct.review_one[rev]:
                    print(" -> First review: TODAY")
            elif now ==  struct.review_two[rev]:
                    print(" -> Second review: TODAY")
            elif now == struct.review_three[rev]:
                    print(" -> Last review: TODAY")

            print()
            print()


