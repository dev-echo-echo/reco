from dataclasses import dataclass

def data_parser(data):
    @dataclass
    class Struct:
        concept_id: int = None
        name : str  = None
        date_added : str = None
        review_one: dict = None 
        review_two: dict = None 
        review_three: dict = None 

    for item in data:
        struct = Struct()     
        for key in item:
            if key == 'reviews':
                for i, review_status in enumerate(item['reviews']):
                    match i:
                        case 0:
                            struct.review_one=review_status
                        case 1:
                            struct.review_two=review_status
                        case 2:
                            struct.review_three=review_status
            else:
                struct.concept_id=item['id']
                struct.name=item['name']
                struct.date_added=item['date_added']
        yield struct

