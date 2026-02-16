def move_disk(source, destination, s_name, d_name):
    disk = source.pop()           # Remove top disk
    destination.append(disk)      # Place on destination
    print(f"Move disk {disk} from {s_name} to {d_name}")

def tower_of_hanoi(n, source, auxiliary, destination, s_name, a_name, d_name):
    if n == 1:
        move_disk(source, destination, s_name, d_name)
        return
    
    tower_of_hanoi(n-1, source, destination, auxiliary, s_name, d_name, a_name)
    move_disk(source, destination, s_name, d_name)
    tower_of_hanoi(n-1, auxiliary, source, destination, a_name, s_name, d_name)

# Number of disks
n = 3

# Using arrays (lists) as stacks
source = list(range(n, 0, -1))   # [3,2,1]
auxiliary = []
destination = []

tower_of_hanoi(n, source, auxiliary, destination, "A", "B", "C")

print("\nFinal Destination Rod:", destination)
