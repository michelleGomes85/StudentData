from FileProcessor import FileProcessor, FileError, EmptyFileError
from LineProcessor import LineProcessor
from Constants import Constants
from TextDialog import TextDialog

class InvalidDate(Exception):
    pass

def showReport(points_sum):
    
    text_dialog = TextDialog(Constants.Messages.TITLE) 
    
    text = Constants.Messages.NEW_LINE
    
    for key in sorted(points_sum.keys()):
        text += Constants.Messages.REPORT_HEADER.format(key[0] + Constants.Messages.SPACE + key[1], points_sum[key]) + Constants.Messages.NEW_LINE
        
    text_dialog.show_text(text)

def main():
    
    try:
        file_name = input(Constants.Messages.INPUT_PROMPT)

        processor = FileProcessor(file_name)
        line_processor = LineProcessor()

        points_sum = {}
        
        for line in processor.lines():
            
            words = line_processor.process_line(line)
            
            if len(words) != 3:
                raise InvalidDate(Constants.Errors.MALFORMED_LINE.format(line.strip()))
            
            first_name, last_name, points_str = words
            
            try:
                points = float(points_str)
            except ValueError:
                raise InvalidDate(Constants.Errors.INVALID_SCORE.format(points_str))
            
            student = (first_name, last_name)
            points_sum[student] = points_sum.get(student, 0) + points
            
        showReport(points_sum)
            
    except (FileError, EmptyFileError, InvalidDate) as e:
        text_dialog = TextDialog(Constants.Messages.TITLE) 
        text_dialog.show_error(str(e))

if __name__ == "__main__":
    main()
