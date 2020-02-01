import curses
from curses.textpad import Textbox, rectangle

#make an input box for user to prompt when options are too long for command line 

#this uses the curses library that is only inclueded in linux so windows users will need to use alternatives
#such as Cygwin

class TextInput(object):
    @classmethod
    def show(cls, message, content=None):
        return curses.wrapper(cls(message, content)._show)

    def __init__(self, message, content):
        self._message = message
        self._content = content

    def _show(self, stdscr):
        #set reasonable size for input box
        lines, cols = curses.LINES - 10, curses.COLS - 40
        y_begin, x_begin = (curses.LINES - lines) / 2, (curses.COLS - cols) / 2

        editwin = curses.newwin(lines, cols, y_begin, x_begin)
        editwin.addsr(0, 1, "{}: Hit ctrl-G to submit)".format(self._message))
        rectangle(editwin, 1, 0, lines-2, cols-1)
        editwin.refresh()

        inputwin = curses.newwin(lines-4, cols-2, y_begin+2, x_begin+1)
        box = Textbox(inputwin)
        self._load(box, self._content)
        return self._edit(box)

    def load(self, box, text):
        if not text:
            return
        for c in text:
            box._insert_printable_char(c)

        def _edit(self, box):
            while True:
                ch = box.win.getch()
                if not ch:
                    continue
                if ch == 127:
                    ch = curses.KEY_BACKSPACE
                if not box.do_command(ch):
                    break
                box.win.refresh()
                

            return box.gather()



if __name__ == "__main__":
    result = TextInput._show('enter your name', 'please')
    print(f'your name is {result}')

