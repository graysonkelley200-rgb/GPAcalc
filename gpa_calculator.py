"""GPA Calculator

Accepts credits per class (0.5 – 6, in steps of 0.5) and a percentage
grade (1 – 100) for each class and computes a weighted GPA on a 4.0 scale.
"""

VALID_CREDITS = {x / 10 for x in range(5, 61, 5)}  # 0.5, 1.0, ..., 6.0


def percent_to_grade_points(percent: float) -> float:
    """Convert a percentage grade to grade points on a 4.0 scale."""
    if percent >= 93:
        return 4.0
    elif percent >= 90:
        return 3.7
    elif percent >= 87:
        return 3.3
    elif percent >= 83:
        return 3.0
    elif percent >= 80:
        return 2.7
    elif percent >= 77:
        return 2.3
    elif percent >= 73:
        return 2.0
    elif percent >= 70:
        return 1.7
    elif percent >= 67:
        return 1.3
    elif percent >= 63:
        return 1.0
    elif percent >= 60:
        return 0.7
    else:
        return 0.0


def calculate_gpa(classes: list[tuple[float, float]]) -> float:
    """Calculate weighted GPA from a list of (credits, percent_grade) tuples."""
    total_points = sum(credits * percent_to_grade_points(grade) for credits, grade in classes)
    total_credits = sum(credits for credits, _ in classes)
    return total_points / total_credits if total_credits > 0 else 0.0


def get_credits() -> float:
    """Prompt the user for a valid credit value."""
    while True:
        raw = input("  Credits (0.5 – 6, in steps of 0.5): ").strip()
        try:
            value = float(raw)
        except ValueError:
            print("  Please enter a number.")
            continue
        # Round to one decimal place to avoid floating-point issues
        rounded = round(value, 1)
        if rounded not in VALID_CREDITS:
            print("  Credits must be between 0.5 and 6.0 in steps of 0.5.")
            continue
        return rounded


def get_grade() -> float:
    """Prompt the user for a valid percentage grade."""
    while True:
        raw = input("  Grade (1 – 100 as a percent): ").strip()
        try:
            value = float(raw)
        except ValueError:
            print("  Please enter a number.")
            continue
        if not (1 <= value <= 100):
            print("  Grade must be between 1 and 100.")
            continue
        return value


def main() -> None:
    print("=== GPA Calculator ===")
    print("Enter your classes one at a time. Type 'done' when finished.\n")

    classes: list[tuple[float, float]] = []
    class_num = 1

    while True:
        prompt = input(f"Add class {class_num}? (yes/done): ").strip().lower()
        if prompt in ("done", "d", "no", "n"):
            break
        if prompt not in ("yes", "y", ""):
            print("Please type 'yes' to add a class or 'done' to finish.")
            continue

        credits = get_credits()
        grade = get_grade()
        classes.append((credits, grade))
        grade_points = percent_to_grade_points(grade)
        print(f"  → {credits} credit(s), {grade}% = {grade_points:.1f} grade points\n")
        class_num += 1

    if not classes:
        print("No classes entered. Exiting.")
        return

    gpa = calculate_gpa(classes)
    print(f"\nYour GPA: {gpa:.2f} / 4.00")


if __name__ == "__main__":
    main()
