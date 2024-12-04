class Demo:
    """A simple demo class."""

    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        """Return a greeting message."""
        return f"Hello, {self.name}!" 