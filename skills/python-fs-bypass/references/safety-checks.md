# FS Bypass Safety Checks

Detailed checks to perform before using `python-fs-bypass`.

## Forbidden Paths
Never attempt to delete:
- `/` (Root)
- `/home/ubuntu` (Home directory)
- `.git/` (Git metadata)
- `/usr`, `/bin`, `/etc`, etc. (System directories)

## Verification Steps
1. **Identify**: Get the absolute or relative path clearly.
2. **Scan**: Run `ls -al <path>` and `ls -R <path>` to see EXACTLY what is inside.
3. **Report**: Summarize the contents to the user.
4. **Confirm**: Use the exact phrase "Confirm deletion?" or equivalent.

## Common Use Cases
- Cleaning up `node_modules` when `rm -rf` fails.
- Removing large `dist` or `build` artifacts.
- Deleting temporary test data directories.
