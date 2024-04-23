
def is_criticality_balanced(temperature, neutrons_emitted):
    product = temperature * neutrons_emitted
    if temperature < 800 and neutrons_emitted > 500 and product < 500000.0:
        return True
    return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percentage =(generated_power / theoretical_max_power) * 100
    if percentage >= 80:
        return 'green'
    if percentage >= 60:
        return 'orange'
    if percentage >= 30:
        return 'red'
    return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    total = temperature * neutrons_produced_per_second
    if total < threshold * 0.9:
        return 'LOW'
    if threshold * 0.9 < total < threshold * 1.1:
        return 'NORMAL'
    return 'DANGER'
    