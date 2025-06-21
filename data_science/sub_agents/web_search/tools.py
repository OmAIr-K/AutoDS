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

"""Tools for web search agent."""

from google.adk.tools import ToolContext
from google.adk.tools import google_search

async def search_web(
    query: str,
    tool_context: ToolContext,
) -> str:
    """Tool to search the web using Google Search.
    
    Args:
        query: The search query string
        tool_context: The tool context containing state and other information
        
    Returns:
        str: The search results as a formatted string
    """
    try:
        search_results = await google_search(query)
        formatted_results = format_search_results(search_results)
        return formatted_results
    except Exception as e:
        return f"Error performing web search: {str(e)}"

def format_search_results(results: list) -> str:
    """Format the search results into a readable string.
    
    Args:
        results: List of search results
        
    Returns:
        str: Formatted search results
    """
    if not results:
        return "No results found."
        
    formatted = "Web Search Results:\n\n"
    for i, result in enumerate(results, 1):
        formatted += f"{i}. {result.get('title', 'No title')}\n"
        formatted += f"   URL: {result.get('link', 'No URL')}\n"
        formatted += f"   Snippet: {result.get('snippet', 'No description')}\n\n"
    
    return formatted 