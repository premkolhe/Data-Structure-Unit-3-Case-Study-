# Data-Structure-Unit-3-Case-Study-
A Python case study demonstrating stack and queue operations implemented with linked lists, including push, pop, enqueue, dequeue, and display operations.

# Stack and Queue Using Linked Lists

A Python case study for Unit 3: Stacks, Queues, and Linked Lists. It implements stack and queue operations using a singly linked list.

## Features

### Stack

- `push` adds an item to the top.
- `pop` removes the item from the top.
- `peek` displays the top item.
- `display` shows items from top to bottom.
- Follows **LIFO**: Last In, First Out.

### Queue

- `enqueue` adds an item to the rear.
- `dequeue` removes the item from the front.
- `peek` displays the front item.
- `display` shows items from front to rear.
- Follows **FIFO**: First In, First Out.

## Requirements

- Python 3.7 or newer
- No external packages required

## How to Run

Open a terminal in this folder and run:

```bash
python CaseStudy3.py
```

If your system uses `python3`, run:

```bash
python3 CaseStudy3.py
```

## Sample Output

See [`sample_output.txt`](sample_output.txt) for the complete output.

## Complexity

| Operation | Time |
|---|---:|
| Stack push | O(1) |
| Stack pop | O(1) |
| Stack peek | O(1) |
| Queue enqueue | O(1) |
| Queue dequeue | O(1) |
| Queue peek | O(1) |

Displaying all items takes **O(n)** time, where `n` is the number of items.

## Files

- `CaseStudy3.py` — Stack and queue implementation and demonstration.
- `README.md` — Project overview and run instructions.
- `sample_output.txt` — Example output from the program.