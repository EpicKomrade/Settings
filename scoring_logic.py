def calculate_reward(current_score, win_percentage):
    # Handle empty or invalid
    if current_score in ("", None):
        return 0

    # Convert to float safely
    try:
        score = float(current_score)
    except (TypeError, ValueError):
        return 0  

    # Your piecewise formula from Google Sheets
    if score <= 2:
        return -3
    elif score > 2 and score < 7:
        # -3 * (1 - (score-2)/5)
        return round(-3 * (1 - (score - 2)/5), 1)
    elif score == 7:
        return 0
    elif score >= 7.9:
        # Original positive calculation
        try:
            if isinstance(win_percentage, str) and win_percentage.endswith("%"):
                win_pct = float(win_percentage.rstrip("%")) / 100
            else:
                win_pct = float(win_percentage)
        except (TypeError, ValueError):
            win_pct = 0.5
            
        base_calc = round(((score - 7.9) * 2.2) + ((win_pct - 0.5) * 4), 1)
        
        # The MAX(IF(OR(...))) logic from your formula
        if base_calc > 0:
            return base_calc
        else:
            return max(base_calc - 1, -3)
    else:
        # Scores between 7 and 7.9
        return 0
