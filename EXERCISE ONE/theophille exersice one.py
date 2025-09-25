import array

# Integers: Simulated data for number of students in each room
room_student_counts = [3, 4, 2, 5, 4, 3]
total_students = sum(room_student_counts)
average_students = total_students / len(room_student_counts)
min_students = min(room_student_counts)
max_students = max(room_student_counts)

# Strings: Formatted report using f-strings
report = (
    f"--- Dormitory Room Allocation Report ---\n"
    f"Total rooms: {len(room_student_counts)}\n"
    f"Total students: {total_students}\n"
    f"Average students per room: {average_students:.2f}\n"
    f"Minimum students in a room: {min_students}\n"
    f"Maximum students in a room: {max_students}\n"
)
# Two f-strings in use
summary = f"Summary: {total_students} students across {len(room_student_counts)} rooms."
average_report = f"Avg. occupancy: {average_students:.2f} students/room."

print(report)
print(summary)
print(average_report)

# Booleans: Threshold condition (e.g., standard is 3.5 students per room)
THRESHOLD = 3.5
if (average_students > THRESHOLD) and (max_students > 4):
    print("Status: Above Standard (High occupancy and at least one crowded room)")
elif (average_students > THRESHOLD) or (max_students > 4):
    print("Status: Marginally Above Standard")
else:
    print("Status: Below Standard (Occupancy is within limits)")

# Lists: Rooms list
rooms = ['Room A', 'Room B', 'Room C', 'Room D']
print("\nRooms before modification:", rooms)
# Add a new room
rooms.append('Room E')
# Remove a room if it starts with 'C'
for room in rooms:
    if room.startswith('Room C'):
        rooms.remove(room)
        break
rooms.sort()
print("Rooms after modification and sorting:", rooms)

# Arrays: Using array module for numeric subset
student_array = array.array('i', room_student_counts[:4])  # fixed-size for first 4 rooms
array_sum = sum(student_array)
list_sum = sum(room_student_counts[:4])
print(f"\nSum of students (array): {array_sum}")
print(f"Sum of students (list): {list_sum}")
print("Array and list sums are equal:", array_sum == list_sum)

# Dictionaries: List of room records
room_records = [
    {'id': 101, 'name': 'Room A', 'value': 3},
    {'id': 102, 'name': 'Room B', 'value': 4},
    {'id': 103, 'name': 'Room C', 'value': 2},
    {'id': 104, 'name': 'Room D', 'value': 5}
]
# Update Room B's value
for record in room_records:
    if record['name'] == 'Room B':
        record['value'] = 5
# Delete Room C's record
room_records = [rec for rec in room_records if rec['name'] != 'Room C']
# Compute total value
total_value = sum(rec['value'] for rec in room_records)
print(f"\nRoom records after update and delete: {room_records}")
print(f"Total students in remaining rooms (from dictionary): {total_value}")