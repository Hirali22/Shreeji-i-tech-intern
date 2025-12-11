# Create a closure-based login attempt limiter
def login_attempt_limiter(max_attempts):
    attempts = 0
    def inner():
        nonlocal attempts
        attempts += 1
        if attempts <= max_attempts:
            return "Login successful"
        else:
            return "Login failed. Too many attempts."
    return inner