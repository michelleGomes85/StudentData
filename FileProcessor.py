
from Constants import Constants

class FileError(Exception):
    pass

class EmptyFileError(Exception):
    pass

class FileProcessor:
    
    def __init__(self, file_name):
        self.__file_name = file_name
        
    def read_file(self):
        try:
            with open(self.__file_name, "r") as file:
                lines = file.readlines()
                
                if not lines:
                    raise EmptyFileError(Constants.Errors.EMPTY_FILE)
                
                return lines
        except:
            raise FileError(Constants.Errors.FILE_NOT_FOUND)
        
    def lines(self):
        lines = self.read_file()
        
        for line in lines:
            yield line.strip()