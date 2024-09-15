import json, os
from lecture import Lecture, Assignment, Link
from template import Template

with open('config.json', 'r') as file:
    config = json.load(file)

folder_name = config['folder']
theme = config['theme_dir'] + '/' + config['theme']

template = Template(theme)

lecture_list = []

for entry in os.scandir(f"./{folder_name}"):
    if entry.is_dir():
        lecture = Lecture(os.path.basename(entry))
        for file in os.scandir(entry):
            basename = os.path.basename(file)
            if basename.endswith('.py'):
                link = Link(os.path.splitext(basename)[0], os.path.abspath(file))
                lecture.add_link(link)
            elif basename.endswith('.txt'):
                assignment = Assignment(os.path.splitext(basename)[0], os.path.abspath(file))
                lecture.add_assignment(assignment)
        lecture_list.append(lecture)

with open(f'{theme}/template.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

lecture_dom = []

for lecture in lecture_list:
    lecture_dom_item = template.item
    lecture_dom_item = lecture_dom_item.replace("{{ name }}", lecture.name)
    
    link_dom_list = []

    for link in lecture.links:
        link_dom_item = template.link
        link_dom_item = link_dom_item.replace("{{ url }}", link.url)
        link_dom_item = link_dom_item.replace("{{ name }}", link.name)
        link_dom_list.append(link_dom_item)
    
    lecture_dom_item = lecture_dom_item.replace("{{ links }}", ''.join(link_dom_list))
    
    assignment_dom_list = []

    for assignment in lecture.assignments:
        assignment_dom_item = template.assignment
        assignment_dom_item = assignment_dom_item.replace("{{ url }}", assignment.url)
        assignment_dom_item = assignment_dom_item.replace("{{ name }}", assignment.name)
        assignment_dom_list.append(assignment_dom_item)
       
    lecture_dom_item = lecture_dom_item.replace("{{ assignments }}", ''.join(assignment_dom_list))

    lecture_dom.append(lecture_dom_item)

course_dom = template.template
course_dom = course_dom.replace("{{ course_name }}", folder_name)
course_dom = course_dom.replace("{{ lectures }}", ''.join(lecture_dom))

print(course_dom)