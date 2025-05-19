# AI Secretary - MVP Architecture (Calendar & Agent)

## System Overview

This document outlines the minimalist MVP architecture for an AI secretary system focused primarily on calendar management and agent functionality. Other features (email, fitness coaching, etc.) are included as placeholders for future development.

**Core Technologies:**
- **Frontend**: Next.js (React framework)
- **Backend**: Python (FastAPI)
- **Database**: Supabase (PostgreSQL) - without Auth for MVP
- **AI Orchestration**: LangChain
- **Models**: OpenAI GPT-4 / Anthropic Claude

## Architecture Diagram

```
┌───────────────────┐     ┌────────────────────────┐     ┌────────────────────┐
│                   │     │                        │     │                    │
│  Next.js Frontend │◄────►  Python FastAPI Backend│◄────►  Supabase          │
│                   │     │                        │     │  (PostgreSQL)      │
└───────────────────┘     └────────────────────────┘     └────────────────────┘
         ▲                            ▲                             
         │                            │                             
         ▼                            ▼                             
┌───────────────────┐     ┌────────────────────────┐     ┌────────────────────┐
│                   │     │                        │     │                    │
│  External APIs    │     │  LangChain Agent      │     │  AI Models         │
│  (Google, MS365)  │◄────►  Orchestration        │◄────►  (OpenAI/Anthropic) │
│                   │     │                        │     │                    │
└───────────────────┘     └────────────────────────┘     └────────────────────┘
```

## File & Folder Structure (MVP Focus)

```
project-root/
│
├── frontend/                  # Next.js application
│   ├── public/                # Static assets
│   ├── src/
│   │   ├── app/               # Next.js App Router
│   │   │   ├── page.tsx       # Landing page
│   │   │   ├── dashboard/     # Simple dashboard
│   │   │   └── calendar/      # Calendar views (MVP FOCUS)
│   │   ├── components/        # Reusable UI components
│   │   │   ├── layout/        # Layout components
│   │   │   ├── calendar/      # Calendar components (MVP FOCUS)
│   │   │   └── common/        # Shared components
│   │   ├── hooks/             # Custom React hooks
│   │   │   └── useCalendar.ts # Calendar hook (MVP FOCUS)
│   │   ├── lib/               # Utility functions & API clients
│   │   │   └── api.ts         # API client
│   │   ├── services/          # Frontend services
│   │   │   └── calendar.ts    # Calendar service (MVP FOCUS)
│   │   └── types/             # TypeScript type definitions
│   ├── tailwind.config.js     # Tailwind CSS configuration
│   └── package.json           # Frontend dependencies
│
├── backend/                   # Python FastAPI application
│   ├── app/
│   │   ├── main.py            # Entry point
│   │   ├── api/               # API endpoints
│   │   │   ├── routes/        # Route definitions
│   │   │   │   └── calendar.py # Calendar routes (MVP FOCUS)
│   │   │   └── dependencies.py # Dependency injection
│   │   ├── core/              # Core application code
│   │   │   ├── config.py      # Configuration
│   │   │   └── errors.py      # Error handling
│   │   ├── db/                # Database
│   │   │   ├── session.py     # Supabase session
│   │   │   └── models/        # Data models (simple for MVP)
│   │   ├── services/          # Business logic services
│   │   │   └── calendar/      # Calendar integration (MVP FOCUS)
│   │   ├── agents/            # LangChain agent definitions
│   │   │   ├── secretary.py   # Secretary agent (MVP FOCUS)
│   │   │   └── tools/         # Custom agent tools for calendar
│   │   └── schemas/           # Pydantic schemas
│   └── requirements.txt       # Python dependencies
│
├── .env.example               # Example environment variables
└── README.md                  # Project documentation
```

## Component Details (MVP Focus)

### Frontend (Next.js)

#### Key Components

1. **Simple Dashboard (`/src/app/dashboard/`)**
   - Basic overview of calendar events
   - Entry point to calendar features
   - Minimal UI with focus on functionality

