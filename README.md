# AI Chat Assistant using Google Gemini
A chat assistant built end-to-end: a frontend that validates and formats user
input, a backend that routes and re-validates the request, and an API layer that
builds context, assembles the prompt, runs inference, and returns a response.

## Architecture Diagram

```mermaid
flowchart TD
    A["USER INPUT"]
    B["FRONTEND PROCESSING
    - input validation
    - state management
    - JSON formatting"]
    C["BACKEND PROCESSING
    - route header
    - data validation
    - service call"]
    D["API PROCESSING PIPELINE
    1. context building
    2. prompt engineering
    3. model inference
    4. response generation"]

    A --> B
    B -->|"HTTP POST api/v1/chat"| C
    C --> D
```
## System Architecture
**Frontend (React):**
-> captures user input
-> displays AI responses
-> handles real-time interactions

**Backend (Python):**
-> processes requests
-> manages API calls
-> handles business logic

**AI Layer (Gemini):**
-> generaters intelligent responses
-> processes natural language
-> provides AI capabilities

## State Diagram 

### States

| State | Meaning |
| --- | --- |
| VALIDATING | input validation and formatting |
| PROCESSING | AI API call in progress |
| RESPONDING | displaying AI response |


```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Validating : submit(message)
    Validating --> Processing : [valid]
    Validating --> Error : [invalid]
    Processing --> Responding : success()
    Processing --> Error : error()
    Responding --> Idle : complete()
    Error --> Validating : retry()
    Error --> Idle : reset()
    Idle --> [*] : closeSession()
```
