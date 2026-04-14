from commands.add import add
from commands.today import today
from commands.show import show
from commands.mark_done import mark_done
from commands.version import version

   
def handle_add(arguments):
    concept = add(
            name=arguments['name'], 
            reviews=arguments['reviews'] 
            )
    arguments['data'].append(concept)
    arguments['save'](arguments['data'], arguments['path'])
    print('done')

def handle_mark_done(arguments):
    mark = mark_done(arguments['data'])
    arguments['save'](mark, arguments['path'])

dispatcher = {
        'add': handle_add, 
        'today': lambda arguments: today(data=arguments['data']),
        'show': lambda arguments: show(data=arguments['data']),
        'mark': handle_mark_done,
        'version': version 
        }


