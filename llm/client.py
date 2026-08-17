from google import genai
from config import get_gemini_api_key

def create_gemini_client():
#create and return final gemini client
	api_key =  get_gemini_api_key()

	return genai.Client(api_key= api_key)


