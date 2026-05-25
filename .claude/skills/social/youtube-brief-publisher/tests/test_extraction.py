import os
import sys
import unittest
from unittest.mock import patch

# Ajuster le path pour importer les scripts locaux
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from scripts.transcribe_elevenlabs import run_transcription_pipeline


class TestTranscriptionPipeline(unittest.TestCase):
    @patch("scripts.transcribe_elevenlabs.download_youtube_audio")
    @patch("scripts.transcribe_elevenlabs.transcribe_audio_elevenlabs")
    def test_pipeline_success(self, mock_transcribe, mock_download):
        # Configurer les mocks
        mock_download.return_value = "/tmp/mock_video.mp3"
        mock_transcribe.return_value = {
            "clean_transcript": "Ceci est une transcription de test pour schoolsWP.",
            "word_count": 9,
        }

        # Exécuter
        res = run_transcription_pipeline("https://www.youtube.com/watch?v=12345678901", "mock_key")

        # Vérifications
        self.assertEqual(res["clean_transcript"], "Ceci est une transcription de test pour schoolsWP.")
        self.assertEqual(res["word_count"], 9)
        mock_download.assert_called_once()
        mock_transcribe.assert_called_once_with("/tmp/mock_video.mp3", "mock_key", "scribe_v2", "fra")


if __name__ == "__main__":
    unittest.main()
