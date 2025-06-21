# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Web Search Agent: Search the web for information using Google Search."""

import os
from google.genai import types

from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext

from .prompts import return_instructions_web_search
from google.adk.tools import google_search

def setup_before_agent_call(callback_context: CallbackContext) -> None:
    """Setup the agent."""
    pass  # No specific setup needed for web search agent

web_search_agent = Agent(
    model=os.getenv("WEB_SEARCH_AGENT_MODEL", "gemini-2.0-flash-001"),
    name="web_search_agent",
    instruction=return_instructions_web_search(),
    tools=[google_search],
    before_agent_callback=setup_before_agent_call,
    generate_content_config=types.GenerateContentConfig(temperature=0.2),
) 