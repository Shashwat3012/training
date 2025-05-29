import math
from typing import Final
from enum import Enum

# Module-level constants (UPPER_CASE naming convention)
MAX_CONNECTIONS: Final[int] = 100
DEFAULT_TIMEOUT: Final[float] = 30.0
API_BASE_URL: Final[str] = "https://api.example.com/v1"
SUPPORTED_FORMATS: Final[tuple] = ("json", "xml", "csv")



# Mathematical constants
PI: Final[float] = math.pi
EULER_NUMBER: Final[float] = math.e
GOLDEN_RATIO: Final[float] = (1 + math.sqrt(5)) / 2



# Class-based constants organization.
class ConfigConstants:    
    # Database configuration
    DB_HOST: Final[str] = "localhost"
    DB_PORT: Final[int] = 5432
    DB_NAME: Final[str] = "production"
    
    # Application settings
    DEBUG_MODE: Final[bool] = False
    LOG_LEVEL: Final[str] = "INFO"
    CACHE_DURATION: Final[int] = 3600  # seconds


# Enum for HTTP status codes - more robust than simple constants.
class StatusCodes(Enum):
    SUCCESS = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    NOT_FOUND = 404
    INTERNAL_ERROR = 500



# Show proper usage of constants in functions
def demonstrate_constants():
    print(f"Maximum allowed connections: {MAX_CONNECTIONS}")
    print(f"API endpoint: {API_BASE_URL}")
    print(f"Supported formats: {', '.join(SUPPORTED_FORMATS)}")
    
    # Using mathematical constants
    circle_area = PI * (5 ** 2)
    print(f"Area of circle (radius=5): {circle_area:.2f}")
    
    # Using class-based constants
    connection_string = f"postgresql://{ConfigConstants.DB_HOST}:{ConfigConstants.DB_PORT}/{ConfigConstants.DB_NAME}"
    print(f"Database connection: {connection_string}")
    
    # Using enum constants
    response_status = StatusCodes.SUCCESS
    print(f"HTTP Status: {response_status.name} ({response_status.value})")

if __name__ == "__main__":
    demonstrate_constants()