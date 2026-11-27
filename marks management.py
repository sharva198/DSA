class Node:
	def __init__(self, score):
		self.score = score
		self.left = None
		self.right = None
# 1. Insert a score using a simple while loop
def insert(root, score):
def insert(root, score):
	new_node = Node(score)
	if root is None:
		return new_node
	curr = root
	while True:
		if score < curr.score:
			if curr.left is None:
				curr.left = new_node
				break
			curr = curr.left
		else:
			if curr.right is None:
				curr.right = new_node
				break
			curr = curr.right
	return root
# 2. Display scores in ascending order (Left -> Root -> Right)
def get_ascending(root):
	if root is None:
		return []
	return get_ascending(root.left) + [root.score] + get_ascending(root.right)
# 3. Find lowest (extreme left) and highest (extreme right)
def find_min(root):
	while root.left:
		root = root.left
	return root.score
def find_max(root):
	while root.right:
		root = root.right
	return root.score
# 5. Search for a particular score using a while loop
def search(root, target):
	while root:
		if target == root.score:
			return True
		elif target < root.score:
			root = root.left
		else:
			root = root.right
	return False
# --- Main Program ---
scores = [45, 78, 32, 89, 56, 92, 67, 34, 85, 73, 61, 98]
root = None
# Task 1: Insert all scores
for s in scores:
	root = insert(root, s)
# Task 2: Ascending order
sorted_scores = get_ascending(root)
print("2. Ascending order:", sorted_scores)
# Task 3: Highest and lowest
print("3. Lowest:", find_min(root), "| Highest:", find_max(root))
# Task 4: Count students scoring above 50
above_50 = len([s for s in sorted_scores if s > 50])
print("4. Count above 50:", above_50)
# Task 5: Search for a score
print("5. Search 73:", "Found" if search(root, 73) else "Not Found")
# Task 6: Average score
average = sum(sorted_scores) / len(sorted_scores)
print(f"6. Average score: {average:.2f}")