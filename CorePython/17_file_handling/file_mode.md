## Python File Modes

| Mode | Description |
|------|-------------|
| `r`  | Read mode — opens the file for reading. File must exist. |
| `w`  | Write mode — creates or overwrites the file. |
| `a`  | Append mode — opens file and writes at the end (does not overwrite). |
| `r+` | Read + Write — file must exist; does not truncate. |
| `w+` | Write + Read — creates or overwrites the file. |
| `a+` | Append + Read — writes at end; file created if missing. |
| `rb`, `wb`, `ab` | Same as above but in **binary** mode. |

### Quick Summary
- **`r`** → read
- **`w`** → write (overwrite)
- **`a`** → append
- **`+`** → read + write combo
- **`b`** → binary files
