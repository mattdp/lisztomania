write_path_default_value = './todays_routine.org' #where to write the output, 
write_path = os.getenv('LIZTOMANIA_WRITE_PATH',write_path_default_value)

class Task:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.tags = kwargs.get('tags')
        self.note = kwargs.get('note')

def main():
    debug = True    
    default_depth = 3 #how many "*" to append to a top-level task
    formatted_output = ''

    tasks = []
    tasks.append(
        Task(id=1,title="basic class",tags=["red","weekday"],note="example\nnote\nwith\nnewlines")
    )

    for t in tasks:
        formatted_output += "*"*default_depth + t.title
        if t.note:
            formatted_output += "\n"+t.note+"\n"

    if debug:
        print(formatted_output)
    
    with open(write_path, 'w') as file:
        file.write(formatted_output)

main()