from pydub import AudioSegment

def load_audio_file(fname):
    """load audio file"""
    sound = None
    try:
        if fname.endswith('.mp3') or fname.endswith('.MP3'):
            sound = AudioSegment.from_mp3(fname)
        elif fname.endswith('.wav') or fname.endswith('.WAV'):
            sound = AudioSegment.from_wav(fname)
        elif fname.endswith('.ogg'):
            sound = AudioSegment.from_ogg(fname)
        elif fname.endswith('.flac'):
            sound = AudioSegment.from_file(fname, "flac")
        elif fname.endswith('.3gp'):
            sound = AudioSegment.from_file(fname, "3gp")
        elif fname.endswith('.3g'):
            sound = AudioSegment.from_file(fname, "3gp")

            duration = sound.duration_seconds
    except Exception as e:
        print("Couldn't load file")

        return None, None

    return sound, duration




