from utils.struct import data_parser  
from commands.today import today_review

def mark_done(data):
    status = 'status'
    ID = 'id'
    reviews = 'reviews'
    due_reviews = []
    for struct in data_parser(data):
        is_review, review_num = today_review(struct.review_one, struct.review_two, struct.review_three)
        if is_review != None and  is_review[status] == False:
            due_reviews.append({'id':struct.concept_id, 'name':struct.name, 'review_num':review_num})
        else:
            pass

    if not due_reviews:
        print("No reviews today or you reviewed all today's reviews")
    else:
        print("Today's due reviews:")
        print()
        right_ids = []
        for item in due_reviews:
            print(f"  [{item['id']}] {item['name']}")
            right_ids.append(item['id'])
        print()

        user_input = None
        while True: 
            try:
                user_input = int(input("Choose and ID to mark as done:"))
            except ValueError:
                # this is a weired way to quit.
                print("Please enter a valid value or -1 to quit")
            if user_input is not None and user_input in right_ids:
                for j, item in enumerate(due_reviews): 
                    current_review_num = due_reviews[j]['review_num']
                    for i, _dict in enumerate(data):
                        for key in _dict:
                            if data[i][ID] == user_input:
                                data[i][reviews][current_review_num][status] = True
                                continue
                break
            if user_input == -1:
                break
    return data
                            
