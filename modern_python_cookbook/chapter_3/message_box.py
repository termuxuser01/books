import curses
import textwrap
import itertools

#curses allows to draw textbased boxes on the screen
class MessageBox(object):
    @classmethod
    def show(cls, message, cancel=False, width=40):
        """Show a message with an Ok/Cancel dialog.

        Provide ``cancel=True`` argument to show a cancel button 
        too.
        Returns the user selected choice:

            - 0 = Ok
            - 1 = Cancel
        """
        dialog = MessageBox(message, width, cancel)
        return curses.wrapper(dialog._show)

    def __init__(self, message, width, cancel):
        self._message = self._build_message(width, message)
        self._width = width
        self._height = max(self._message.count('\n')+1, 3) + 6
        self._selected = 0
        self._buttons = ['Ok']
        if cancel:
            self._buttons.append('Cancel')

    def _build_message(self, width, message):i
    #wrap the actual text to allign text so it can be adjusted to the window
        lines = []
        for line in message.split('\n'):
            if line.strip():
                lines.extend(textwrap.wrap(line, width-4,                                             
                             replace_whitespace=False))
            else:
                lines.append('')
        return '\n'.join(lines)

    def _show(self, stdscr):
        """
        method then creates the actual box window, adds a border to it, and displays the message within it.
        """
        win = curses.newwin(self._height, self._width, 
                            (curses.LINES - self._height) // 2, 
                            (curses.COLS - self._width) // 2)
        win.keypad(1)
        win.border()
        textbox = win.derwin(self._height - 1, self._width - 3, 
                             1, 2)
        textbox.addstr(0, 0, self._message)
        return self._loop(win)

    def _loop(self, win):
        """
        draw the buttons with their own borders and loop (reprint the screen when user switches options with arrow keys
        """
        while True:
            for idx, btntext in enumerate(self._buttons):
                #delimit each box to use the same amount of space
                allowedspace = self._width // len(self._buttons)
                btn = win.derwin(
                    3, 10, 
                    self._height - 4, 
                    (((allowedspace-10)//2*idx) + allowedspace*idx 
                       + 2)
                )
                btn.border()
                flag = 0
                if idx == self._selected:
                    flag = curses.A_BOLD
                btn.addstr(1, (10-len(btntext))//2, btntext, flag)
            #draw the buttons on the screen
            win.refresh()

            key = win.getch()
            if key == curses.KEY_RIGHT:
                self._selected = 1
            elif key == curses.KEY_LEFT:
                self._selected = 0
            elif key == ord('\n'):
                return self._selected


if __name__ == '__main__':
    MessageBox.show('hello world\npress enter to continue')
    #check for user choices 
    if MessageBox.show('Are you sure?\n\npress enter to confirm',
                   cancel=True) == 0:
        print("Yeah! Let's continue")
    else:
        print("That's sad, hope to see you soon")
