import sys
import time
import shutil


def withprogressbar(func):
    """yeild values from 0 to 100 to show progressbar of given function advances"""

    def _func_with_progress(*args, **kwargs):
        max_width, _ = shutil.get_terminal_size()

        #to make this decorator function interact with the decorated function while still runing use python generators
        #when the withprog function is called we will infact be calling this function and the first thing it will do is
        #call the decorated function.

        while True:
            try:
                #since the decorated function has a yield progress statement, every time it wants to progress it has to return a generator
                progress = next(gen)
                #Once the decorated function finished all the work it had to do, it will raise a StopIteration 
            except StopIteration as exc:
                sys.stdout.write('\n')
                return exc.value
            else:
                #build the actaul message so left over space can be used by progress bar
                message = '[%s] {}%%'.format(progress)
                #add three characters to cope with the %% and %s 
                bar_width = max_width - len(message) + 3

                filled = int(bar_width / 100 * progress)
                spaceleft = bar_width - filled                
                bar = '=' * filled + ' ' * spaceleft
                #ensure that when message is printed it will not move to a new line like print()
                sys.stdout.write((message+'\r') % bar)
                sys.stdout.flush()

    return _func_with_progress

#for the sake of the example make a function that waits 100s

#use the function as decorator so it can be used on any function
@withprogressbar
def wait(seconds):
    """waits given amount of seconds and then return how much it waited"""

    start = time.time()
    step = seconds / 100
    for i in range(1,101):
        time.sleep(step)
        #send % of progress to progress bar
        yield i
    
    #return how much time has passed since we started
    return time.time() - start


print('WAITED', wait(10))

