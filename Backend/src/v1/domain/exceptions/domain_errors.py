class DomainError(Exception):
    def __init__(self, message: str = "Domain error") -> None:
        self.message = message
        super().__init__(self.message)


class UnauthorizedAccessError(DomainError):
    def __init__(self, message: str = "Unauthorized access") -> None:
        super().__init__(message)


class InjectionDetectedError(DomainError):
    def __init__(self, message: str = "Request blocked for security reasons") -> None:
        super().__init__(message)


class InvalidCitationError(DomainError):
    def __init__(self, message: str = "Invalid citation in response") -> None:
        super().__init__(message)


class RateLimitExceededError(DomainError):
    def __init__(self, message: str = "Rate limit exceeded", retry_after: int = 60) -> None:
        self.retry_after = retry_after
        super().__init__(message)