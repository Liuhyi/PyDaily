class Task:
    """Represents a simplistic Task (coroutine wrapper) to be executed."""

    def __init__(self, coro):
        self.coro = coro
        self.done = False

    def run(self):
        try:
            # Run the coroutine to the next yield
            next(self.coro)
        except StopIteration:
            self.done = True


class EventLoop:
    """A very basic event loop resembling a simplified asyncio loop."""

    def __init__(self):
        self.tasks = []

    def create_task(self, coro):
        """Wrap a coroutine in a Task and schedule it."""
        task = Task(coro)
        self.tasks.append(task)
        return task

    def run_until_complete(self):
        """Run the loop until all tasks are done."""
        while any(not task.done for task in self.tasks):
            for task in self.tasks:
                if not task.done:
                    task.run()


# Example coroutine functions
def coroutine_example(name, times):
    """A sample coroutine that prints and yields control."""
    for i in range(times):
        print(f"Coroutine {name} execution {i + 1}/{times}")
        yield  # Yield control back to the event loop


# Example usage of the loop and coroutine
def main():
    loop = EventLoop()
    loop.create_task(coroutine_example("A", 3))
    loop.create_task(coroutine_example("B", 2))
    loop.run_until_complete()

# Uncomment the following line to test the event loop implementation
main()
