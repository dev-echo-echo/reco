from datetime import datetime, timedelta

def calculate_reviews(start_data):
    review1 = start_data + timedelta(days=3)
    review2 = review1 + timedelta(days=7)
    review3 = review2 + timedelta(days=30)

    review_1 = {"review": review1.strftime('%d-%m-%Y'), "status": False}
    review_2 = {"review": review2.strftime('%d-%m-%Y'), "status": False}
    review_3 = {"review": review3.strftime('%d-%m-%Y'), "status": False}

    return [review_1, review_2, review_3]
