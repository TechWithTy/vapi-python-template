from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from .get import VapiCallDetail

class ListCallsQueryParams(BaseModel):
    """
    Query parameters for listing calls (GET /call) as per Vapi API documentation.
    All fields use TypeScript-compatible aliases for seamless API interop.
    """
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)
    id: str | None = Field(None, alias="id")  # ! Unique identifier for the call
    assistant_id: str | None = Field(None, alias="assistantId")  # ! Filter by assistant ID
    phone_number_id: str | None = Field(None, alias="phoneNumberId")  # ! Filter by phone number ID
    limit: int | None = Field(None, alias="limit")  # ! Maximum number of items to return (default 100)
    created_at_gt: datetime | None = Field(None, alias="createdAtGt")  # ! createdAt > value
    created_at_lt: datetime | None = Field(None, alias="createdAtLt")  # ! createdAt < value
    created_at_ge: datetime | None = Field(None, alias="createdAtGe")  # ! createdAt >= value
    created_at_le: datetime | None = Field(None, alias="createdAtLe")  # ! createdAt <= value
    updated_at_gt: datetime | None = Field(None, alias="updatedAtGt")  # ! updatedAt > value
    updated_at_lt: datetime | None = Field(None, alias="updatedAtLt")  # ! updatedAt < value
    updated_at_ge: datetime | None = Field(None, alias="updatedAtGe")  # ! updatedAt >= value
    updated_at_le: datetime | None = Field(None, alias="updatedAtLe")  # ! updatedAt <= value
    # todo: Add any new fields if Vapi API expands query parameters

class ListCallsResponse(BaseModel):
    """
    Response model for listing calls (GET /call).
    Returns a list of VapiCallDetail objects and the total count, matching the Vapi API response.
    """
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)
    calls: list[VapiCallDetail] = Field(..., alias="calls")  # ! List of call details, see VapiCallDetail for all fields
    total_count: int | None = Field(None, alias="totalCount")  # ! Total number of calls found
