def label_sentiments(score):
    """
    Convert VADER compound score into sentiment label.
    
    Parameters:
    - score (float): Compound score from VADER (-1 to 1).
    
    Returns:
    - str: 'positive', 'negative', or 'neutral'
    """
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'
