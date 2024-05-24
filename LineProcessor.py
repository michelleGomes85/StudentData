
class LineProcessor:
    
    def __init__(self, delimiter=' '):
        self.__delimiter = delimiter
        
    def process_line(self, line) :
        return line.split(self.__delimiter)