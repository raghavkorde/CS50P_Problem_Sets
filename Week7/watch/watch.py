import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Regular expression pattern to match a YouTube URL in the format
    # http://youtube.com/embed/... or https://youtube.com/embed/...
    pattern = r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>"
    match = re.search(pattern, s)
    if match:
        # Extract the video ID from the matched URL
        video_id = match.group(2)
        # Convert the URL to the shorter youtu.be format
        return f'https://youtu.be/{video_id}'
    else:
        return None



if __name__ == "__main__":
    main()





