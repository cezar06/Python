import pyttsx3
import sys
import os

def is_valid_file_name(file_name):
    invalid_characters = "\\/:*?\"<>|"
    for character in invalid_characters:
        if character in file_name:
            return False
    return True

def convert_line_to_mp3(text, output_file_path):
    engine = pyttsx3.init()
    tts_voices = engine.getProperty('voices')
    engine.setProperty('voice', tts_voices[1].id)
    engine.save_to_file(text, output_file_path)
    engine.runAndWait()

def convert_dir_to_mp3(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        line = line.strip()
                        if len(line) == 0:
                            continue
                        if is_valid_file_name(line):
                            if line[-1] == '.': line = line[:-1]
                            output_file_path = os.path.join(output_directory, line + '.mp3')
                            convert_line_to_mp3(line, output_file_path)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Wrong usage, instead try: python ttsfiles.py input_directory output_directory')
        sys.exit(1)
    convert_dir_to_mp3(sys.argv[1], sys.argv[2])
