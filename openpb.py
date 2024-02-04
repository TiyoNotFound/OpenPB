import sys
import time

print("""
   ____                   _____  ____  
  / __ \                 |  __ \|  _ \\ 
 | |  | |_ __   ___ _ __ | |__) | |_) |
 | |  | | '_ \ / _ \ '_ \|  ___/|  _ < 
 | |__| | |_) |  __/ | | | |    | |_) |
  \____/| .__/ \___|_| |_|_|    |____/ 
        | |                            
        |_|                            
""")



class OpenPB:
    def __init__(self, total, length=40, prefix='OpenPB', suffix='Complete', fill='█', print_end='\r', show_percentage=True, show_elapsed_time=True):
        """Initialize the OpenPB instance."""
        self.total = total
        self.length = length
        self.prefix = prefix
        self.suffix = suffix
        self.fill = fill
        self.print_end = print_end
        self.show_percentage = show_percentage
        self.show_elapsed_time = show_elapsed_time
        self.start_time = None
        self.current_iteration = 0

    def _calculate_progress_info(self, iteration):
        percent = 100 * (iteration / float(self.total))
        filled_length = int(self.length * iteration // self.total)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        elapsed_time = time.time() - self.start_time if self.start_time else 0

        progress_info = f'{self.prefix} |{bar}|'

        if self.show_percentage:
            progress_info += f' {percent:.1f}%'

        if self.show_elapsed_time:
            progress_info += f' Elapsed Time: {elapsed_time:.2f}s'

        return progress_info

    def OpenPB_update(self, iteration):
        """Update the progress bar."""
        progress_info = self._calculate_progress_info(iteration)

        sys.stdout.write(f'\r{progress_info} {self.suffix}')
        sys.stdout.flush()

        if iteration == self.total:
            print()  # Move to the next line after completion

    def OpenPB_start(self):
        """Start the progress bar."""
        self.start_time = time.time()
        self.OpenPB_update(0)

    def OpenPB_finish(self):
        """Finish and complete the progress bar."""
        self.OpenPB_update(self.total)

    def OpenPB_increment(self, step=1):
        """Increment the progress bar by the specified step."""
        current_iteration = min(self.total, self.current_iteration + step)
        self.current_iteration = current_iteration
        self.OpenPB_update(current_iteration)

    def OpenPB_set_prefix(self, new_prefix):
        """Set a new prefix for the progress bar."""
        self.prefix = new_prefix
        self.OpenPB_update(self.current_iteration)