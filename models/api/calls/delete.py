from pydantic import BaseModel

class VapiDeleteCallResponse(BaseModel):
    """Vapi-specific response model for deleting a call."""
    success: bool = ...
    message: str | None = None
