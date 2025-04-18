import re

def extract_text_from_pwi_utf8(file_path, save_to_txt=False):
    """
    Extract readable text from a .PWI file using UTF-8 decoding.
    
    Parameters:
        file_path (str): Path to the .pwi file.
        save_to_txt (bool): If True, save the extracted text to a .txt file.
    
    Returns:
        str: The cleaned, extracted text.
    """
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read()

        # Skip the header (typically 512 bytes in PWI files)
        content_data = raw_data[512:]

        # Decode using UTF-8, ignoring undecodable characters
        text = content_data.decode('utf-8', errors='ignore')
    except Exception as e:
        return f"[ERROR] Failed to read or decode the file: {e}"

    # Split text into lines and keep only lines with alphanumeric characters
    lines = text.splitlines()
    filtered_lines = [
        line.strip() for line in lines
        if re.search(r'[A-Za-z0-9]', line.strip())
    ]

    result = '\n'.join(filtered_lines)

    # Optionally save to a .txt file
    if save_to_txt:
        output_path = file_path.replace('.pwi', '_extracted.txt')
        try:
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(result)
            print(f"[INFO] Cleaned text saved to: {output_path}")
        except Exception as e:
            print(f"[ERROR] Failed to save the output file: {e}")

    return result

# === Example Usage ===
if __name__ == "__main__":
    pwi_file_path = 'example.pwi'  # Replace with your actual .pwi file path
    extracted_text = extract_text_from_pwi_utf8(pwi_file_path, save_to_txt=True)

    print("=== Clean Extracted Text ===\n")
    print(extracted_text)