2. **Calendar Interface (`/src/app/calendar/`)**
   - Interactive calendar view
   - Event creation/editing
   - Scheduling assistant interface
   - Connection to external calendars (Google/Microsoft)

#### State Management

- **Local State**: React hooks (useState, useReducer)
  - Component-specific UI states
  - Form data handling

- **Server State**: React Query
  - Calendar API data fetching and caching
  - Simple state synchronization

### Backend (Python FastAPI)

#### Core Services

1. **Calendar Service (`/backend/app/services/calendar/`)**
   - Calendar integration with Google Calendar/Microsoft 365
   - Event creation, modification, deletion
   - Conflict detection and resolution
   - Basic scheduling algorithms

#### LangChain Agent Architecture

1. **Secretary Agent (`/backend/app/agents/secretary.py`)**
   - Processes natural language calendar requests
   - Maintains conversation context
   - Extracts key scheduling information
   - Handles basic preferences

#### Custom Agent Tools

1. **Calendar Tools (`/backend/app/agents/tools/calendar_tools.py`)**
   - Schedule optimization algorithms
   - Conflict resolution
   - Free time detection
   - Calendar synchronization

### Database (Supabase)

#### Main Tables

1. **user_preferences** (minimal, no auth)
   - Basic user settings
   - Calendar preferences
   - Agent behavior settings

2. **calendar_events**
   - Event details
   - Associations with external calendars
   - Recurrence rules
   - Meta-information (creation source, etc.)

3. **calendar_connections**
   - External calendar connection details
   - API tokens (encrypted)
   - Sync status

#### Relationships

- user_preferences 1→n calendar_events
- user_preferences 1→n calendar_connections

*Note: Other components (email, fitness, etc.) will be implemented in future phases*

## Integration Flows (MVP)

### Calendar Integration Flow

1. User connects Google/Microsoft calendar (manual setup for MVP)
2. Access tokens stored in Supabase (encrypted)
3. Secretary agent processes natural language scheduling requests
4. Calendar service uses appropriate API to check availability
5. LangChain agent proposes optimal scheduling options
6. User confirms, and event is created across systems

## API Endpoints (MVP)

### Calendar Endpoints

- `GET /api/calendar/events` - Get calendar events
- `POST /api/calendar/events` - Create calendar event
- `PUT /api/calendar/events/{id}` - Update calendar event
- `DELETE /api/calendar/events/{id}` - Delete calendar event
- `POST /api/calendar/schedule` - AI scheduling assistant
- `GET /api/calendar/connections` - Get connected calendars
- `POST /api/calendar/connections` - Connect calendar

## Implementation Plan (MVP)

### Phase 1: Foundation (Week 1)

- Set up Next.js project
- Set up FastAPI backend
- Configure Supabase (minimal setup without auth)
- Establish basic API structure

### Phase 2: Calendar Integration (Week 2)

- Google Calendar API integration
- Microsoft 365 Calendar API integration
- Calendar CRUD operations
- Basic calendar visualization

### Phase 3: Agent Implementation (Week 3)

- LangChain setup
- Basic secretary agent for calendar management
- Natural language processing for scheduling
- Conflict detection logic

### Phase 4: UI & Testing (Week 4)

- Polished calendar UI
- Agent interaction interface
- Integration testing
- Bug fixes and optimizations

## Future Extensions (Post-MVP)

1. **Authentication System**
   - User registration and login
   - Secure session management
   - Role-based access control

2. **Email Management**
   - Email account integration
   - AI-assisted email handling
   - Follow-up management

3. **Fitness Coaching**
   - Workout planning
   - Progress tracking
   - Exercise recommendations

4. **Nutrition & Food Ordering**
   - Meal tracking
   - Restaurant order scheduling
   - Nutritional analysis

## Conclusion

This MVP architecture provides a focused approach to building an AI secretary system with calendar management as the core functionality. By limiting the scope to essential features, development time and complexity are significantly reduced while still delivering valuable functionality. The modular design allows for easy expansion to additional domains in future phases.
