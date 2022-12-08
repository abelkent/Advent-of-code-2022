"""
AoC Day 7
"""

#Directory = array of data with extra bits
#File = tuple of 2 elements ("name",size)

working_dir = None

class directory():

    def __init__(self, name, parent = None, children = list(), files = list()):
        self.name = name
        self.parent = parent
        self.children = children
        self.files = files
    

    def add_file(self,data):
        self.files.append(data)
        
    def step_down(self, dir_name):
        global working_dir
        flag = False
        for child in self.children:
            if child.name == dir_name:
                working_dir = child
                flag = True
        
        if flag == False:
            child_dir = directory(dir_name,self)
            self.children.append(child_dir)
            working_dir = child_dir
            
        
    def step_up(self):
        global working_dir
        working_dir = self.parent
        
    
    def get_size(self):
        
        size = 0
        
        for file in self.files:
            size += file[1]

        
        return size


root = directory("/")
working_dir = root
print(working_dir.name)
working_dir.step_down("personal")
working_dir.add_file(["file",500])
print(working_dir.get_size())
working_dir.step_up()
working_dir.add_file(["Another",100])
print(working_dir.get_size())
working_dir.step_down(("personal"))
print(working_dir.name)
print(working_dir.get_size())