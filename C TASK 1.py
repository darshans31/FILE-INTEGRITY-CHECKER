import os
import hashlib
import json

HASHES_FILE = 'file_hashes.json'

def compute_file_hash(file_path, algorithm='sha256'):
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def scan_files(directory, algorithm='sha256'):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for name in files:
            full_path = os.path.join(root, name)
            file_hashes[full_path] = compute_file_hash(full_path, algorithm)
    return file_hashes

def save_hashes(hashes, file_path=HASHES_FILE):
    with open(file_path, 'w') as f:
        json.dump(hashes, f, indent=2)

def load_hashes(file_path=HASHES_FILE):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as f:
        return json.load(f)

def compare_hashes(old_hashes, new_hashes):
    changes = {'modified': [], 'deleted': [], 'added': []}
    for path in old_hashes:
        if path not in new_hashes:
            changes['deleted'].append(path)
        elif old_hashes[path] != new_hashes[path]:
            changes['modified'].append(path)
    for path in new_hashes:
        if path not in old_hashes:
            changes['added'].append(path)
    return changes
if __name__ == "__main__":
    
    target_dir = input("Enter the directory to monitor: ").strip()
    mode = input("Type 'init' to save hashes or 'check' to verify integrity: ").strip()

    if mode == 'init':
        hashes = scan_files(target_dir)
        save_hashes(hashes)
        print("Initial hashes saved.")
    elif mode == 'check':
        old_hashes = load_hashes()
        new_hashes = scan_files(target_dir)
        result = compare_hashes(old_hashes, new_hashes)
        print("Scan complete. Changes detected:")
        print(json.dumps(result, indent=2))
    else:
        print("Unknown mode. Use 'init' or 'check'.")