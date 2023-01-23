class BaseBackend():

    def __init__(self) -> None:
        pass

    def render(self, filename):

        raise NotImplementedError(f"Backend does not implement render()")