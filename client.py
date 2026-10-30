# -*- coding: utf-8 -*-
"""
Personal Agent Master Orchestrator Client
Zero-dependency circadian energy-adaptive task scheduler, multimodal ambient intent fusion,
and proactive intervention thresholding for sovereign personal AI companions.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentOrchestrator:
    """
    Sovereign Personal Agent core orchestrator.
    Dynamically aligns daily workloads with physiological circadian rhythms,
    evaluates ambient multimodal contexts without invasive prompt fatigue,
    and governs proactive intervention thresholds.
    """

    def schedule_circadian_focus_blocks(
        self,
        tasks: List[Dict[str, Any]],
        circadian_peak_hour: float = 10.0,
        current_hrv_readiness: float = 0.85
    ) -> Dict[str, Any]:
        """
        Schedules cognitive workload matching task cognitive complexity to user's
        circadian energy curve: Energy(h) = Readiness * exp(-((h - Peak)/3.5)^2).
        Task format: {"id": "t1", "title": "Write Spec", "cognitive_load": 0.9, "duration_minutes": 60}
        """
        if not tasks:
            raise ValueError("Task list cannot be empty.")

        # Sort tasks descending by cognitive load
        sorted_tasks = sorted(tasks, key=lambda t: t.get("cognitive_load", 0.5), reverse=True)

        # Discretize work hours into 8 standard slots (9:00 to 17:00)
        time_slots = []
        for hour in range(9, 17):
            dist = hour - circadian_peak_hour
            # Circadian energy function
            energy = round(current_hrv_readiness * math.exp(- (dist * dist) / (2.0 * 2.5 * 2.5)), 3)
            time_slots.append({"hour": hour, "time_label": f"{hour:02d}:00", "available_energy": energy, "assigned_tasks": []})

        # Match heaviest cognitive load to highest available energy slots
        allocated_tasks = []
        for task in sorted_tasks:
            c_load = task.get("cognitive_load", 0.5)
            # Find slot with highest energy that has capacity
            best_slot = max(time_slots, key=lambda s: s["available_energy"])
            
            allocated_tasks.append({
                "task_id": task.get("id"),
                "title": task.get("title"),
                "cognitive_load": c_load,
                "scheduled_slot": best_slot["time_label"],
                "slot_energy_level": best_slot["available_energy"],
                "cognitive_fit_score": round(1.0 - abs(c_load - best_slot["available_energy"]), 3)
            })
            best_slot["assigned_tasks"].append(task.get("id"))
            # Energy depletion penalty for the slot
            best_slot["available_energy"] = round(max(0.1, best_slot["available_energy"] - 0.25), 3)

        mean_fit = round(sum(t["cognitive_fit_score"] for t in allocated_tasks) / len(allocated_tasks), 3)

        return {
            "total_tasks_scheduled": len(allocated_tasks),
            "circadian_peak_hour": circadian_peak_hour,
            "current_hrv_readiness": current_hrv_readiness,
            "average_cognitive_fit": mean_fit,
            "schedule": allocated_tasks,
            "circadian_recommendation": "OPTIMAL_FLOW_STATE" if mean_fit >= 0.75 else "REDUCE_AFTERNOON_LOAD"
        }

    def fuse_multimodal_ambient_intent(
        self,
        screen_active_app: str,
        user_typing_wpm: float,
        calendar_minutes_to_next_meeting: int,
        unread_notifications_count: int
    ) -> Dict[str, Any]:
        """
        Fuses passive ambient signals to infer user focus state and urgency without manual prompting.
        """
        # Deep focus score calculation
        flow_typing = min(1.0, user_typing_wpm / 80.0) if user_typing_wpm > 0 else 0.1
        meeting_proximity_pressure = max(0.0, 1.0 - (calendar_minutes_to_next_meeting / 60.0)) if calendar_minutes_to_next_meeting < 60 else 0.0
        notification_distraction = min(1.0, unread_notifications_count / 15.0)

        # Focus index (0.0 to 1.0)
        focus_index = round(max(0.0, min(1.0, flow_typing * 0.6 + (1.0 - notification_distraction) * 0.4 - meeting_proximity_pressure * 0.3)), 3)

        if focus_index >= 0.7:
            state = "DEEP_WORK_FLOW"
            action_policy = "DO_NOT_DISTURB_SILENT_BUFFER"
        elif meeting_proximity_pressure >= 0.6:
            state = "PRE_MEETING_TRANSITION"
            action_policy = "SURFACE_UPCOMING_BRIEF_AND_LINKS"
        elif notification_distraction >= 0.5:
            state = "ATTENTION_FRAGMENTED"
            action_policy = "SUMMARIZE_AND_TRIAGE_NOTIFICATIONS"
        else:
            state = "CASUAL_BROWSING"
            action_policy = "PROACTIVE_SERENDIPITY_SUGGESTIONS"

        return {
            "screen_app": screen_active_app,
            "inferred_state": state,
            "focus_index": focus_index,
            "ambient_action_policy": action_policy,
            "meeting_proximity_pressure": round(meeting_proximity_pressure, 2),
            "notification_load_penalty": round(notification_distraction, 2)
        }

    def evaluate_proactive_intervention_threshold(
        self,
        candidate_intervention: str,
        importance_score: float,
        user_focus_index: float,
        interruption_cost: float = 0.6
    ) -> Dict[str, Any]:
        """
        Evaluates whether the agent should proactively interrupt the user.
        Utility = Importance - (interruption_cost * user_focus_index).
        Interrupt only if Utility > 0.35.
        """
        importance = max(0.0, min(1.0, importance_score))
        focus = max(0.0, min(1.0, user_focus_index))

        net_utility = round(importance - (interruption_cost * focus), 3)
        should_interrupt = net_utility >= 0.35

        return {
            "candidate_intervention": candidate_intervention,
            "importance_score": importance,
            "user_focus_index": focus,
            "net_utility": net_utility,
            "decision": "PROACTIVELY_INTERRUPT" if should_interrupt else "DEFER_TO_SUMMARY_DIGEST",
            "delivery_channel": "HEADS_UP_BANNER" if should_interrupt else "EPISODIC_NOTIFICATION_DRAWER"
        }
