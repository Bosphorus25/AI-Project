from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import Request, HTTPException, FastAPI

# This function will handle validation errors thrown by FastAPI
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    request -> the incoming HTTP request (contains path, headers, method, etc.)
    exc -> the actual validation error raised by FastAPI (has .errors() method)
    """

    # Step 1: Collect all errors into a list
    errors = []
    for error in exc.errors():  
        """
        exc.errors() returns a list of dictionaries.
        Example:
        [
          {
            'loc': ('body', 'age'),
            'msg': 'value is not a valid integer',
            'type': 'type_error.integer'
          }
        ]
        Each dict tells:
          - where the error happened ("loc")
          - what went wrong ("msg")
          - the type/category of error
        """
        errors.append({
            "field": ".".join(map(str, error["loc"])),  
            # "loc" is usually a tuple like ('body', 'age') → we join it to "body.age"
            "message": error["msg"]  
            # A human-readable message, e.g. "value is not a valid integer"
        })

    # Step 2: Build a custom JSON response
    return JSONResponse(
        status_code=400,  
        # Validation errors are client mistakes → 400 Bad Request
        content={
            "status": "error",  
            "message": "Validation failed",  
            "errors": errors  
            # Our collected list of clean errors (so frontend can display them)
        }
    )


# Handle FastAPI HTTPException (like raise HTTPException(status_code=404, ...))
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "message": exc.detail,
            "errors": None
        }
    )


# Handle any unexpected exception (Python-level errors, not explicitly raised HTTPException)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "An unexpected error occurred",
            "errors": str(exc)
        }
    )

# bundling these handlers
def add_exception_handlers(app: FastAPI):
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)
