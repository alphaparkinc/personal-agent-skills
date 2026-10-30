# -*- coding: utf-8 -*-
"""
Personal Agent Master Orchestrator FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentOrchestrator

mcp = FastMCP("personal-agent-skills")
orchestrator = PersonalAgentOrchestrator()

@mcp.tool()
def schedule_circadian_focus_blocks(
    tasks_json: str,
    circadian_peak_hour: float = 10.0,
    current_hrv_readiness: float = 0.85
) -> str:
    """
    Schedules cognitive tasks dynamically matched against user circadian energy curve.
    """
    tasks = json.loads(tasks_json)
    res = orchestrator.schedule_circadian_focus_blocks(tasks, circadian_peak_hour, current_hrv_readiness)
    return json.dumps(res, indent=2)

@mcp.tool()
def fuse_multimodal_ambient_intent(
    screen_active_app: str,
    user_typing_wpm: float,
    calendar_minutes_to_next_meeting: int,
    unread_notifications_count: int
) -> str:
    """
    Fuses passive ambient desktop/mobile signals into inferred focus state and intervention policy.
    """
    res = orchestrator.fuse_multimodal_ambient_intent(
        screen_active_app, user_typing_wpm, calendar_minutes_to_next_meeting, unread_notifications_count
    )
    return json.dumps(res, indent=2)

@mcp.tool()
def evaluate_proactive_intervention_threshold(
    candidate_intervention: str,
    importance_score: float,
    user_focus_index: float,
    interruption_cost: float = 0.6
) -> str:
    """
    Decides whether an agent should proactively interrupt the user or defer to an ambient digest.
    """
    res = orchestrator.evaluate_proactive_intervention_threshold(
        candidate_intervention, importance_score, user_focus_index, interruption_cost
    )
    return json.dumps(res, indent=2)

def main():
    print("Testing Personal Agent Orchestrator FastMCP Server:")
    tasks = [{"id": "t1", "title": "Quarterly Budget Planning", "cognitive_load": 0.85}]
    print(schedule_circadian_focus_blocks(json.dumps(tasks)))

if __name__ == "__main__":
    main()
