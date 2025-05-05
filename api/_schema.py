# Dynamically import all VAPI types as globals using TypesConfig
import importlib
import sys
from pathlib import Path

from ._types import TypesConfig

print(f"[DEBUG] sys.path before modification: {sys.path}")
print(f"[DEBUG] Attempting to import modules using library_name='{TypesConfig.library_name}'")

_imported_types = {}

for filename in TypesConfig.types:
    module_name = f"{TypesConfig.library_name}.types.{Path(filename).stem}"
    if TypesConfig.conversion_method == "camel_case":
        class_name = "".join(
            part.capitalize() for part in Path(filename).stem.split("_")
        )
    else:
        class_name = Path(filename).stem
    print(f"[DEBUG] Importing: module_name='{module_name}', class_name='{class_name}'")
    try:
        mod = importlib.import_module(module_name)
        _imported_types[class_name] = getattr(mod, class_name)
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"[ERROR] Could not import {class_name} from {module_name}: {e}")

globals().update(_imported_types)

__all__ = list(_imported_types.keys())

# Exports for grouped access
VAPI_REQUEST_TYPES = [
    AddVoiceToProviderDto,
    ApiRequest,
    ApiRequestMethod,
    ApiRequestMode,
    ChatCompletionsDto,
    CloneVoiceDto,
]

VAPI_RESPONSE_TYPES = [
    AssistantPaginatedResponse,
    CallBatchResponse,
    CallLogsPaginatedResponse,
    CallPaginatedResponse,
    ChatServiceResponse,
    ClientMessage,
]
