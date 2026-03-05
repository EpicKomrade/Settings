def calculate_reward(current_score, win_percentage):
    # Handle empty or invalid input
    if current_score in ("", None):
        return 0

    # Convert to float safely
    try:
        score = float(current_score)
    except (TypeError, ValueError):
        return 0  

    # 0 is neutral
    if score == 0:
        return 0

    # 1–7 LERP scaled rewards (0 → 1 at 7)
    if 1 <= score <= 7:
        return round(score / 7, 2)

    # 8+ scores: original formula with streak/history bonus
    if score >= 8:
        try:
            # Convert win_percentage string like "60%" to float
            if isinstance(win_percentage, str) and win_percentage.endswith("%"):
                win_pct = float(win_percentage.rstrip("%")) / 100
            else:
                win_pct = float(win_percentage)
        except (TypeError, ValueError):
            win_pct = 0.5  # default if invalid

        # Original positive calculation
        base_calc = round(((score - 7.9) * 2.2) + ((win_pct - 0.5) * 4), 1)

        # Enforce minimum baseline of 1.5
        return max(base_calc, 1.5)

    # For scores between 7 and 8 (like 7.1–7.9), treat as 0 points
    return 0
