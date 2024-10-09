# Participants in two separate events
event1_participants = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
event2_participants = ['Charlie', 'Eva', 'George', 'Hannah', 'Alice']

# Step 1: Convert lists to sets
event1_set = set(event1_participants)
event2_set = set(event2_participants)

# 1. Find participants who attended both events
both_events = event1_set.intersection(event2_set)
print("Participants who attended both events:", both_events)

# 2. Find participants who attended only one event
one_event_only = event1_set.symmetric_difference(event2_set)
print("Participants who attended only one event:", one_event_only)

# 3. List all unique participants who attended either event
all_participants = event1_set.union(event2_set)
print("All unique participants:", all_participants)

# 4. Remove a participant named 'Eva' from the set of all participants
all_participants.discard('Eva')
print("All unique participants after removing 'Eva':", all_participants)
