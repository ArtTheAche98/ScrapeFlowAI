import os
import re
import logging

from openai import OpenAI

logger = logging.getLogger(__name__)


class ContentOptimizer:
    def __init__(self):
        self.client = OpenAI(
            # api_key=os.getenv('DEEPSEEK_API_KEY'),
            api_key=os.getenv('AILAB_API_KEY'),
            base_url="https://api.ailab.ge",
            # base_url="https://api.deepseek.com/v1"
        )

    def optimize_content(self, content, style='INSIGHTS'):
        """Optimize content using DeepSeek AI"""
        style_prompts = {
            'NEWS': (
                "Rewrite the following article as a professional LinkedIn post. "
                "Summarize the main points in your own words, avoid generic phrases, do not mention 'link in comments', "
                "and do not use placeholders like [context]. Write as if you are the author sharing insights directly. "
                "Make the post engaging and informative, at least 150 words."
            ),
            'INSIGHTS': (
                "Summarize the following content into a LinkedIn post that shares key insights. "
                "Do not use generic phrases, do not mention 'link in comments', and do not use placeholders. "
                "Write as if you are the expert sharing your perspective. Make it at least 150 words."
            ),
            'SUMMARY': (
                "Write a LinkedIn post summarizing the following content. "
                "Do not use generic phrases, do not mention 'link in comments', and do not use placeholders. "
                "Make it concise, engaging, and at least 100 words."
            ),
            'QUOTES': (
                "Extract and highlight key quotes and insights from the following content for a LinkedIn post. "
                "Do not use generic phrases, do not mention 'link in comments', and do not use placeholders. "
                "Use direct quotes only if they are present in the content. Ensure the post is at least 100 words."
            ),
        }

        prompt = style_prompts.get(style, style_prompts['INSIGHTS'])
        
        try:
            logger.info("Attempting to call DeepSeek API...")
            response = self.client.chat.completions.create(
                # model="deepseek-chat",
                model="kona",
                messages=[
                    {
                    "role": "system", 
                    "content": (
                        "You are a professional LinkedIn content writer. "
                        "You are a professional content optimizer for LinkedIn."
                        "Write a complete, ready-to-post LinkedIn update in plain text. "
                        "Absolutely do not use markdown, links, or hashtags. If you see any, remove them. "
                        "Do NOT use any formatting like bold, italics, or lists. "
                        "Do NOT include any placeholders like [context] or [link in comments]. "
                        "Do NOT include any links or placeholders like [here] or (link in comments). "
                        "Do NOT use hashtags. "
                        "Do NOT use generic phrases, buzzwords or placeholders. "
                        "Write in a natural, engaging, and informative style."
                    )
            },
                    {"role": "user", "content": f"{prompt}\n\n{content}"}
                ],
                max_tokens=500,
                temperature=0.7
            )
            logger.info(f"Raw API Response: {response}")

            
            optimized_content = response.choices[0].message.content
            return optimized_content
        except Exception as e:
            print(f"Error optimizing content: {str(e)}")
            return None