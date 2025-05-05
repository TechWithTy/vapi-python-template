from pydantic import BaseModel, Field
from typing import Optional, Dict
from ._enums import TranscriberProvider, ModelProvider, BackgroundSound, FirstMessageMode, CallStatus

class Transcriber(BaseModel):
    """Transcriber options."""
    provider: TranscriberProvider = Field(..., description="Available transcriber providers")
    model: str = Field(..., description="Model used for transcription")
    language: str = Field(..., description="Language code (e.g., 'en', 'bg')")
    smart_format: bool = Field(..., alias="smartFormat", description="Smart formatting options")
    keywords: list[str] = Field(..., description="Keywords to improve transcription accuracy")
    endpointing: Optional[int] = Field(None, description="Endpointing threshold")

class ModelFunction(BaseModel):
    """Function details for model tool."""
    name: str = Field(..., description="Name of the function")
    description: str = Field(..., description="Function description")
    parameters: Dict[str, str] = Field(..., description="Parameter properties")

class ServerDetails(BaseModel):
    """Server details for tool execution."""
    timeout_seconds: int = Field(..., alias="timeoutSeconds", description="Timeout for server requests")
    url: str = Field(..., description="Server URL")
    secret: str = Field(..., description="Server secret for authentication")

class ModelTool(BaseModel):
    """Assistant model tools."""
    async_: bool = Field(..., alias="async", description="Whether the tool runs asynchronously")
    messages: list[Dict[str, str]] = Field(..., description="Messages associated with the tool")
    type: str = Field(..., description="Type of tool (for example, DTMF tool)")
    function: ModelFunction = Field(..., description="Function details of the tool")
    server: ServerDetails = Field(..., description="Server details for tool execution")

class AssistantModel(BaseModel):
    """Assistant model."""
    assistant_id: Optional[str] = Field(None, alias="assistantID", description="Assistant ID")
    messages: list[Dict[str, str]] = Field(..., description="Messages exchanged by the assistant")
    tools: list[ModelTool] = Field(..., description="Tools that the assistant can use")
    tool_ids: list[str] = Field(..., alias="toolIds", description="List of tool IDs")
    provider: ModelProvider = Field(..., description="Available LLM providers")
    model: str = Field(..., description="Model identifier")
    temperature: float = Field(..., description="Temperature for model responses")
    knowledge_base: Optional[Dict[str, str]] = Field(None, alias="knowledgeBase", description="Optional knowledge base for model queries")
    max_tokens: int = Field(..., description="Maximum number of tokens for responses")
    emotion_recognition_enabled: bool = Field(..., alias="emotionRecognitionEnabled", description="Whether emotion recognition is enabled")
    num_fast_turns: int = Field(..., alias="numFastTurns", description="Number of fast-turns allowed")

class Voice(BaseModel):
    """Assistant voice options."""
    filler_injection_enabled: bool = Field(..., alias="fillerInjectionEnabled", description="Whether filler words like 'um' are injected")
    provider: str = Field(..., description="Voice provider")
    voice_id: str = Field(..., alias="voiceId", description="Voice identifier")
    speed: float = Field(..., description="Speed of the speech")
    chunk_plan: Dict[str, str] = Field(..., alias="chunkPlan", description="Plan for chunking voice output")

class Assistant(BaseModel):
    """Assistant configuration."""
    transcriber: Transcriber = Field(..., description="Transcriber options")
    model: AssistantModel = Field(..., description="Model options for the assistant")
    voice: Voice = Field(..., description="Voice options for the assistant")
    first_message_mode: FirstMessageMode = Field(..., alias="firstMessageMode", description="Defines who speaks first")
    recording_enabled: bool = Field(..., alias="recordingEnabled", description="Whether recording is enabled")
    hipaa_enabled: bool = Field(..., alias="hipaaEnabled", description="Whether HIPAA compliance is enabled")
    client_messages: list[str] = Field(..., alias="clientMessages", description="List of client messages")
    server_messages: list[str] = Field(..., alias="serverMessages", description="List of server messages")
    silence_timeout_seconds: int = Field(..., alias="silenceTimeoutSeconds", description="Timeout for silence before ending the call")
    max_duration_seconds: int = Field(..., alias="maxDurationSeconds", description="Maximum duration of the call in seconds")
    background_sound: BackgroundSound = Field(..., alias="backgroundSound", description="Background sound during the call")
    backchanneling_enabled: bool = Field(..., alias="backchannelingEnabled", description="Whether backchanneling ('mm-hmm') is enabled")
    background_denoising_enabled: bool = Field(..., alias="backgroundDenoisingEnabled", description="Whether background denoising is enabled")

class AssistantOverrides(BaseModel):
    """Assistant overrides for call configuration."""
    transcriber: Optional[Transcriber] = Field(None, description="Override transcriber options")
    model: Optional[Dict[str, str]] = Field(None, alias="model", description="Override model options")
    voice: Optional[Dict[str, str]] = Field(None, alias="voice", description="Override voice options")
    client_messages: Optional[list[str]] = Field(None, alias="clientMessages", description="Override client messages")
    server_messages: Optional[list[str]] = Field(None, alias="serverMessages", description="Override server messages")

class VapiCreateCallRequest(BaseModel):
    """Vapi-specific model for creating a call."""
    name: str = Field(..., description="The name of the call")
    assistant_id: Optional[str] = Field(None, alias="assistantId", description="Existing assistant ID if you're using an assistant that has already been created")
    assistant: Optional[Assistant] = Field(None, alias="assistant", description="Transient assistant data (used if assistantId is not provided)")
    assistant_overrides: Optional[AssistantOverrides] = Field(None, alias="assistantOverrides", description="Overrides for assistant or assistantId settings")
    squad_id: Optional[str] = Field(None, alias="squadId", description="Existing squad ID")
    squad: Optional[Dict[str, str]] = Field(None, alias="squad", description="Transient squad data (used if squadId is not provided)")
    phone_number_id: Optional[str] = Field(None, alias="phoneNumberId", description="Existing phone number ID")
    phone_number: Optional[Dict[str, str]] = Field(None, alias="phoneNumber", description="Transient phone number data (used if phoneNumberId is not provided)")
    customer_id: Optional[str] = Field(None, alias="customerId", description="Existing customer ID")
    customer: Optional[Dict[str, str]] = Field(None, alias="customer", description="Transient customer data (used if customerId is not provided)")
