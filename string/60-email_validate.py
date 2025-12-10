# Validate email format using simple logic.
email = "test@example.com"
for i in email:
    if i == "@":
        break
else:
    print("Valid email")