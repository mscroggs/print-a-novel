import curses
import locale
from time import sleep

locale.setlocale(locale.LC_ALL, "")

scr = curses.initscr()

curses.start_color()
curses.use_default_colors()
curses.noecho()
curses.cbreak()
old = curses.curs_set(0)

scr.keypad(1)
scr.refresh()

script = "revenge-of-the-sith"

try:
    while True:
        rows, cols = scr.getmaxyx()

        with open(script) as f:
            txt = f.read()
        lines = [i.split() for i in txt.split("\n")]
        displayed = [""]
        for line in lines:
            for word in line:
                if len(displayed[-1]) + 1 + len(line) > cols - 6:
                    displayed.append("")
                    if len(displayed) > rows - 6:
                        displayed = displayed[1:]
                for c in word:
                    displayed[-1] += c

                    scr.clear()
                    for i, d in enumerate(displayed):
                        scr.addstr(3+i, 3, d)
                    scr.refresh()
                    sleep(0.05)
                displayed[-1] += " "

            displayed.append("")
            if len(displayed) > rows - 6:
                displayed = displayed[1:]

            sleep(0.05)
except KeyboardInterrupt:
    pass


curses.nocbreak()
curses.curs_set(old)
scr.keypad(0)
curses.echo()
curses.endwin()

