from __future__ import annotations

from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..base import BaseCampaign


class CostBreakdown(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)
    transport: float = Field(..., alias="transport")
    stt: float = Field(..., alias="stt")
    llm: float = Field(..., alias="llm")
    tts: float = Field(..., alias="tts")
    vapi: float = Field(..., alias="vapi")
    total: float = Field(..., alias="total")
    llm_prompt_tokens: int = Field(..., alias="llmPromptTokens")
    llm_completion_tokens: int = Field(..., alias="llmCompletionTokens")
    tts_characters: int = Field(..., alias="ttsCharacters")


class ArtifactPlan(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)
    video_recording_enabled: bool = Field(..., alias="videoRecordingEnabled")
    recording_s3_path_prefix: str = Field(..., alias="recordingS3PathPrefix")


class AnalysisPlan(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)
    summary: str = Field(..., alias="summary")
    structured_data: dict[str, Any] = Field(..., alias="structuredData")
    success_evaluation: str = Field(..., alias="successEvaluation")


class Destination(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)
    type: str = Field(..., alias="type")
    number_e164_check_enabled: bool = Field(..., alias="numberE164CheckEnabled")
    number: str = Field(..., alias="number")
    extension: str | None = Field(None, alias="extension")
    message: str | None = Field(None, alias="message")
    description: str | None = Field(None, alias="description")


class Monitor(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)
    listen_url: str = Field(..., alias="listenUrl")
    control_url: str = Field(..., alias="controlUrl")


class ConversationMessage(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)
    data: dict[str, Any] = Field(..., alias="data")


class VapiCallDetail(BaseModel):
    """
    Full response model for a single call, as returned by the Vapi GET /call API.
    All fields and types match the official API docs for maximum compatibility.
    """
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)
    id: str = Field(..., alias="id")  # ! Unique identifier for the call
    org_id: str = Field(..., alias="orgId")  # ! Org that this call belongs to
    created_at: datetime = Field(..., alias="createdAt")  # ! When the call was created
    updated_at: datetime = Field(..., alias="updatedAt")  # ! When the call was last updated
    type: str | None = Field(None, alias="type")  # ! Type of call
    costs: list[dict] | None = Field(None, alias="costs")  # ! Costs of individual components (USD)
    messages: list[dict] | None = Field(None, alias="messages")  # ! Call messages
    phone_call_provider: str | None = Field(None, alias="phoneCallProvider")  # ! Provider (e.g., twilio)
    phone_call_transport: str | None = Field(None, alias="phoneCallTransport")  # ! Transport (e.g., sip)
    status: str | None = Field(None, alias="status")  # ! Status of the call
    ended_reason: str | None = Field(None, alias="endedReason")  # ! Why the call ended
    destination: dict | None = Field(None, alias="destination")  # ! Call transfer destination
    started_at: datetime | None = Field(None, alias="startedAt")  # ! When the call started
    ended_at: datetime | None = Field(None, alias="endedAt")  # ! When the call ended
    cost: float | None = Field(None, alias="cost")  # ! Total cost (USD)
    cost_breakdown: dict | None = Field(None, alias="costBreakdown")  # ! Cost breakdown (USD)
    artifact_plan: dict | None = Field(None, alias="artifactPlan")  # ! Assistant artifact plan (for POST /call/web)
    analysis: dict | None = Field(None, alias="analysis")  # ! Call analysis
    monitor: dict | None = Field(None, alias="monitor")  # ! Real-time monitor info
    artifact: dict | None = Field(None, alias="artifact")  # ! Artifacts created from the call
    phone_call_provider_id: str | None = Field(None, alias="phoneCallProviderId")  # ! Provider call ID (e.g., callSid)
    assistant_id: str | None = Field(None, alias="assistantId")  # ! Assistant used for the call
    assistant: dict | None = Field(None, alias="assistant")  # ! Assistant object (if transient)
    assistant_overrides: dict | None = Field(None, alias="assistantOverrides")  # ! Assistant/template variable overrides
    squad_id: str | None = Field(None, alias="squadId")  # ! Squad used for the call
    squad: dict | None = Field(None, alias="squad")  # ! Squad object (if transient)
    phone_number_id: str | None = Field(None, alias="phoneNumberId")  # ! Phone number used for the call
    phone_number: dict | None = Field(None, alias="phoneNumber")  # ! Phone number object (if transient)
    customer_id: str | None = Field(None, alias="customerId")  # ! Customer called (ID)
    customer: dict | None = Field(None, alias="customer")  # ! Customer object (if transient)
    name: str | None = Field(None, alias="name")  # ! Name of the call (<=40 chars)
    schedule_plan: dict | None = Field(None, alias="schedulePlan")  # ! Schedule plan for the call
    transport: dict | None = Field(None, alias="transport")  # ! Transport map


# GHL call response variant adds contact and campaign IDs


class DatabaseResponse(VapiCallDetail):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)
    contact_id: str = Field(..., alias="contactId")
    campaign_id: str = Field(..., alias="campaignId")


class CallList(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)
    calls: list[DatabaseResponse] = Field(..., alias="calls")


class CallCampaign(BaseCampaign):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)
    caller_number: str = Field(..., alias="callerNumber")
    receiver_number: str = Field(..., alias="receiverNumber")
    duration: int = Field(..., alias="duration")
    call_type: str = Field(..., alias="callType")
    ai_voice: str | None = Field(None, alias="aiVoice")
    company_campaignsuser_id: UUID = Field(..., alias="companyCampaignsuserId")
    call_details: list[DatabaseResponse] = Field(..., alias="callDetails")
