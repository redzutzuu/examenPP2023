class AudioPlayer:
    def play(self):
        print("Playing music...")

    def stop(self):
        print("Stopping music...")

    def record(self):
        print("Recording audio...")

class Radio:
    def tune(self, frequency):
        print(f"Tuning to radio station at frequency {frequency}...")

    def listen(self):
        print("Listening to radio...")

class BoomboxFacade:
    def __init__(self):
        self.audio_player = AudioPlayer()
        self.radio = Radio()

    def play_music(self):
        self.audio_player.play()

    def stop_music(self):
        self.audio_player.stop()

    def record_audio(self):
        self.audio_player.record()

    def tune_to_radio(self, frequency):
        self.radio.tune(frequency)

    def listen_to_radio(self):
        self.radio.listen()

def main():
    boombox = BoomboxFacade()

    # Redare muzică
    boombox.play_music()

    # Înregistrare audio
    boombox.record_audio()

    # Ascultare radio
    boombox.tune_to_radio(98.5)
    boombox.listen_to_radio()

if __name__ == "__main__":
    main()
