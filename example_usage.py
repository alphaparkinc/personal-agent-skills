# -*- coding: utf-8 -*-
"""
Demonstration of Personal Agent Master Orchestrator in a Daily Production Scenario.
"""

from client import PersonalAgentOrchestrator

orchestrator = PersonalAgentOrchestrator()

print("=" * 64)
print("DEMO: Personal Agent Ambient & Circadian Life Management")
print("=" * 64)

# 1. Circadian Task Scheduling
tasks = [
    {"id": "t1", "title": "System Architecture Deep-Dive", "cognitive_load": 0.95, "duration_minutes": 90},
    {"id": "t2", "title": "Vendor Contract Review", "cognitive_load": 0.70, "duration_minutes": 45},
    {"id": "t3", "title": "Inbox & Receipt Reconciliation", "cognitive_load": 0.30, "duration_minutes": 30},
    {"id": "t4", "title": "Team Catchup Notes", "cognitive_load": 0.40, "duration_minutes": 30}
]

schedule_res = orchestrator.schedule_circadian_focus_blocks(tasks, circadian_peak_hour=10.5, current_hrv_readiness=0.90)
print(f"\n1. Circadian Schedule (Avg Fit: {schedule_res['average_cognitive_fit'] * 100:.1f}%):")
for item in schedule_res["schedule"]:
    print(f"  [{item['scheduled_slot']}] {item['title']} (Load: {item['cognitive_load']:.2f} | Fit: {item['cognitive_fit_score']:.2f})")

# 2. Ambient Focus State Fusion
ambient = orchestrator.fuse_multimodal_ambient_intent(
    screen_active_app="VS Code / Python IDE",
    user_typing_wpm=68.5,
    calendar_minutes_to_next_meeting=75,
    unread_notifications_count=4
)
print(f"\n2. Ambient State Fusion: State={ambient['inferred_state']} (Focus Index: {ambient['focus_index']})")
print(f"   Policy: {ambient['ambient_action_policy']}")

# 3. Proactive Interruption Thresholding
candidate1 = "Flight delay of 45 minutes for flight departing in 3 hours"
int1 = orchestrator.evaluate_proactive_intervention_threshold(candidate1, importance_score=0.90, user_focus_index=ambient["focus_index"])
print(f"\n3. Interruption 1: '{candidate1}'")
print(f"   Decision: {int1['decision']} via {int1['delivery_channel']} (Net Utility: {int1['net_utility']})")

candidate2 = "Newsletter digest: Top 10 Python tips this week"
int2 = orchestrator.evaluate_proactive_intervention_threshold(candidate2, importance_score=0.20, user_focus_index=ambient["focus_index"])
print(f"\n4. Interruption 2: '{candidate2}'")
print(f"   Decision: {int2['decision']} via {int2['delivery_channel']} (Net Utility: {int2['net_utility']})")

print("\nPersonal Agent Orchestrator execution successful!")
