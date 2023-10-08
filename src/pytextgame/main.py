from components.compartments import Room, Door

class Playground :
    def __init__(self, name, id = 0) :
        self.id = id
        self.name = name
        self.entry = None
        
    def activate(self, comps) :
        self.compartments = comps
        
    def create_entry_doors(self, dir_en, dir_ex, ex_lock) :
        self.entry_default = Door(self.entry, 'entry-door', dir_en, False)
        self.exit_default = Door(self.entry, 'exit-door', dir_ex, ex_lock)
        
    def create_start(self, objs) :
        self.start = Room(self, 'Start', [self.entry_default, self.exit_default], objs, self.exit_default.direction)
        
        
    

