# FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: DARSHAN S

*INTERN ID*: CT04DR855

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR


### Description of the Code and Its Workflow

The script starts by defining constants and functions to handle file hashing, directory traversal, and state comparison. Its workflow is as follows:

- *File Hash Calculation:* The compute_file_hash function reads a file in binary chunks and computes its hash using a specified algorithm (default is sha256). Hashing ensures even tiny changes in file contents are detected, as hash values will differ if the file is altered in any way.
- *Recursive Directory Scanning:* The scan_files function walks through a directory and subdirectories using os.walk. For each file found, it computes the hash and stores it in a dictionary with the path as the key.
- *State Persistence:* Hashes are saved to disk using json.dump for future comparison (save_hashes function) and loaded with json.load (load_hashes function). This provides a snapshot of the directory’s state at any given time.
- *Change Detection:* The core function compare_hashes evaluates the previous and current file hash dictionaries. It identifies deleted files (present in old, not in new), added files (present in new, not in old), and modified files (present in both, but with different hashes).
- *Interactive CLI:* The script’s entry point handles user input, prompting for a directory and mode (init to save current state, check to compare with last saved state), and prints detected changes in a structured JSON format.

### Core Tools and Libraries Used

- *Python Standard Library:*
  - os: For directory traversal and file path management, which enables platform-independent operations.
  - hashlib: For calculating cryptographic hashes, critical for ensuring data integrity and detecting unauthorized changes.
  - json: For serializing hash data to disk and deserializing it during comparison, ensuring portability and readability of stored file integrity records.

### Potential Applications

This script is highly relevant for systems requiring change monitoring or intrusion detection, including:

- *Security and Compliance:* Detects unauthorized or accidental changes to critical files (e.g., configuration files, executables). Useful in environments subject to audits or requiring evidence of data integrity, like HIPAA or PCI-DSS regulated systems.
- *Backup Verification:* Confirms that files haven’t changed between backup cycles, protecting against silent data corruption or ransomware.
- *File System Monitoring:* Can be integrated into larger monitoring frameworks to alert administrators when unexpected changes occur.
- *Penetration Testing and Cybersecurity:* Helps track modifications in sensitive areas during tests or incident response.

### Extensions and Integrations

- Third-party frameworks like OSSEC or Samhain perform similar integrity checks with more extensive features (alerts, reporting, remediation). This script can be extended to support those environments by adding networking features, more hashing algorithms, or automated alerting.
- Pairing with automated deployment pipelines ensures code and configuration integrity before and after updates.

### Why These Tools?

Using the Python standard libraries guarantees cross-platform compatibility, ease of maintenance, and minimizes external dependencies. Employing hash functions rather than simple timestamp or size checks greatly increases reliability in detecting file changes, as hashes are immune to certain evasive techniques and accidental overwrites.

### Conclusion

This script offers a practical solution for detecting file changes in a directory using proven Python tools, making it a valuable utility for system administrators, security analysts, and developers needing a lightweight, customizable integrity monitoring tool within their workflows.
