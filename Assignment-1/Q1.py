# Q1.py
# This program demonstrates how immutable default parameters behave

def count_message(msg, count=0):
    """
    Accepts a message and a default count.
    Since integers are immutable, the count does NOT persist across calls.
    """
    count += 1
    print(f"Message: {msg}, Count: {count}")
    return count


# Sample calls
count_message("heya")
count_message("hello")
count_message("welcome")
