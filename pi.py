import os
import openai
import argparse
import re
from typing import List

def main():
  print("Running example")

  parser = argparse.ArgumentParser()
  parser.add_argument("--input", "-i", type=str, required=True)
  args = parser.parse_args()
  user_input = args.input

  print(f"User Input: {user_input}")
  if validate_length(user_input):
    branding_result = generate_branding_snippet(user_input)
    keywords_text = generate_keywords(user_input)
    print (branding_result)
    print (keywords_text)
  else:
    raise ValueError("Input length is too long.")


def validate_length(prompt: str) -> str:
  return len(prompt) <= 60


def generate_branding_snippet(prompt: str) -> str:
  #load API
  openai.api_key = "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"
  enriched_prompt = f"Generate upbeat branding snippet for {prompt}:"
  print(enriched_prompt)
  response = openai.Completion.create(
    engine="davinci-instruct-beta-v3", prompt=enriched_prompt, max_tokens=30
    )

  #Extract output text
  branding_text: str = response["choices"][0]["text"]
  
  #Strip whitespace
  branding_text = branding_text.strip()
  
  #add ... if the last character is not the end. 
  last_char = branding_text[-1]

  if last_char not in [".", "!", "?"]:
    branding_text += "..."

  return branding_text


def generate_keywords(prompt: str) -> List[str]:
  #load API
  openai.api_key = "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"
  enriched_prompt = f"Generate related branding keywords for {prompt}:"
  print(enriched_prompt)
  response = openai.Completion.create(
    engine="davinci-instruct-beta-v3", prompt=enriched_prompt, max_tokens=30
    )

  #Extract output text
  keywords_text: str = response["choices"][0]["text"]
  
  #Strip whitespace
  keywords_text = keywords_text.strip()
  keywords_array = re.split(",|\n|-", keywords_text)
  keywords_array = [k.lower().strip() for k in keywords_array]
  keywords_array = [k for k in keywords_array if len(k) > 0]

  return keywords_array
  


if __name__ == "__main__":
  main()