
# OpenPB - Customizable Progress Bar for Python

OpenPB is a Python library that provides a customizable progress bar for tracking the progress of tasks in your scripts. It is easy to use, highly customizable, and suitable for various applications.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Function Reference](#function-reference)
- [Contributing](#contributing)
- [License](#license)

## Overview

OpenPB allows you to integrate a progress bar into your Python scripts, providing a visual representation of the progress of tasks. It offers customization options for appearance and additional features like percentage display and elapsed time.

## Usage

Create an instance of OpenPB, start, increment, and finish the progress bar as shown below:

## Function Reference

| Function              | Description                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| `__init__(...)`       | Initializes the OpenPB instance with parameters such as total iterations, length, prefix, etc.|
| `OpenPB_start()`      | Starts the progress bar and sets the start time.                                              |
| `OpenPB_finish()`     | Completes the progress bar and prints a newline.                                              |
| `OpenPB_increment(step=1)` | Increments the progress bar by the specified step.                                        |
| `OpenPB_set_prefix(new_prefix)` | Sets a new prefix for the progress bar.                                                |
| `OpenPB_update(iteration)` | Updates the progress bar based on the provided iteration.                               |

### Example:

```python
from openpb import OpenPB
import time

# Create an instance of OpenPB
progress_bar = OpenPB(total=100, length=50, prefix='Task', suffix='Complete', show_percentage=True)

# Start the progress bar
progress_bar.OpenPB_start()

# Perform your task with iterations
for i in range(100):
    # Simulate some work
    time.sleep(0.1)

    # Update the progress bar
    progress_bar.OpenPB_increment()

# Finish the progress bar
progress_bar.OpenPB_finish()
```

## Contributing

We welcome contributions! If you have ideas, bug reports, or feature requests, please create an issue. Pull requests are also encouraged.

## License

This project is licensed under the [MIT License](LICENSE).
