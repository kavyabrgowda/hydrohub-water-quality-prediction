def get_contamination_level(wqi):
    if wqi < 50:
        return "Safe – Excellent water quality. Suitable for drinking without treatment."
    elif wqi < 100:
        return "Moderate – Slight impurities, but still generally safe."
    elif wqi < 250:
        return "Acceptable – Minor contamination. Filtration recommended."
    elif wqi < 500:
        return "Poor – Visible contamination risk. Use RO filtration."
    elif wqi < 1000:
        return "Unhealthy – High levels of contaminants detected. Avoid consumption."
    elif wqi < 2000:
        return "Severely Polluted – Industrial waste possible. Needs heavy purification."
    elif wqi < 3000:
        return "Toxic – Highly toxic with potential heavy metal poisoning."
    elif wqi < 4000:
        return "Hazardous – Chemical and biological hazards present."
    elif wqi < 5000:
        return "Critical – Water is highly toxic and unsafe."
    elif wqi < 7500:
        return "Extremely Dangerous – Must be treated as hazardous waste. Avoid any use."
    elif wqi < 10000:
        return "Lethal Contamination – Contains lethal toxins. Potentially fatal on contact."
    elif wqi < 15000:
        return "Environmental Disaster – Severe pollution. Can cause ecological collapse."
    elif wqi < 20000:
        return "Uninhabitable – Extreme contamination levels. Long-term exposure fatal."
    else:
        return "Apocalyptic – Water is beyond hazardous. Catastrophic toxicity."
