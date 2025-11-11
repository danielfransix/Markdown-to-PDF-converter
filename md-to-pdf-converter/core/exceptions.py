"""Custom exceptions for the markdown to PDF converter."""


class ConverterError(Exception):
    """Base exception for all converter-related errors."""
    pass


class FileNotFoundError(ConverterError):
    """Raised when a required file is not found."""
    def __init__(self, file_path: str):
        self.file_path = file_path
        super().__init__(f"File not found: {file_path}")


class ConversionError(ConverterError):
    """Raised when conversion from markdown to PDF fails."""
    def __init__(self, message: str, original_error: Exception = None):
        self.original_error = original_error
        if original_error:
            super().__init__(f"Conversion failed: {message}. Original error: {str(original_error)}")
        else:
            super().__init__(f"Conversion failed: {message}")


class InvalidMarkdownError(ConverterError):
    """Raised when markdown content is invalid or cannot be processed."""
    pass


class StyleError(ConverterError):
    """Raised when there's an issue with CSS styling."""
    pass