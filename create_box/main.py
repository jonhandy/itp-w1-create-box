"""This is the entry point of the program."""


def create_box(height, width, character):
    string = ""
    if height >= 1 and width >= 1:
        for h in range(height):
            for w in range(width):
                string += character
            string += "\n"
            
        return string
    else:
        return 'invalid size'
        
def empty_box(height, width, character):
    string = ""
    if height >= 3 and width >= 3:
        for h in range(height):
            if h == 0 or h == height - 1:
                for j in range(width):
                    string += character
                string += "\n"
            else:
                
                for w in range(width):
                    if w == 0 or w == width - 1:
                        string += character
                    else:
                        string += " "
                string += "\n"
            
        return string
    else:
        return 'invalid size'
    
        
    
        

if __name__ == '__main__':
    create_box(3, 4, '*')


