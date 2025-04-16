import os
import re
import sys

def update_sconstruct_file(base_src_dir, build_number):
    """Updates the point version in the SConstruct file."""
    file_path = os.path.join(base_src_dir, "SConstruct")
    temp_path = file_path + ".temp"
    pattern_to_find = r"(point\s*=\s*)\d+"
    found_and_updated = False

    try:
        with open(file_path, 'r') as original_file, open(temp_path, 'w') as temp_file:
            for line in original_file:
                new_line, changes_made = re.subn(pattern_to_find, r'\g<1>' + build_number, line)
                temp_file.write(new_line)
                if changes_made > 0:
                    found_and_updated = True

        if found_and_updated:
            os.remove(file_path) 
            os.rename(temp_path, file_path) 
            print(f"Updated {os.path.basename(file_path)}")
            return True
        else:
            os.remove(temp_path) 
            print(f"No update needed for {os.path.basename(file_path)}")
            return True 

    except FileNotFoundError:
        print(f"Error: Cannot find file {file_path}", file=sys.stderr)
        return False
    except (IOError, OSError) as e:
        print(f"Error working with file {file_path}: {e}", file=sys.stderr)
        if os.path.exists(temp_path):
            try: os.remove(temp_path)
            except OSError: pass
        return False

def update_version_file(base_src_dir, build_number):
    """Updates the ADLMSDK_VERSION_POINT in the VERSION file."""
    file_path = os.path.join(base_src_dir, "VERSION")
    temp_path = file_path + ".temp"
    pattern_to_find = r"(ADLMSDK_VERSION_POINT\s*=\s*)\d+"
    found_and_updated = False

    try:
        with open(file_path, 'r') as original_file, open(temp_path, 'w') as temp_file:
            for line in original_file:
                new_line, changes_made = re.subn(pattern_to_find, r'\g<1>' + build_number, line)
                temp_file.write(new_line)
                if changes_made > 0:
                    found_and_updated = True

        if found_and_updated:
            os.remove(file_path)
            os.rename(temp_path, file_path)
            print(f"Updated {os.path.basename(file_path)}")
            return True
        else:
            os.remove(temp_path)
            print(f"No update needed for {os.path.basename(file_path)}")
            return True

    except FileNotFoundError:
        print(f"Error: Cannot find file {file_path}", file=sys.stderr)
        return False
    except (IOError, OSError) as e:
        print(f"Error working with file {file_path}: {e}", file=sys.stderr)
        if os.path.exists(temp_path):
             try: os.remove(temp_path)
             except OSError: pass
        return False

def run_updates():
    build_num = os.environ.get("BuildNum")
    source_dir = os.environ.get("SourcePath")

    if not build_num:
        print("Error: BuildNum environment variable not set.", file=sys.stderr)
        sys.exit(1)
    if not source_dir:
        print("Error: SourcePath environment variable not set.", file=sys.stderr)
        sys.exit(1)
    if not build_num.isdigit():
         print(f"Error: BuildNum ('{build_num}') is not a simple number.", file=sys.stderr)
         sys.exit(1)

    src_path = os.path.join(source_dir, "develop", "global", "src")

    sconstruct_success = update_sconstruct_file(src_path, build_num)
    version_success = update_version_file(src_path, build_num)

    if sconstruct_success and version_success:
        print("Finished update process.")
        sys.exit(0)
    else:
        print("Update process failed for one or more files.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_updates() 