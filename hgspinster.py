import sys
import time

# Base class for spinners
class Spinner:
    def __init__(self, spinner_type='basic'):
        self.spinner_type = spinner_type
        self.spinner_frames = self.get_spinner_frames()

    def get_spinner_frames(self):
        """Define different types of spinners."""
        if self.spinner_type == 'arrow':
            return ['→', '↘', '↓', '↙', '←', '↖', '↑', '↗']
        elif self.spinner_type == 'bouncing_ball':
            width = 10
            return [f"[{' ' * i}o{' ' * (width - i)}]" for i in range(width)] + \
                [f"[{' ' * i}o{' ' * (width - i)}]" for i in range(width, 0, -1)]
        elif self.spinner_type == 'firework':
            return ['[   *   ]', '[  ***  ]', '[ ***** ]', '[*******]', '[ ***** ]', '[  ***  ]', '[   *   ]']
        elif self.spinner_type == 'matrix':
            return ['[101010101010]', '[010101010101]', '[101010101010]', '[010101010101]']
        elif self.spinner_type == 'heartbeat':
            return ['<3', '< 3', '<  3', '<   3', '<    3', '<     3']
        elif self.spinner_type == 'rocket':
            return ['🚀      ', ' 🚀     ', '  🚀    ', '   🚀   ', '    🚀  ', '     🚀 ', '      🚀']
        elif self.spinner_type == 'snake':
            return ['~', '~^', '~^~', '~^~^', '~^~^~', '^~^~^', '^~^~', '^~^', '^~']
        elif self.spinner_type == 'dna':
            return ['    A     T   ', '   A A   T T  ', '  A   A T   T ', ' A     A     T',
                    ' T     A     A', ' T   T A   A  ', '  T T   A A   ', '   T     A    ']
        elif self.spinner_type == 'fidget_spinner':
            return ['○○○', ' ◯◯◯', '  ◯◯◯', '   ◯○○', '    ◯○○', '     ○○◯', '      ○◯◯', '○◯◯    ']
        elif self.spinner_type == 'waterfall':
            return ['🌊     ', '  🌊   ', '    🌊 ', '      🌊', '    🌊 ', '  🌊   ', '🌊     ']
        elif self.spinner_type == 'pacman':
            return ['<o     ', '<oo    ', '<ooo   ', '<oooo  ', '<ooooo ', '< oooo', '<  ooo', '<   oo']
        elif self.spinner_type == 'meteor':
            return ['☄️      ', ' ☄️     ', '  ☄️    ', '   ☄️   ', '    ☄️  ', '     ☄️ ']
        elif self.spinner_type == 'moon':
            return ['🌑', '🌒', '🌓', '🌔', '🌕', '🌖', '🌗', '🌘']
        else:  # default is a simple line spinner
            return ['-', '\\', '|', '/']


    def spin(self, duration=5):
        """Run the spinner for a set amount of time (in seconds)."""
        start_time = time.time()
        while time.time() - start_time < duration:
            for frame in self.spinner_frames:
                sys.stdout.write(f'\r{frame}')
                sys.stdout.flush()
                time.sleep(0.2)
        sys.stdout.write('\rDone!\n')
        sys.stdout.flush()

# Subclass that adds progress percentage with ETA
class SpinnerWithProgress(Spinner):
    def spin_with_progress(self, current_task, total_tasks, start_time=None):
        """Run the spinner and display the progress along with ETA."""
        if start_time is None:
            start_time = time.time()
            
        while current_task <= total_tasks:
            for frame in self.spinner_frames:
                # Calculate progress
                progress = (current_task / total_tasks) * 100
                
                # Calculate ETA
                elapsed_time = time.time() - start_time
                if current_task > 0:
                    estimated_total_time = (elapsed_time / current_task) * total_tasks
                    eta = estimated_total_time - elapsed_time
                else:
                    eta = 0

                sys.stdout.write(f'\r{frame} {current_task}/{total_tasks} [{progress:.2f}%] ETA: {eta:.2f}s')
                sys.stdout.flush()
                time.sleep(0.2)
                current_task += 1

        sys.stdout.write('\rCompleted!\n')
        sys.stdout.flush()


# Example usage
if __name__ == '__main__':
    try:
        # List of spinner types to choose from
        spinner_types = ['basic', 'arrow', 'bouncing_ball', 'firework', 'matrix', 'heartbeat', 'rocket', 'snake']

        # Iterate over different spinner types
        for spinner_type in spinner_types:
            print(f"Spinner Type: {spinner_type}")
            
            # Basic spinner (no progress)
            basic_spinner = Spinner(spinner_type)
            basic_spinner.spin(duration=5)  # Spins for 5 seconds

            # Spinner with progress + ETA
            spinner_with_progress = SpinnerWithProgress(spinner_type)
            total_tasks = 50
            start_time = time.time()
            spinner_with_progress.spin_with_progress(1, total_tasks, start_time)  # Spins with progress + ETA

    except KeyboardInterrupt:
        sys.stdout.write('\rStopped\n')
        sys.stdout.flush()
