class Template:
    def __init__(self, theme_dir):
        self.template = ''
        self.item = ''
        self.link = ''
        self.assignment = ''

        self.items = []

        with open(f'{theme_dir}/template.html', 'r', encoding='utf-8') as file:
            self.template = file.read()
        
        with open(f'{theme_dir}/item.html', 'r', encoding='utf-8') as file:
            self.item = file.read()
        
        with open(f'{theme_dir}/link.html', 'r', encoding='utf-8') as file:
            self.link = file.read()
        
        with open(f'{theme_dir}/assignment.html', 'r', encoding='utf-8') as file:
            self.assignment = file.read()