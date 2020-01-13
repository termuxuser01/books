import shutil
import textwrap, itertools

#use shutil.get_terminal_size to get the size of the terminal windows for sizing matters and output formatting

def maketable(cols):
    #if it fails to get terminal size or the output is passed to something that isn't a terminal(eg a file) it will have a default fallback
    terms_size = shutil.get_terminal_size(fallback=(80, 24))
    #compute the size of the terminal window and divide it by the number of columns
    colsize = (terms_size.columns // len(cols)) - 3
    if colsize < 1:
        raise ValueError('Column too small')
    return '\n'.join(map(' | '.join, itertools.zip_longest(*[
        [s.ljust(colsize) for s in textwrap.wrap(col, colsize)] for col in cols
    ], fillvalue=' '*colsize)))



#now it is possible to print any text and adapt it to the terminal window being used

COLUMNS = 5

TEXT = ['Lorem ipsum dolor sit amet, consectetuer adipiscing elit. '
        'Aenean commodo ligula eget dolor. Aenean massa. '
        'Cum sociis natoque penatibus et magnis dis parturient montes, '
        'nascetur ridiculus mus'] * COLUMNS

print(maketable(TEXT))

    
