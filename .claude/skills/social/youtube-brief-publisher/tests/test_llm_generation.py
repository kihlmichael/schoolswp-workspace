import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Ajuster le path pour importer les scripts locaux
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from scripts.run_pipeline import generate_script_brief, generate_seo_metadata


class TestLLMGeneration(unittest.TestCase):
    @patch("requests.post")
    def test_generate_script_brief(self, mock_post):
        # Mocker la réponse API d'Anthropic pour Sonnet
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"content": [{"text": "Voici mon script vidéo original au JE."}]}
        mock_post.return_value = mock_response

        # Exécuter
        res = generate_script_brief(
            transcript="Transcription brute de test",
            user_brief="Mon brief d'angle",
            output_lang="francais",
            api_key="mock_anthropic_key",
        )

        self.assertEqual(res, "Voici mon script vidéo original au JE.")
        mock_post.assert_called_once()

    @patch("requests.post")
    def test_generate_seo_metadata(self, mock_post):
        # Mocker la réponse API d'Anthropic pour Haiku (retourne du JSON)
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "content": [
                {
                    "text": '{\n  "title": "Titre de test",\n  "description": "Description de test",\n  "tags": ["tag1", "tag2"]\n}'
                }
            ]
        }
        mock_post.return_value = mock_response

        # Exécuter
        res = generate_seo_metadata(script_content="Mon script de test", api_key="mock_anthropic_key")

        self.assertEqual(res["title"], "Titre de test")
        self.assertEqual(res["description"], "Description de test")
        self.assertEqual(res["tags"], ["tag1", "tag2"])
        mock_post.assert_called_once()


if __name__ == "__main__":
    unittest.main()
