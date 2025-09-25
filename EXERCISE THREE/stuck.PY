# Stack: LIFO (Last In, First Out)
email_stack = []

# Push actions
email_stack.append("Open Email")
email_stack.append("Type Message")
email_stack.append("Send")

# Undo last action
email_stack.pop()

# What's left?
print("Remaining actions:", email_stack)